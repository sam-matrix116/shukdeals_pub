from multiprocessing import context
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from account.api.serializers import *
from account.models import *
from account.utils import *
from account.utils import convert_currency as __, render_to_pdf
from django.template.loader import get_template
from django.utils.translation import gettext as _
import datetime
from django.utils import timezone
from shuktv.utils.customPermissionClass import IsNGO, IsNormalUser
from shuktv.utils.customPaginations import paginated_data
from deals.api.serializers import BusinessDealSerializer
from classifieds.api.serializers import ClassifiedSerializer
from jobs.api.serializers import JobDetailSerializer
from django.db.models import Q
from django.conf import settings
from account.managestripe import *
from account.managetranzila import *
from shuktv.utils.misc import blacklist_token
import rest_framework_simplejwt
from rest_framework_simplejwt.views import TokenRefreshView
from django.db.models import Sum, Q, Count, Avg, Min
from deals.utils import *
from django.http import JsonResponse


import logging
logger = logging.getLogger('demo_log')
logger = logging.getLogger('django')


class TokenRefreshAPIView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer


class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):

        logger.info("Registration Start")

        user_type = request.data.get('user_type',None)
        email = request.data.get('email')
        phone = request.data.get('phone')
        password = request.data.get('password', None)
        confirm_password = request.data.get('confirm_password', None)

        # validations start
        
        if not password:
            return Response({
                'status': False,
                'message': _("Password is required"),
                'field': 'password'
            }, status=400)
        elif not confirm_password:
            return Response({
                'status': False,
                'message': _('Confirm Password is required'),
                'field': 'confirm_password'
            }, status=400)

        elif password != confirm_password:
            return Response({
                'status': False,
                'message': _('Password and Confirm password do not match'),
                'field': 'password'
            }, status=400)

        elif len(password) < 8:
            return Response({
                'status': False,
                'message': _('Password must be atleast 8 characters')
            }, status=400)
        # validations end

        try:
            phone_already_exists = MyUser.objects.get(phone=phone)
        except:
            phone_already_exists = None

        try:
            email_already_exists = MyUser.objects.get(email=email)
        except:
            email_already_exists = None
        
        if email_already_exists or phone_already_exists:
            
            if email_already_exists:
                old_user = email_already_exists
                old_user_phone_email = old_user.email
                email_or_phone = 'email'

                return Response({
                    'status': False,
                    'phone': old_user.phone,
                    'email': old_user.email,
                    'message': _("This email is already registered with us.")
                }, status=201)

            elif phone_already_exists:
                old_user = phone_already_exists
                old_user_phone_email = old_user.phone
                email_or_phone = 'phone'

                return Response({
                    'status': False,
                    'phone': old_user.phone,
                    'email': old_user.email,
                    'message': _("This phone is already registered with us.")
                }, status=201)
            
            
            
        else:
            serializer = RegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            user.set_password(password)
            user.save()

            if user.user_type == 'ngo':
                # save referal token for ngo
                NgoReferalToken.objects.create(user=user)

            if user.user_type == 'business' or user.user_type == 'ngo':
                user.is_approved = False
            else:
                user.is_approved = True

            user.save()
            
            random_code = get_random_code()
            Code.objects.create(user=user, confirmation_code=random_code)

            custom_message = _("Please use below OTP to verify your email.")
            send_email_status = send_otp_email(user.email,random_code, custom_message)

            if send_email_status:
                return Response({
                    'status': True,
                    'phone': user.phone,
                    'email': user.email,
                    'message': _('You are registered successfully. We have sent a code on your email address for verification.')
                }, status=201)    
            else:
                return Response({
                    "status": False,
                    "message": _("Something Went Wrong while sending OTP to {}, Please Try Again Later!".format(user.email))
                }, status=400)
            

def send_otp_email(user_email, otp, custom_message):
    subject = '[Shuk.tv] Verify your email'
    plaintext = get_template('emails/verify-email.txt')
    htmly     = get_template('emails/verify-email.html')
    d = { 'random_code': otp , 'custom_message': custom_message}
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    try:
        status = send_email(user_email, subject, text_content, html_content)
    except:
        status = False
    return status


class RegistrationPhoneOTPSendView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        phone = request.data.get('phone', None)
        change_phone = request.data.get('change_phone', None)

        if not phone:
            return Response({
                "status": False,
                "message": _("Phone is required.")
            })
        
        try:
            user = MyUser.objects.get(phone=phone)
        except:
            return Response({
                "status": False,
                "message":  _("This phone is not registered")
            })
        
        if phone == user.phone and user.is_phone_verified:

            if not user.is_approved:
                return Response({
                    'status': True,
                    'message': _("Your account is pending for approval from the backend team. Please wait until it's verified.")
                })

            token = get_tokens_for_user(user)
            return Response({
                "status": False,
                "token": token['access'],
                "refresh": token['refresh'],
                "message":_("This phone is already verified.Redirecting to landing page.")
            })
        
        if change_phone:
            phone = change_phone
            if (len(phone) < 10 or len(phone) > 17):
                return Response({
                    "status": False,
                    "message":_("Invalid New Phone.")
                })

            try:
                phone_already_exists = MyUser.objects.get(phone=phone)
            except:
                phone_already_exists = None
            
            if phone_already_exists:
                return Response({
                    "status": False,
                    "message":_("This phone already exist.")
                })
        
        status = send_otp_on_phone(phone)

        if status == 'error':
            return Response({
                'status': False,
                'message': _('Some error in sending sms.')
            })
        
        
        TempToken.objects.filter(user=user).delete()
        temp_code = TempToken(user=user)
        temp_code.save()
        
        return Response({
            'status': True,
            'tempToken': temp_code.token,
            'message': _('OTP sent to your phone {}. Please verify.'.format(phone))
        })


class RegistrationPhoneOTPVerifyView(APIView):

    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        otp = request.data.get('otp', None)
        phone = request.data.get('phone', None)
        change_phone = request.data.get('change_phone', None)
        
        if not otp or not phone:
            return Response({
                'status': False,
                'message': _('OTP and Phone is required'),
                'field': 'opt and phone'
            }, status=400)

        try:
            user = MyUser.objects.get(phone=phone)
        except:
            return Response({
                "status": False,
                "message": _("This phone is not registered")
            })
        
        if change_phone:
            phone = change_phone

        status = verify_otp_on_phone(phone,otp)

        if not status == 'approved':
            return Response({
                'status': False,
                'message': _('Not Valid Code or Expired, Request a New One'),
                'field': 'otp'
            }, status=400)
        
        TempToken.objects.filter(user=user).delete()
        temp_code = TempToken(user=user)
        temp_code.save()
        
        user.phone = phone
        user.is_phone_verified = True
        user.save()

        return Response({
            'status': True,
            'tempToken': temp_code.token,
            'message': _('Phone Verified Successfully.')
        })


class PhoneOTPSendView(APIView):

    def post(self, request):
        
        phone = request.data.get('phone', None)
        user = request.user

        if phone and phone == request.user.phone and request.user.is_phone_verified:
            return Response({
                "status": False,
                "message":_("This is your already registered and verified number. Enter a different number to update.")
            })

        # if phone number is to be updated
        if phone and phone != request.user.phone:

            if (len(phone) < 10 or len(phone) > 17):
                return Response({
                    "status": False,
                    "message":_("Invalid New Phone.")
                })

            try:
                phone_already_exists = MyUser.objects.get(phone=phone)
            except:
                phone_already_exists = None
            
            if phone_already_exists:
                return Response({
                    "status": False,
                    "message":_("This phone already exist.")
                })
            # else:
                # user.phone = phone
                # user.is_phone_verified = False
                # user.save()

        # send otp using twilio
        if phone:
            status = send_otp_on_phone(phone)
        else:
            status = send_otp_on_phone(user.phone)

        if status == 'error':
            return Response({
                'status': False,
                'message': _('Some error in sending sms.')
            })
        
        TempToken.objects.filter(user=user).delete()
        temp_code = TempToken(user=user)
        temp_code.save()
        
        return Response({
            'status': True,
            'tempToken': temp_code.token,
            'message': _('OTP sent to your phone. Please verify.')
        })


class PhoneOTPVerifyView(APIView):
    
    def post(self, request):
        otp = request.data.get('otp', None)
        phone = request.data.get('phone', None)
        
        if not otp or not phone:
            return Response({
                'status': False,
                'message': _('OTP and Phone is required'),
                'field': 'opt and phone'
            }, status=400)

        user = request.user

        status = verify_otp_on_phone(phone,otp)

        if not status == 'approved':
            return Response({
                'status': False,
                'message': _('Not Valid Code or Expired, Request a New One'),
                'field': 'otp'
            }, status=400)
        
        TempToken.objects.filter(user=user).delete()
        temp_code = TempToken(user=user)
        temp_code.save()
        
        user.phone = phone
        user.is_phone_verified = True
        user.save()

        token = get_tokens_for_user(user)

        return Response({
            'status': True,
            'tempToken': temp_code.token,
            "token": token['access'],
            "refresh": token['refresh'],
            'message': _('Phone Verified Successfully.')
        })


class OTPVerifyView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        otp = request.data.get('otp', None)
        email = request.data.get('email', None)
        if not otp or not email:
            return Response({
                'status': False,
                'message': _('OTP and Email is required'),
                'field': 'opt and email'
            }, status=400)

        try:
            user = MyUser.objects.get(email = email)
        except:
            return Response({
                'status': False,
                'message': _('Invalid Email'),
                'field': 'email'
            }, status=400)

        try:
            code = Code.objects.get(confirmation_code=otp, user = user, usage = 'Register')
        except Code.DoesNotExist:
            return Response({
                'status': False,
                'message': _('Not Valid Code or Expired, Request a New One'),
                'field': 'otp'
            }, status=400)
        
        TempToken.objects.filter(user=user).delete()
        temp_code = TempToken(user=user)
        temp_code.save()
        
        user.is_verified = True
        user.save()
        code.delete()

        # token = get_tokens_for_user(user)

        return Response({
            'status': True,
            'tempToken': temp_code.token,
            # "token": token['access'],
            # "refresh": token['refresh'],
            'message': _('Email verified successfully.')
        })


class LoginView(APIView):
    
    authentication_classes = []
    permission_classes = []

    def post(self, request):

        email_or_phone = request.data.get('email_or_phone', None).strip()
        user = None
        login_using = 'email'

        if email_or_phone:
            
            if is_valid_email(email_or_phone):
                try:
                    user = MyUser.objects.get(email=email_or_phone)
                except:
                    return Response({"status": False, "message": _("This email does not exists.")}, status=400)

            if not user and is_valid_phone(email_or_phone):
                login_using = 'phone'
                email_or_phone_with_plus = "+"+email_or_phone
                try:
                    user = MyUser.objects.get(Q(phone=email_or_phone)|Q(phone=email_or_phone_with_plus))
                except:
                    return Response({"status": False, "message": _("This phone does not exists.")}, status=400)

            if user:
                
                if not user.is_verified:
                    return Response({
                        "status": False, 
                        "message": _("Email is not verified."),
                        "goto":"email_verification",
                        'phone': user.phone,
                        'email': user.email,
                        'user_type': user.user_type
                    }, status=200)
            
                if not user.is_phone_verified:
                    return Response({
                        "status": False, 
                        "message": _("Phone is not verified."),
                        "goto":"phone_verification", 
                        'phone': user.phone,
                        'email': user.email,
                        'user_type': user.user_type
                    }, status=200)
                
                if (user.user_type == 'business' or user.user_type == 'member') and not user.plan:
                    
                    TempToken.objects.filter(user=user).delete()
                    temp_code = TempToken(user=user)
                    temp_code.save()
                    
                    return Response({
                        "status": False, 
                        "message": _("Please select plan to proceed."),
                        "goto":"plan", 
                        'tempToken': temp_code.token,
                        'phone': user.phone,
                        'email': user.email,
                        'user_type': user.user_type
                    }, status=200)

                if not user.is_approved:
                    return Response({"status": False, "message": _("Account not Approved by admin. Please contact administrator.")}, status=400)
                if not user.active:
                    return Response({"status": False, "message": _("Your account is deactivated by the admin. Please contact administrator.")}, status=400)
                if user.is_deleted:
                    return Response({"status": False, "message": _("Account is deleted. Please contact administrator.")}, status=400)
            else:
                return Response({"status": False, "message": _("Wrong Credentials!")}, status=400)
        else:
            return Response({
                "status": False,
                "message": _("Email/Phone is required"),
                "field": "email,phone"
            }, status=400)

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user.last_login = datetime.datetime.now()
        user.save()

        OnelineUser.objects.create(user=user)
        token = get_tokens_for_user(user)
        user_serializer = LoginUserDetailSerializer(user)

        resp_data = {
            "status": True,
            "token": token['access'],
            "refresh": token['refresh'],
            "user": user_serializer.data,
        }

        if not user.plan:
            TempToken.objects.filter(user=user).delete()
            temp_code = TempToken(user=user)
            temp_code.save()
            resp_data.update({
                'tempToken': temp_code.token
            })

        # Log Activity
        ActivityLog.objects.create(user=user)

        return Response(resp_data, status=200)


class LogoutView(APIView):

    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({
                "status": False,
                "message": _("refresh_token field is required!"),
                "field": "refresh_token"
            }, status=400)

        try:
            blacklist_token(refresh_token)
        except rest_framework_simplejwt.exceptions.TokenError:
            return Response({
                "status": False,
                "message": _("Token is invalid or expired"),
            }, status=400)

        except Exception as e:
            return Response({
                "status": False,
                "message": _("Token is invalid or expired"),
            }, status=400)

        request.user.last_login = timezone.now()
        request.user.save()

        online_users = OnelineUser.objects.filter(user=request.user)
        online_users.delete()

        # Log Activity
        ActivityLog.objects.create(user=request.user,type="logout")

        # delete all devices
        # UserDevice.objects.filter(user = request.user).delete()

        return Response({'status': True, 'Message': _('You have successfully logged out!')}, status=200)


class ForgotPasswordAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        email = request.data.get('email', None)
        if not email:
            return Response({"status": False, "message": _("Email is Required!"), "field": "email"}, status=400)
        try:
            user = MyUser.objects.get(email=email)
        except MyUser.DoesNotExist:
            return Response({"status": False, "message": _("No Account Found!")}, status=400)

        if not user.is_verified:
            return Response({"status": False, "message": _("User is Not Active, Activate your account first!")}, status=400)

        if Code.objects.filter(user=user).exists():
            Code.objects.get(user=user).delete()
            
        random_code = get_random_code()
        code = Code(user=user, confirmation_code=random_code, usage='Forgot')
        code.save()

        custom_message = "We've got a request from you to reset the password for your account. Please use below OTP to verify your email."
        send_email_status = send_otp_email(user.email,random_code,custom_message)

        if send_email_status:
            return Response({"status": True, "message": _("Check your email for confirmation Code!")})
        else:
            return Response({"status": False, "message": _("Something Went Wrong while sending OTP to {}, Please Try Again Later!".format(email))}, status=400)


class ForgotPasswordAPIViewNew(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        
        email_or_phone = request.data.get('email_or_phone', None)
        recovery_using = 'email'

        if not email_or_phone:
            return Response({"status": False, "message": _("Email/Phone is Required!"), "field": "email_or_phone"}, status=400)
        
        if is_valid_email(email_or_phone):
            try:
                user = MyUser.objects.get(email=email_or_phone)
            except:
                return Response({"status": False, "message": _("This email does not exists.")}, status=400)
        
        if not user and email_or_phone.isnumeric():
            recovery_using = 'phone'
            try:
                user = MyUser.objects.get(phone=email_or_phone)
            except:
                return Response({"status": False, "message": _("This phone does not exists.")}, status=400)
        
        if recovery_using == 'email' and not user.is_verified:
            return Response({"status": False, "message": _("Email is not verified, verify your email first!")}, status=400)
        
        if recovery_using == 'phone' and not user.is_phone_verified:
            return Response({"status": False, "message": _("Phone is not verified, verify your phone first!")}, status=400)
        
        if recovery_using == 'email':
            if Code.objects.filter(user=user).exists():
                Code.objects.get(user=user).delete()

            random_code = get_random_code()
            code = Code(user=user, confirmation_code=random_code, usage='Forgot')
            code.save()

            custom_message = "We've got a request from you to reset the password for your account. Please use below OTP to verify your email."
            send_email_status = send_otp_email(user.email,random_code,custom_message)
        
        if recovery_using == 'phone':
            send_otp_on_phone(email_or_phone,random_code)

        if send_email_status:
            return Response({"status": True, "message": _("Check your email for confirmation Code!")})
        else:
            return Response({"status": False, "message": _("Something Went Wrong while sending OTP to {}, Please Try Again Later!".format(email))}, status=400)


class ResendOtpAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        email = request.data.get('email', None)
        usage = request.data.get('usage', None)
        
        if not email:
            return Response({"status": False, "message": _("Email is Required!"), "field": "email"}, status=400)
        
        if not usage:
            return Response({"status": False, "message": _("Usage is Required. Register/Forgot"), "field": "usage"}, status=400)
        
        if usage not in dict(CODE_CHOICES):
            return Response({"status": False, "message": _("Invalid Usage"), "field": "usage"}, status=400)

        try:
            user = MyUser.objects.get(email=email)
        except MyUser.DoesNotExist:
            return Response({"status": False, "message": _("No Account Found!")}, status=400)

        
        if Code.objects.filter(user=user).exists():
            Code.objects.get(user=user).delete()
            
        random_code = get_random_code()
        code = Code(user=user, confirmation_code=random_code, usage=usage)
        code.save()

        custom_message = _("Please use below OTP to verify your account")
        send_email_status = send_otp_email(user.email,random_code, custom_message)

        if send_email_status:
            return Response({"status": True, "message": _("Check your email for confirmation Code!")})
        else:
            return Response({"status": False, "message": _("Something Went Wrong while sending OTP to {}, Please Try Again Later!".format(email))}, status=400)


class ResendOtpEmailUpdateAPIView(APIView):
    
    def post(self, request):
        
        new_email = request.data.get('new_email', None)
        usage = request.data.get('usage', None)
        
        if not new_email:
            return Response({"status": False, "message": _("New email is Required!"), "field": "new_email"}, status=400)
        
        if not usage:
            return Response({"status": False, "message": _("Usage is Required. Change Email"), "field": "usage"}, status=400)
        
        if usage not in dict(CODE_CHOICES) or usage != 'Change Email':
            return Response({"status": False, "message": _("Invalid Usage"), "field": "usage"}, status=400)
        
        try:
            email_already_exist = MyUser.objects.get(email=new_email)
        except:
            email_already_exist = None

        if email_already_exist:
            return Response({
                "status": False,
                "message":_("This email already exist.")
            })

        user = request.user
        
        if Code.objects.filter(user=user).exists():
            Code.objects.get(user=user).delete()
            
        random_code = get_random_code()
        code = Code(user=user, confirmation_code=random_code, usage=usage)
        code.save()

        custom_message = _("Please use below OTP to verify your account")
        send_email_status = send_otp_email(new_email,random_code, custom_message)

        if send_email_status:
            return Response({
                "status": True,
                'tempToken': reload_token(request.user), 
                "message": _("Check your email for confirmation Code!")
            })
        else:
            return Response({"status": False, "message": _("Something Went Wrong while sending OTP to {}, Please Try Again Later!".format(new_email))}, status=400)


class CodeVerificationAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        try:
            code = request.data.get('code', None)
            if not code:
                return Response({
                    "status": False,
                    "message": _("Code is Required!"),
                    "field": "code"
                }, status=400)

            email = request.data.get('email', None)
            if not email:
                return Response({
                    "status": False,
                    "message": _("Email is Required!"),
                    "field": "phone"
                }, status=400)

            try:
                user = MyUser.objects.get(email=email)
            except:
                return Response({"status": False, "message": _("Email not Found!")}, status=400)
            
            try:
                user_code = Code.objects.get(confirmation_code=code, user = user, usage = 'Forgot')
            except:
                return Response({"status": False, "message": _("Invalid Code")}, status=400)

            code_created_time = user_code.created_at
            
            if not check_expiration_code(code_created_time):
                user_code.delete()
                return Response({"status": False, "message": _("Code Expired, Request a New One!"), "field": "code"}, status=400)

            if user_code.usage == 'Register':

                token = get_tokens_for_user(user)

                user_code.user.is_verified = True
                user_code.user.save()
                user_code.delete()
                return Response({
                    "status": True, 
                    "token": token['access'],
                    "refresh": token['refresh'],
                    "message": _("Account has been verified successfully")
                })
            return Response({
                "status": True, 
                "code": code, 
                "email": user.email
            })
        except Code.DoesNotExist:
            return Response({"status": False, "message": _("Wrong Confirmation Code!"), "field": "code"}, status=400)


def check_expiration_code(time):
    code_created_time = time
    time_elapsed = datetime.datetime.now().timestamp() - code_created_time.timestamp()
    if time_elapsed > 1800:
        return False
    return True


class NewPasswordAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        
        code = request.data.get('code')
        email = request.data.get('email')

        if not code or not email:
            return Response({
                "status": False,
                "message": _("code and email is not there."),
                "field": "code,email"
            }, status=400)

        try:
            user = MyUser.objects.get(email=email)
        except:
            return Response({
                "status": False,
                "message": _("Email is Invalid."),
                "field": "code"
            }, status=400)

        try:
            user_code = Code.objects.get(user = user, usage = 'Forgot')
        except Code.DoesNotExist:
            return Response({
                "status": False,
                "message": _("Code Expired, Request a New One!"),
                "field": "code"
            }, status=400)

        if user_code.confirmation_code != code:
            return Response({
                "status": False,
                "message": _("Wrong confirmation code"),
                "field": "code"
            }, status=400)

        code_created_time = user_code.created_at

        if not check_expiration_code(code_created_time):
            user_code.delete()
            return Response({
                "status": False,
                "message": _("Code Expired, Request a New One!"),
                "field": "code"
            }, status=400)

        try:
            password = request.data['new_password']
            confirm_password = request.data['confirm_password']
        except Exception as e:
            return Response({
                "status": False,
                "message": _("Both Fields are required!"),
                "field": "new_password and confirm_password"
            }, status=400)

        if len(password) < 8:
            return Response({
                'status': False,
                'message': _('Password must be atleast 8 characters')
            }, status=400)

        if password != confirm_password:
            return Response({"status": False, "message": _("Passwords do not match")}, status=400)
        else:
            user = user_code.user
            user.set_password(password)
            user.save()
            user_code.delete()
            return Response({"status": True, "message": _("Password has been set!")})


class UpdatePasswordAPIView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        if not user.check_password(serializer.validated_data['current_password']):
            return Response({
                "status": False,
                "message": _("Wrong old Password"),
                "field": "current_password"
            }, status=400)

        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({"status": True, "message": _("Password has been successfully changed!")})


class CategoriesListView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        categories = BusinessCategory.objects.filter(parent=None)
        serializer = CategorySerializer(categories, many = True, context={"request": request})

        return Response({
            'status': True,
            'data': serializer.data
        })


class SubCategoriesListView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, category_id):
        categories = BusinessCategory.objects.filter(parent=category_id)
        serializer = CategorySerializer(categories, many = True, context={"request": request})

        return Response({
            'status': True,
            'data': serializer.data
        })


class UpdateProfileView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)
    
    def post(self, request):
        
        business_category = None
        if "business_category" in request.data:
            try:
                business_category = BusinessCategory.objects.get(id = request.data["business_category"])
            except:
                return Response({
                    'status': False,
                    'message': _("Invalid business category")
                })

        # business category cannot be updated
        if business_category and request.user.business_category != None and request.user.business_category.keyword != business_category.keyword:
            
            return Response({
                'status': False,
                'message': _("Your business category is already set to '{}'. You cannot change it.").format(request.user.business_category.name)
            })



        serializer = UpdateProfileSerializer(request.user, data = request.data, context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            # location handle start
            primary_location = None
            if "location" in request.data:
                try:
                    primary_location = UserLocation.objects.get(user = request.user, is_primary = True)
                except:
                    # add the location
                    location_serializer = LocationSerializer(data = request.data, context={"request": request})
                    if location_serializer.is_valid(raise_exception = True):
                        newly_added_location = location_serializer.save()
                        UserLocation.objects.create(location = newly_added_location, user=request.user, is_primary=True)
                        request.user.extra_location -= 1
                        request.user.save()
                
                if primary_location:
                    # update the existing primary location
                    location = primary_location.location
                    location_serializer = LocationUpdateSerializer(location, data = request.data, context={"request": request})
                    if location_serializer.is_valid(raise_exception = True):
                        location_serializer.save()
            # location handle end

            # business category restaurant start
            if request.user.business_category and request.user.business_category.keyword == 'restaurant':
                
                # handle menu and delivery partners start
                if "menu" in request.data and request.data["menu"]:
                    menu = None
                    try:
                        menu = RestaurantMenu.objects.get(user = request.user)
                    except:
                        menu_serializer = MenuSerializer(data=request.data, context={'request': request})
                        if menu_serializer.is_valid(raise_exception = True):
                            menu_serializer.save()

                    if menu:
                        menu_serializer = MenuUpdateSerializer(menu, data=request.data, context={'request', request})
                        if menu_serializer.is_valid(raise_exception = True):
                            menu_serializer.save()
                
                if "delivery_partner" in request.data:
                    delivery_partners = request.POST.getlist('delivery_partner')
                    for dp in delivery_partners:
                        request.user.delivery_partner.add(dp)
                    
            # business category restaurant end

            return Response({
                "status": True, 
                "data": serializer.data,
                "message": _("Profile Updated Successfully")
            })
        else:
            return Response({
                "status": False, 
                "message": _("Some error")
            })
        

class RelationsListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)
    
    def get(self, requests):
        
        relations = []

        for key,value in FAMILY_RELATIONS:
            relations.append(
                {
                "key": key,
                "relation":value
                }
            )

        return Response({
            'status': True,
            'data': relations
        })


def send_password_email(family_member, password):
    print("password in email",password)
    subject = '[Shuk.tv] Family Member Details'
    plaintext = get_template('emails/family-member-password.txt')
    htmly     = get_template('emails/family-member-password.html')
    d = { 'password': password, 'family_member': family_member }
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    print(html_content)
    try:
        status = send_email(family_member.email, subject, text_content, html_content)
    except:
        status = False
    return status


def send_password_email_to_store(store, password):
    print("password in email",password)
    subject = '[Shuk.tv] Store Details'
    plaintext = get_template('emails/store-password.txt')
    htmly     = get_template('emails/store-password.html')
    d = { 'password': password, 'store': store }
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    print(html_content)
    try:
        status = send_email(store.email, subject, text_content, html_content)
    except:
        status = False
    return status


class FamilyMemberView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)
    
    def post(self,request):

        if request.user.parent:
            return Response({
                "status": False,
                "message":_("You cannot create family member")
            })

        try:
            member_already_exists = MyUser.objects.get(parent = request.user.id)
        except:
            serializer = FamilyMemberCreateSerializer(data = request.data, context={"request": request})
            if serializer.is_valid(raise_exception=True):
                
                family_member = serializer.save()
                
                # create password and send in email
                random_password = random_string(12)
                print('random_password',random_password)
                family_member.set_password(random_password)
                
                family_member.language = family_member.parent.language
                family_member.currency = family_member.parent.currency
                family_member.cover_pic = family_member.parent.cover_pic
                family_member.administrator_name = family_member.parent.administrator_name
                family_member.country = family_member.parent.country
                
                family_member.plan = family_member.parent.plan
                family_member.user_type = family_member.parent.user_type
                family_member.ngo = family_member.parent.ngo
                
                family_member.is_approved = True
                family_member.is_verified = True
                family_member.is_phone_verified = True
                family_member.save()

                send_password_email(family_member, random_password)

                return Response({
                    "status": True, 
                    "data": serializer.data,
                    "message": _("Family Member Added Successfully")
                })
        
        serializer = FamilyMemberSerializer(member_already_exists, data = request.data, context={"request": request})
        if serializer.is_valid(raise_exception=True):
                family_member = serializer.save()
                family_member.update_at = timezone.now()
                return Response({
                    "status": True, 
                    "data": serializer.data,
                    "message": _("Family Member Updated Successfully")
                })
        

class DeleteFamilyMemberView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)
    
    def get(self,request):

        # family member can be deleted only after the billing cycle is over


        try:
            family_member = MyUser.objects.get(parent = request.user)
        except:
            return Response({
                    'status': False,
                    'message': _("Invalid Family Member")
                })
        
        family_member.parent = None
        family_member.plan_id = 1
        family_member.save()
        
        return Response({
            "status": True, 
            "message": _("Family Member deleted Successfully")
        })


class DeleteAccountReasonView(APIView):

    def get(self, request):

        dict_choices = {k: _(v) for k,v in USER_DELETE_REASONS}
        return Response({
            "status": True,
            "data": dict_choices
        })


class DeleteAccountView(APIView):
    
    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request):

        if request.user.is_deleted:
            return Response({
                "status": False,
                "message":  _("User is already deleted"),
            })

        if "delete_reason" not in request.data:
            return Response({
                "status": False,
                "field": "delete_reason",
                "message":  _("Please send delete reason"),
            })

        delete_reason = request.data["delete_reason"]

        if delete_reason not in dict(USER_DELETE_REASONS):
            return Response({
                "status": False,
                "field": "delete_reason",
                "message":  _("Invalid Reason"),
            })
        
        if request.user.user_type == 'ngo':
            
            if request.user.is_default_ngo:
                return Response({
                    "status": False,
                    "message":  _("You cannot delete your account for the moment as it is used as default Non Profitable Organization. Please contact admin for deleting your account."),
                })
        
            if not allocate_members_and_businesses_to_default_ngo(request.user):
                return Response({
                    "status": False,
                    "message":  _("You cannot delete your account at the moment. Please contact admin."),
                })
        
        request.user.is_deleted = True
        request.user.delete_reason = request.data["delete_reason"]
        request.user.save()

        randomize_all_user_data(request.user)

        return Response({
            "status": True,
            "message":  _("Account deleted Successfully.")
        })


class NgoListView(APIView):

    authentication_classes = []
    permission_classes = []
    
    def get(self, requests):
        ngos = active_ngos().filter(user_type='ngo')
        serializer = NgosSerializer(ngos, many = True)

        return Response({
            'status': True,
            'data': serializer.data
        })
    

class CountryListView(APIView):

    authentication_classes = []
    permission_classes = []
    
    def get(self, requests):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many = True)

        return Response({
            'status': True,
            'data': serializer.data
        })
    

class LanguageListView(APIView):

    authentication_classes = []
    permission_classes = []
    
    def get(self, requests):
        
        languages = []

        for key,value in LANGUAGES_ALLOWED:
            languages.append(
                {
                "key": key,
                "name":value,
                "flag": get_map_for_language(key)
                }
            )

        return Response({
            'status': True,
            'data': languages
        })

    
class CurrencyListView(APIView):

    authentication_classes = []
    permission_classes = []
    
    def get(self, requests):
        
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)

        return Response({
            'status': True,
            'data': serializer.data
        })


class PlanListView(APIView):

    authentication_classes = []
    permission_classes = []
    
    def get(self, requests):
        user_type = self.request.GET.get('user_type')
        to_currency = self.request.GET.get('to_currency')
        plans = Plan.objects.filter(user_type=user_type)
        serializer = PlanSerializer(plans, many = True, context = {'to_currency': to_currency})

        return Response({
            'status': True,
            'data': serializer.data
        })


def get_user_from_token(token):
    try:
        temp_token = TempToken.objects.get(token=token)
    except:
        return None
    
    return temp_token.user

            

class PlanActivateNewView(APIView):

    permission_classes = (AllowAny,)
    
    def post(self, request):
        
        plan = request.data.get('plan', None)
        
        if not plan:
            return Response({
                'status': False,
                'message': _('Plan is required')
            }, status=400)

        
        user = request.user

        if not user or user.is_anonymous:
            if "tempToken" not in request.data:
                return Response({
                    "status": False,
                    "message":  _("You cannot access this module.")
                })
            user = get_user_from_token(request.data["tempToken"])

        
        if not user or user.is_anonymous:
            return Response({
                "status": False,
                "message": _("You cannot access this module")
            })
            
        
        try:
            valid_plan = Plan.objects.get(id=plan)
        except Plan.DoesNotExist:
            return Response({
                'status': False,
                'message': _('Invalid Plan'),
                'field': 'plan'
            })
        
        if valid_plan.user_type != user.user_type:
            return Response({
                'status': False,
                'message': _('This plan is not for current user type'),
                'field': 'plan'
            })
        
        if valid_plan.amount == 0:
            user.plan = valid_plan
            user.save()

            if user.user_type == 'business':
                try:
                    plan_feature = PlanFeature.objects.get(plan=valid_plan, feature_type='location')
                except:
                    pass
                if plan_feature:
                    user.extra_location = plan_feature.numbers_allowed
                    user.save()

            return Response({
                'status': True,
                'message': _("Plan activated successfully")
            })
        
        payment_detail = create_plan_payment(valid_plan, user)
    
        return Response({
            'status': True,
            'goto': "payment",
            'payment_detail': payment_detail.id
        })
    

class GenerateStripeIntentView(APIView):

    permission_classes = (AllowAny,)

    def post(self,request):

        payment_detail = request.data.get('payment_detail', None)
        
        user = request.user

        if not user or user.is_anonymous:
            if "tempToken" not in request.data:
                return Response({
                    "status": False,
                    "message":  _("You cannot access this module.")
                })
            user = get_user_from_token(request.data["tempToken"])

        
        if not user or user.is_anonymous:
            return Response({
                "status": False,
                "message": _("You cannot access this module")
            })
        
        if not payment_detail:
            return Response({
                'status': False,
                'message': _('Payment Detail is missing'),
                'field': 'payment_detail'
            }, status=400)

        try:
            payment_detail = PaymentDetail.objects.get(id=payment_detail)
        except:
            return Response({
                'status': False,
                'message': _('Payment Detail is Invalid')
            }, status=400)
        
        amount = payment_detail.amount
        

        resp = stripe_payment_intent(user, amount)

        if resp:

            stripe_client_secret = resp.client_secret

            # create a row in table stripe details to store the payment details
            StripeDetailNew.objects.create(
                user = user,
                intent = resp.id,
                payment_detail = payment_detail
            )

            return Response({
                'status': True,
                'stripe_client_secret': stripe_client_secret,
            })
        else:
            return Response({
                'status': False,
                'message':  _("Payment gateway issue in stripe")
            })
        

class GetTranzilaTokenView(APIView):

    permission_classes = (AllowAny,)

    def get(self,request):

        user = request.user

        if not user or user.is_anonymous:
            if "tempToken" not in request.data:
                return Response({
                    "status": False,
                    "message":  _("You cannot access this module.")
                })
            user = get_user_from_token(request.data["tempToken"])

        
        if not user or user.is_anonymous:
            return Response({
                "status": False,
                "message": _("You cannot access this module")
            })

        tranzila_tokens = TranzilaToken.objects.filter(user=user)
        serializer = TranzilaTokenSerializer(tranzila_tokens, many=True)

        return Response({
            "status": True,
            "data": serializer.data
        })


class GetStripePaymentMethodView(APIView):

    permission_classes = (AllowAny,)

    def get(self,request):

        user = request.user

        if not user or user.is_anonymous:
            if "tempToken" not in request.data:
                return Response({
                    "status": False,
                    "message":  _("You cannot access this module.")
                })
            user = get_user_from_token(request.data["tempToken"])

        
        if not user or user.is_anonymous:
            return Response({
                "status": False,
                "message": _("You cannot access this module")
            })

        stripe_details = StripeDetailNew.objects.filter(user=user, status='complete').values('card_mask','payment_method','expire_month','expire_year').distinct()
        serializer = StripeDetailSerializer(stripe_details, many=True)

        return Response({
            "status": True,
            "data": serializer.data
        })


class ListStripePaymentMethodView(APIView):

    permission_classes = (AllowAny,)

    def get(self,request):

        user = request.user

        if not user or user.is_anonymous:
            if "tempToken" not in request.data:
                return Response({
                    "status": False,
                    "message":  _("You cannot access this module.")
                })
            user = get_user_from_token(request.data["tempToken"])

        
        if not user or user.is_anonymous:
            return Response({
                "status": False,
                "message": _("You cannot access this module")
            })

        stripe_payment_methods = get_stripe_payment_methods(user)
        
        payment_methods = []
        for pm in stripe_payment_methods.data:
            card = pm.card
            pm_data = {
                "id": pm.id,
                "last4": card.last4,
                "exp_month": card.exp_month,
                "exp_year": card.exp_year
            }
            payment_methods.append(pm_data)

        return Response({
            "status": True,
            "data": payment_methods
        })


class ListStripePaymentMethodBakView(APIView):

    permission_classes = (AllowAny,)

    def get(self,request):

        user = request.user

        if not user or user.is_anonymous:
            if "tempToken" not in request.data:
                return Response({
                    "status": False,
                    "message":  _("You cannot access this module.")
                })
            user = get_user_from_token(request.data["tempToken"])

        
        if not user or user.is_anonymous:
            return Response({
                "status": False,
                "message": _("You cannot access this module")
            })

        stripe_payment_methods = StripePaymentMethod.objects.filter(user=user)
        serializer = StripePaymentMethodSerializer(stripe_payment_methods, many=True)

        return Response({
            "status": True,
            "data": serializer.data
        })
    

class MarkDefaultStripePaymentMethodView(APIView):

    permission_classes = (AllowAny,)

    def post(self,request):

        if "payment_method" not in request.data:
            return Response({
                "status": False,
                "message":  _("Payment method is required.")
            })
        
        payment_method = request.data.get("payment_method")

        try:
            stripe_payment_method = StripePaymentMethod.objects.get(payment_method=payment_method, user=request.user)
        except:
            return Response({
                "status": False,
                "message":  _("Invalid payment method.")
            })

        for pm in request.user.stripe_payment_methods.all():
            pm.is_default = False
            pm.save()

        stripe_payment_method.is_default = True
        stripe_payment_method.save()

        return Response({
            "status": True,
            "message":  _("This payment method is marked default successfully.")
        })


class DeleteStripePaymentMethodView(APIView):

    def post(self, request):

        if "payment_method" not in request.data:
            return Response({
                "status": False,
                "message":  _("Please send payment method to delete"),
                "field": "payment_method"
            })
        
        payment_method = request.data.get("payment_method")
        
        try:
            detach_payment_method(payment_method)
        except:
            pass

        return Response({
            "status": True,
            "message":  _("Payment method deleted successfully.")
        })


class CreateCheckoutSessionView(APIView):

    def get(self,request):

        user = request.user
        resp = create_checkout_session(user)

        return Response({
            "status": True,
            "data": resp
        })


class AddStripePaymentMethodView(APIView):

    def post(self,request):

        if "CHECKOUT_SESSION_ID" not in request.data:
            return Response({
                "status": False,
                "message":  _("Checkout session id is missing"),
                "field": "CHECKOUT_SESSION_ID"
            })

        CHECKOUT_SESSION_ID = request.data.get("CHECKOUT_SESSION_ID")

        retrieve_checkout_session(request.user, CHECKOUT_SESSION_ID)

        return Response({
            "status": True,
            "message":   _("Payment method added successfully")
        }) 


class GetAccessFromTempToken(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):

        if "tempToken" not in request.data:
            return Response({
                "status": False,
                "field": "tempToken",
                "message":  _("Please send temp token")
            })
        
        user = get_user_from_token(request.data["tempToken"])

        
        if not user or user.is_anonymous:
            return Response({
                "status": False,
                "message": _("You cannot access this module")
            })
        
        # TempToken.objects.filter(user=user).delete()
        
        if not user.is_approved:

            return Response({
                "status": False,
                "message":  _("Your account is pending for approval from the backend team. Please wait until it's verified.")
            })
        
        token = get_tokens_for_user(user)
        user_serializer = LoginUserDetailSerializer(user)

        resp_data = {
            "status": True,
            "token": token['access'],
            "refresh": token['refresh'],
            "user": user_serializer.data,
        }

        ActivityLog.objects.create(user=user)

        return Response(resp_data, status=200)


class GetBasicInfoFromTempToken(APIView):
    
    permission_classes = (AllowAny,)

    def post(self, request):

        user = request.user

        if not user or user.is_anonymous:
            if "tempToken" not in request.data:
                return Response({
                    "status": False,
                    "message":  _("You cannot access this module.")
                })
            user = get_user_from_token(request.data["tempToken"])

        
        if not user or user.is_anonymous:
            return Response({
                "status": False,
                "message": _("You cannot access this module")
            })

        resp_data = {
            "status": True,
            "currency": user.currency.id,
            "currency_iso": user.currency.iso_code,
            "language": user.language,
        }

        ActivityLog.objects.create(user=user)

        return Response(resp_data, status=200)

        
class TranzilaPaymentView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):

        user = request.user

        if not user or user.is_anonymous:
            if "tempToken" not in request.data:
                return Response({
                    "status": False,
                    "message":  _("You cannot access this module.")
                })
            user = get_user_from_token(request.data["tempToken"])

        
        if not user or user.is_anonymous:
            return Response({
                "status": False,
                "message": _("You cannot access this module")
            })

        if "payment_detail" not in request.data:
            return Response({
                "status": False,
                "message": _("Please send payment detail"),
                "field": "payment_detail"
            })
        
        payment_detail = request.data["payment_detail"]

        try:
            payment_detail = PaymentDetail.objects.get(id=payment_detail)
        except:
            return Response({
                "status": False,
                "message": _("Invalid payment details")
            })

    
        if "tranzila_token" in request.data:
            try:
                tranzila_token = TranzilaToken.objects.get(token=request.data.get("tranzila_token"), user=user)
            except:
                tranzila_token  = None
            
            if tranzila_token:
                try:
                    payment_status = process_tranzila_payment(tranzila_token,payment_detail)
                except:
                    return Response({
                        "status": False,
                        "message": _("Some problem in payment")
                    })
                if payment_status['code'] == 1:
                    handle_payment_intent_succeeded_new(payment_detail)
                if payment_status:
                    return Response({
                        "status": payment_status['code'],
                        "message":payment_status['message']
                    })
                else:
                    return Response({
                        "status": False,
                        "message":_("Payment Failed")
                    })
            else:
                return Response({
                    "status": False,
                    "message":_("Invalid Token")
                })
        
    

        if user.currency.iso_code != 'ils':
            return Response({
                "status": False,
                "message":_("For using tranzila, make sure your currency is Israeli Shekels")
            })

        if "card_number" not in request.data:
            return Response({
                "status": False,
                "message": _("Please enter card number"),
                "field": "card_number"
            })
        
        if "expire_month" not in request.data:
            return Response({
                "status": False,
                "message": _("Please enter expiry month"),
                "field": "expire_month"
            })
        
        if "expire_year" not in request.data:
            return Response({
                "status": False,
                "message": _("Please enter expiry year"),
                "field": "expire_year"
            })
        
        

        card_number = request.data["card_number"]
        expire_month = request.data["expire_month"]
        expire_year = request.data["expire_year"]

        try:
            already_exist = TranzilaToken.objects.get(card_mask__icontains=card_number[-1:], expire_month=expire_month, expire_year = expire_year)
        except:
            already_exist = None

        if already_exist:
            return Response({
                "status": False,
                "message":  _("This card already exist.")
            })

        try:
            payment_status = process_tranzila_payment("",payment_detail,card_number,expire_month,expire_year)
        except:
            return Response({
                "status": False,
                "message": _("Some problem in payment")
            })

        if payment_status:
            if payment_status['code'] == 1:
                handle_payment_intent_succeeded_new(payment_detail)
            return Response({
                "status": payment_status['code'],
                "message":payment_status['message']
            })
        else:
            return Response({
                "status": False,
                "message":_("Payment Failed")
            })


class AddTranzilaPaymentMethodView(APIView):

    def post(self, request):

        user = request.user

        if user.currency.iso_code != 'ils':
            return Response({
                "status": False,
                "message":_("For using tranzila, make sure your currency is Israeli Shekels")
            })

        if "card_number" not in request.data:
            return Response({
                "status": False,
                "message": _("Please enter card number"),
                "field": "card_number"
            })
        
        if "expire_month" not in request.data:
            return Response({
                "status": False,
                "message": _("Please enter expiry month"),
                "field": "expire_month"
            })
        
        if "expire_year" not in request.data:
            return Response({
                "status": False,
                "message": _("Please enter expiry year"),
                "field": "expire_year"
            })

        card_number = request.data["card_number"]
        expire_month = request.data["expire_month"]
        expire_year = request.data["expire_year"]

        try:
            already_exist = TranzilaToken.objects.get(card_mask__icontains=card_number[-1:], expire_month=expire_month, expire_year = expire_year)
        except:
            already_exist = None

        if already_exist:
            return Response({
                "status": False,
                "message":  _("This card already exist.")
            })

        payment_detail = PaymentDetail.objects.create(
            user = request.user,
            item_type = 'new_payment_method',
            main_amount_in_usd = 0.27, # 1 ils = 0.27 dollars
            amount = 1,
            locations_to_activate = 0,
            currency = request.user.currency.iso_code
        )
        
        try:
            payment_status = process_tranzila_payment("",payment_detail,card_number,expire_month,expire_year)
        except:
            return Response({
                "status": False,
                "message": _("Some problem in payment")
            })

        if payment_status:
            if payment_status['code'] == 1:
                handle_payment_intent_succeeded_new(payment_detail)
            return Response({
                "status": payment_status['code'],
                "message":payment_status['payment_method_message']
            })
        else:
            return Response({
                "status": False,
                "message": _("Some problem in adding the new payment method.")
            })


class MarkDefaultTranzilaPaymentMethodView(APIView):

    permission_classes = (AllowAny,)

    def get(self,request, payment_method_id):

        try:
            tranzila_payment_method = TranzilaToken.objects.get(id=payment_method_id, user=request.user)
        except:
            return Response({
                "status": False,
                "message":  _("Invalid payment method.")
            })

        for pm in request.user.tranzila_tokens.all():
            pm.is_default = False
            pm.save()

        tranzila_payment_method.is_default = True
        tranzila_payment_method.save()

        return Response({
            "status": True,
            "message":  _("This payment method is marked default successfully.")
        })


class DeleteTranzilaPaymentMethodView(APIView):

    def get(self, request, payment_method_id):

        try:
            payment_method = TranzilaToken.objects.get(id=payment_method_id, user=request.user)
        except:
            return Response({
                "status": False,
                "message":  _("This payment method does not exist")
            })

        payment_method.delete()

        return Response({
            "status": True,
            "message":  _("Payment method deleted successfully.")
        })


class StripePaymentView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):

        user = request.user

        if not user or user.is_anonymous:
            if "tempToken" not in request.data:
                return Response({
                    "status": False,
                    "message":  _("You cannot access this module.")
                })
            user = get_user_from_token(request.data["tempToken"])

        
        if not user or user.is_anonymous:
            return Response({
                "status": False,
                "message": _("You cannot access this module")
            })

        if "payment_detail" not in request.data:
            return Response({
                "status": False,
                "message": _("Please send payment detail"),
                "field": "payment_detail"
            })
        
        payment_detail = request.data["payment_detail"]

        try:
            payment_detail = PaymentDetail.objects.get(id=payment_detail)
        except:
            return Response({
                "status": False,
                "message": _("Invalid payment details")
            })
    
        if "payment_method" in request.data:
            
                
            payment_method=request.data.get("payment_method")
            resp = stripe_payment_offsession(user=user,amount=payment_detail.amount,payment_method=payment_method)
            
            if not resp:
                return Response({
                    "status": False,
                    "message":_("Payment Failed")
                })
            
            logger.info("....stripe resp....")
            logger.info(resp)
            
            charges_detail = resp
            if charges_detail["status"] == "succeeded":

                StripeDetailNew.objects.create(
                    user = user,
                    payment_detail = payment_detail,
                    intent = charges_detail["id"],
                    payment_method = charges_detail["payment_method"],
                    amount = charges_detail["amount"],
                    currency = charges_detail["currency"],
                    status = "pending",
                    description = charges_detail["description"]
                )

                payment_detail.status = 'pending'
                payment_detail.save()

                # handle_payment_intent_succeeded_new(payment_detail)
                print("....stripe success....")

                return Response({
                    "status": True,
                    "payment_detail": payment_detail.id,
                    "message":_("Payment Successful")
                })

        else:

            payment_detail.status = "cancelled"
            payment_detail.save()
            print("....stripe failed....")

            return Response({
                "status": False,
                "message":_("Invalid payment method")
            })


class PaymentDetailStatusView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, payment_detail):

        user = request.user

        if not user or user.is_anonymous:
            if "tempToken" not in request.data:
                return Response({
                    "status": False,
                    "message":  _("You cannot access this module.")
                })
            user = get_user_from_token(request.data["tempToken"])

        
        if not user or user.is_anonymous:
            return Response({
                "status": False,
                "message": _("You cannot access this module")
            })

        try:
            payment_detail = PaymentDetail.objects.get(id=payment_detail)
        except:
            return Response({
                "status": False,
                "message": _("Invalid payment details")
            })
        
        if payment_detail.status == 'complete':
            return Response({
                "status": True,
                "message":  _("Payment successfully.")
            })
        elif payment_detail.status == 'cancelled':
            return Response({
                "status": False,
                "message":  _("Payment Cancelled.")
            })
        elif payment_detail.status == 'pending':
            return Response({
                "status": False,
                "message":  _("Payment in process.")
            })



class StripeWebhookNewView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        stripe.api_key = settings.STRIPE_API_KEY
        event = None
        stripe_detail = None
        event_type = None
        payment_detail = None
        try:
            payload = request.body
            event = json.loads(payload)
        except stripe.error.SignatureVerificationError as e:
            logger.info('⚠️  Webhook signature verification failed.' + str(e))
            return JsonResponse({"success": False})

        if event:
            event_type = event['type']
            logger.info("event", event)
            payment_detail = event['data']['object']
            logger.info("payment_detail['id']")
            logger.info(payment_detail["id"])
            try:
                stripe_detail = StripeDetailNew.objects.get(intent=payment_detail["id"])
            except:
                logger.info("Stripe detail via intent on webhook not found")
                return JsonResponse({"success": False})

            stripe_detail.event_type = event_type
            stripe_detail.payment_method = payment_detail["id"]
            stripe_detail.description = payment_detail["description"]
            stripe_detail.amount = payment_detail["amount"]
            stripe_detail.currency = payment_detail["currency"]
            stripe_detail.save()

        if event_type == 'payment_intent.succeeded':
            logger.info('Payment for {} succeeded'.format(payment_detail['amount']))

            stripe_detail.status = "complete"
            stripe_detail.save()

            stripe_detail.payment_detail.status = 'complete'
            stripe_detail.payment_detail.save()

            handle_payment_intent_succeeded_new(stripe_detail.payment_detail)

        elif event_type == 'payment_intent.payment_failed':

            stripe_detail.status = "cancelled"
            stripe_detail.cancellation_reason = payment_detail["cancellation_reason"]
            stripe_detail.save()

            stripe_detail.payment_detail.status = 'cancelled'
            stripe_detail.payment_detail.save()

        return JsonResponse({"success": True})


class LocationAddView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)
    
    def post(self, request):

        if "locations" not in request.data:
            return Response({
                'status': False,
                'message': _("Please send location to add")
            })

        # check if the user's limit has not reached based on plan

        multiple_locations = request.data["locations"]
        
        locations_count_to_add = int(len(multiple_locations))
        product_price = ProductPrice.objects.get(product_name = 'SINGLE_LOCATION_COST')
        main_amount_in_usd = (float(product_price.cost) * locations_count_to_add)
        
        
        if len(multiple_locations) > request.user.extra_location and main_amount_in_usd > 0:
            return Response({
                'status': False,
                'go_to': 'payment',
                'message': _('Please make payments for adding more locations.')
            })
        
        for location in request.data["locations"]:
            serializer = StoreLocationSerializer(data = location, context={"request": request})
            serializer.is_valid(raise_exception = True)
        
        for location in request.data["locations"]:
            serializer = StoreLocationSerializer(data = location, context={"request": request})
            serializer.is_valid(raise_exception = True)
            location_obj = serializer.save()
            

            store = MyUser.objects.create(
                email = location_obj.store_manager_email,
                phone = location_obj.store_manager_phone,
                parent = request.user,
                is_store = True
            )

            # create password and send in email
            random_password = random_string(12)
            print('random_password',random_password)
            store.set_password(random_password)
            
            store.language = store.parent.language
            store.currency = store.parent.currency
            store.cover_pic = store.parent.cover_pic
            store.administrator_name = store.parent.administrator_name
            store.country = store.parent.country
            
            store.plan = store.parent.plan
            store.user_type = store.parent.user_type
            store.ngo = store.parent.ngo
            
            store.firstname = store.parent.firstname
            store.lastname  = store.parent.lastname
            store.name  = store.parent.name
            store.about  = store.parent.about
            store.business_category  = store.parent.business_category
            store.website_url  = store.parent.website_url
            store.facebook_url  = store.parent.facebook_url
            store.twitter_url  = store.parent.twitter_url
            store.instagram_url  = store.parent.instagram_url
            store.youtube_url  = store.parent.youtube_url
            store.image  = store.parent.image
            store.cover_pic  = store.parent.cover_pic
            store.user_type_category  = store.parent.user_type_category
            store.service_provider_type  = store.parent.service_provider_type
            store.reservation_walkin  = store.parent.reservation_walkin
            
            store.is_approved = True
            store.is_verified = True
            store.is_phone_verified = True
            store.save()

            send_password_email_to_store(store, random_password)

            # associate location with parent user
            UserLocation.objects.create(user=request.user, location = location_obj)

            # associate location with store user
            UserLocation.objects.create(user=store, location = location_obj, is_primary = True)

            if request.user.extra_location > 0:
                request.user.extra_location -= 1
                request.user.save()

        location_ids = [user_location.location_id for user_location in request.user.user_locations.all()]

        all_locations = Location.objects.filter(id__in = location_ids).order_by('-id')
        serializer = LocationSerializer(all_locations, many=True)
            
        return Response({
            'status': True,
            'data': serializer.data
        })
    

class LocationUpdateView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)
    
    def post(self, request, location_id):

        try:
            user_location = UserLocation.objects.get(location_id = location_id, user = request.user)
        except:
            return Response({
                'status': False,
                'message': _('This location does not exist.'),
            }, status=400)

        location = Location.objects.get(id=user_location.location_id)
        
        if "store_manager_email" in request.data:
            
            store_manager_email = request.data["store_manager_email"]
            
            try:
                email_already_exist = MyUser.objects.get(email=request.data["store_manager_email"])
            except:
                email_already_exist = None

            if email_already_exist and location.store_manager_email != store_manager_email:
                return Response({
                    'status': False,
                    'message': _('This store manager email already exist.'),
                }, status=400)

        if "store_manager_phone" in request.data:
            
            store_manager_phone = request.data["store_manager_phone"]
            
            try:
                phone_already_exist = MyUser.objects.get(phone=request.data["store_manager_phone"])
            except:
                phone_already_exist = None

            if phone_already_exist and location.store_manager_phone != store_manager_phone:
                return Response({
                    'status': False,
                    'message': _('This store manager phone already exist.'),
                }, status=400)
        
        
        serializer = LocationUpdateSerializer(location, data = request.data, context={"request": request})
        serializer.is_valid(raise_exception = True)
        location = serializer.save()

        try:
            store_location = UserLocation.objects.get(location=location, is_primary=True)
        except:
            store_location = None

        print("store_location_id",store_location.id)

        if store_location:
            store = store_location.user
            print("store",store)
            if store.email != location.store_manager_email:
                store.email = location.store_manager_email
            if store.phone != location.store_manager_phone:
                store.phone = location.store_manager_phone
            store.save()
            
        return Response({
            'status': True,
            'data': serializer.data
        })


class LocationPaymentView(APIView):

    def post(self, request):

        if "locations_count" not in request.data:
            return Response({
                'status': False,
                'message': _("Please send number of location to add")
            })
        
        locations_count_to_add = int(request.data.get("locations_count"))
        product_price = ProductPrice.objects.get(product_name = 'SINGLE_LOCATION_COST')
        main_amount_in_usd = (float(product_price.cost) * locations_count_to_add)
        total_price_for_locations = main_amount_in_usd + int(settings.SHUKTV_TAX_COST)

        currency = 'usd'
        amount = total_price_for_locations
        if request.user.currency.iso_code != 'usd':
            currency = request.user.currency.iso_code
            amount = __(amount, 'usd', currency)

        # create a row in table payment details to store the payment details
        payment_detail = PaymentDetail.objects.create(
            user = request.user,
            item_type = 'location',
            main_amount_in_usd = main_amount_in_usd,
            amount = amount,
            locations_to_activate = locations_count_to_add,
            currency = currency
        )

        return Response({
            'status': True,
            'go_to': 'payment',
            'payment_detail': payment_detail.id
        })
    

class LocationListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)
    
    def get(self, request):

        items_per_page = self.request.GET.get('items_per_page')
        pagination_on = self.request.GET.get('pagination_on')
        
        user_locations = UserLocation.objects.filter(user=request.user).order_by("-id")
        location_ids = [user_location.location_id for user_location in user_locations]
        locations = Location.objects.filter(id__in = location_ids)

        # search start
        search_key = self.request.GET.get('search_key')
        if search_key:
            locations = locations.filter(
                Q(location__icontains = search_key)| 
                Q(address__icontains = search_key) | 
                Q(city__icontains = search_key) | 
                Q(state__icontains = search_key) | 
                Q(country__icontains = search_key) | 
                Q(zipcode__icontains = search_key)
            )
        # search end

        if pagination_on:
            return paginated_data(locations,LocationSerializer,request, items_per_page)
        else:
            serializer = LocationSerializer(locations, many = True, context={'user': request.user})
            return Response({
                'status': True,
                'data': serializer.data
            }) 


class DeleteLocationView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, location_id):
        
        try:
            user_location = UserLocation.objects.get(location_id = location_id, user = request.user, is_primary = False)
        except:
            return Response({
                'status': False,
                'message': _('This location does not exist.'),
            }, status=400)
        
        store_location = UserLocation.objects.get(location_id = location_id, is_primary = True)
        store = store_location.user
        location = Location.objects.get(id=user_location.location_id)
            
        # delete all details related to the store
        Deal.objects.filter(user=store).update(is_deleted=True)
        Classified.objects.filter(user=store).update(is_deleted=True)
        
        all_user_locations = UserLocation.objects.filter(location_id = location.id)
        all_user_locations.delete()
        location.delete()

        request.user.extra_location += 1
        request.user.save()

        store.is_deleted = True
        store.save()
        
        return Response({
            'status': True,
            'message': _('Location deleted successfully')
        })


class DeliveryPartnerListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)
    
    def get(self, requests):
        delivery_partners = DeliveryPartner.objects.all()
        serializer = DeliveryPartnerSerializer(delivery_partners, many = True)

        return Response({
            'status': True,
            'data': serializer.data
        })
    

class ProfileDetailsView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        serializer = ProfileSerializer(request.user, context={'user':request.user, 'request': request})

        return Response({
            'status': True,
            'data': serializer.data
        })
    

class OtherProfileDetailsView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, user_id):

        # user = get_valid_other_user(request,user_id)
        try:
            user = MyUser.objects.get(id=user_id)
        except:
            pass
        
        if not user:
            return Response({
                'status': False,
                'message':_("This user does not exist.")
            })

        serializer = ProfileSerializer(user, context={'user':request.user})

        return Response({
            'status': True,
            'data': serializer.data
        })
    

class NgoVideoCreateView(APIView):

    permission_classes = (IsAuthenticated, IsNGO, IsNormalUser)

    def post(self,request):
        serializer = NgoVideoSerializer(data = request.data, context={'request':request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'status': True,
                'data': serializer.data,
                'message': _('Ngo video added successfully')
            })


class NgoVideoListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)
    
    def get(self, request):
        ngo_videos = NgoVideo.objects.filter(user=request.user)
        serializer = NgoVideoSerializer(ngo_videos, many = True, context={'request':request,'user': request.user})

        return Response({
            'status': True,
            'data': serializer.data
        })


class NgoVideoDetailView(APIView):

    permission_classes = (IsAuthenticated, IsNGO, IsNormalUser)

    def get(self, request, ngo_video_id):
        
        try:
            ngo_video = NgoVideo.objects.get(id = ngo_video_id, user = request.user)
        except:
            return Response({
                'status': False,
                'message': _('This video does not exist.'),
            }, status=400)
        
        serializer = NgoVideoSerializer(ngo_video, context={'request':request,'user': request.user})
        
        return Response({
            'status': True,
            'data': serializer.data,
        })
          

class UpdateNgoVideoView(APIView):

    permission_classes = (IsAuthenticated, IsNGO, IsNormalUser)

    def post(self, request, ngo_video_id):
        
        try:
            ngo_video = NgoVideo.objects.get(id = ngo_video_id, user = request.user)
        except:
            return Response({
                'status': False,
                'message': _('This video does not exist.'),
            }, status=400)
        
        serializer = NgoVideoSerializer(ngo_video, data = request.data, context={'request':request,'user': request.user})
        
        if serializer.is_valid(raise_exception=True):
            
            serializer.save()
            
            return Response({
                'status': True,
                'data': serializer.data,
                'message': _('Ngo video updated successfully')
            })
        

class DeleteNgoVideoView(APIView):

    permission_classes = (IsAuthenticated, IsNGO, IsNormalUser)

    def get(self, request, ngo_video_id):
        
        try:
            ngo_video = NgoVideo.objects.get(id = ngo_video_id, user = request.user)
        except:
            return Response({
                'status': False,
                'message': _('This video does not exist.'),
            }, status=400)
        
        ngo_video.delete()
        
        return Response({
            'status': True,
            'message': _('Ngo video deleted successfully')
        })
    

class AuthenticatePasswordView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request):

        if "password" not in request.data:
            return Response({
                'status': False,
                'field': 'password',
                'message':_('Password is required')
            })
        
        user = authenticate(email = request.user.email, password = request.data["password"], is_verified = True)

        if user:
            
            return Response({
                'status': True,
                'tempToken': reload_token(request.user),
                'message':_('Password is correct')
            })
        else:
            return Response({
                'status': False,
                'message':_('Password incorrect')
            })
        

class NewEmailAddressView(APIView):

    def post(self,request):

        new_email = request.data.get('new_email', None)
        
        if not new_email:
            return Response({
                'status': False,
                'field': 'new_email',
                'message': _('New Email is required')
            }, status=400)
        
        
        
        if is_valid_email(new_email):
            try:
                email_already_exist = MyUser.objects.get(email = new_email)
            except:
                email_already_exist = None
            if email_already_exist:
                return Response({
                    'status': False,
                    'message': _('This new email is already in use. Send another email'),
                    'field': 'tempToken'
                })
            else:

                random_code = get_random_code()
                Code.objects.filter(user=request.user).delete()
                Code.objects.create(user=request.user, confirmation_code=random_code, usage = 'Change Email')
                
                custom_message = _("Please use below OTP to verify your email.")
                send_email_status = send_otp_email(new_email,random_code, custom_message)
                
                if send_email_status:
                    return Response({
                        'status': True,
                        'tempToken': reload_token(request.user),
                        'new_email': new_email,
                        'message': _('We have sent a verification code on your new email {}. Check Your Email For Verification Code!').format(new_email)
                    })
                else:
                    return Response({
                        "status": False,
                        "message": _("Something Went Wrong while sending OTP to {}, Please Try Again Later!".format(old_user.email))
                    }, status=400)
        else:
            return Response({
                'status': False,
                'message': _('Please send a valid email'),
                'field': 'tempToken'
            })


class ChangeEmailAddressView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self,request):

        new_email = request.data.get('new_email', None)
        otp = request.data.get('otp', None)

        if not otp:
            return Response({
                'status': False,
                'message': _('OTP is required'),
                'field': 'opt'
            }, status=400)

        
        if not new_email:
            return Response({
                'status': False,
                'field': 'new_email',
                'message': _('New Email is required')
            }, status=400)
        
        try:
            Code.objects.get(confirmation_code=otp, user = request.user, usage = 'Change Email')
        except:
            return Response({"status": False, "message": _("Invalid Code")}, status=400)
        
        if is_valid_email(new_email):
            try:
                email_already_exist = MyUser.objects.get(email = new_email)
            except:
                email_already_exist = None
            if email_already_exist:
                return Response({
                    'status': False,
                    'message': _('This new email is already in use. Send another email'),
                    'field': 'tempToken'
                })
            else:
                request.user.email = new_email
                request.user.save()
                return Response({
                    'status': True,
                    'message': _('Email changed successfully')
                })
                
        else:
            return Response({
                'status': False,
                'message': _('Please send a valid email'),
                'field': 'tempToken'
            })
        

class SubscribeNewsletter(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self,request):

        if request.user.newsletter_subscribed:
            request.user.newsletter_subscribed = False
            status = 'Unsubscribed'
        else:
            request.user.newsletter_subscribed = True
            status = 'Subscribed'

        request.user.save()
       
        return Response({
                'status': True,
                'message': _('{} for news letter').format(status),
                'field': 'tempToken'
            })


class AddRemoveFavouriteUserView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, user_id):

        other_user = get_valid_other_user(request,user_id)
        
        if not other_user:
            return Response({
                'status': False,
                'message':_("This user does not exist.")
            })

        if other_user in request.user.favourite_user.all():
            request.user.favourite_user.remove(other_user)
            status = "removed from"
        else:
            request.user.favourite_user.add(other_user)
            status = "added to"

        user_type = other_user.get_user_type_display()

        message = "{} {} favourites.".format(user_type,status)
        print("message",message)

        return Response({
            'status': True,
            'message': _(message)
        })


class LikeUnlikeNgoVideoView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, video_id):

        try:
            ngo_video = NgoVideo.objects.get(id=video_id)
        except:
            return Response({
                'status': False,
                'message':_("This video does not exist.")
            })
    
        if ngo_video in request.user.favourite_ngo_video.all():
            request.user.favourite_ngo_video.remove(ngo_video)
            status = "unliked"
        else:
            request.user.favourite_ngo_video.add(ngo_video)
            status = "liked"

        message = "Video {} successfully".format(status)

        return Response({
            'status': True,
            'message': _(message)
        })


class AddUserReviewView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request):

        serializer = AddUserReviewSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        other_user = get_valid_other_user(request,request.data["user"])

        if not other_user:
            return Response({
                'status': False,
                'message':_("This user does not exist.")
            })

        try:
            already_reviewed = Review.objects.get(user = other_user, reviewed_by = request.user)
        except:
            serializer.save()
            return Response({
                'status': True,
                'data': serializer.data,
                'message': _("Review added successfully.")
            })


        if already_reviewed:
            return Response({
                'status': False,
                'message':_("Already reviewed")
            })
        

class UserReviewListView(APIView):

    permission_classes = (AllowAny,)
    
    def get(self, request, user_id):

        pagination_on = self.request.GET.get('pagination_on')
        items_per_page = self.request.GET.get('items_per_page')

        try:
            user = MyUser.objects.get(id=user_id)
        except:
            return Response({
                "staus": False,
                "message": _("Invalid User")
            })

        reviews = Review.objects.filter(user=user)

        try:
            reviewed_by_logged_user = Review.objects.get(user=user,reviewed_by=request.user)
        except:
            reviewed_by_logged_user = False

        if reviewed_by_logged_user:
            reviewed_by_logged_user = True

        
        total_reviews = reviews.count()
        reviews_aggr = reviews.aggregate(Sum('rating'))
        sum_of_reviews = reviews_aggr['rating__sum']

        if sum_of_reviews:
            average_reviews = sum_of_reviews/total_reviews
        else:
            average_reviews = 0
        
        extra_data = {
            "reviewed_by_logged_user":reviewed_by_logged_user,
            "total_reviews": total_reviews,
            "average_reviews": average_reviews
        }

        if pagination_on:
            return paginated_data(reviews,UserReviewDetailSerializer,request, items_per_page,extra_data = extra_data)
        else:
            serializer = UserReviewDetailSerializer(reviews, many = True, context={'user': request.user})
            data = serializer.data

            return Response({
                    "status": True,
                    "data": data,
                    "extra_data":extra_data
                })


class UserReviewMarkUsefulView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request):

        try:
            review = Review.objects.get(id=request.data.get("review"))
        except:
            return Response({
                "status": False,
                "message":_("Invalid Review")
            })
        
        try:
            already_marked = ReviewMark.objects.get(user = request.user, review = review)
        except:
            serializer = ReviewMarkSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': True,
                'data': serializer.data,
                'message': _("Review marked successfully.")
            })

        if already_marked:
            return Response({
                'status': False,
                'message':_("Already marked")
            })


class UserReviewAddFlagView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request):

        try:
            review = Review.objects.get(id=request.data.get("review"))
        except:
            return Response({
                "status": False,
                "message":_("Invalid Review")
            })
        
        try:
            already_flagged = ReviewFlag.objects.get(user = request.user, review = review)
        except:
            serializer = ReviewFlagSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': True,
                'data': serializer.data,
                'message': _("Review flagged successfully.")
            })

        if already_flagged:
            return Response({
                'status': False,
                'message':_("Already flagged")
            })

        
class NgoPartnersListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)
    
    def get(self, request):

        search_lat = request.GET.get('search_lat')
        search_lon = request.GET.get('search_lon')
        items_per_page = self.request.GET.get('items_per_page')
        pagination_on = self.request.GET.get('pagination_on')
        ngo_category = request.GET.get('ngo_category')
        sort_by_date_joined = request.GET.get('sort_by_date_joined')
        star_rating = request.GET.get('star_rating')
        sort_by_members_associated = request.GET.get('sort_by_members_associated')
        sort_by_business_associated = request.GET.get('sort_by_business_associated')

        ngos = active_users().filter(user_type='ngo').exclude(id=request.user.id,)
        
        if ngo_category:
            ngos = ngos.filter(user_type_category_id = ngo_category)
        if sort_by_date_joined:
            ngos = ngos.order_by("-created_at")
        if star_rating:
            ngos = ngos.annotate(average_rating = Avg('reviews__rating')).filter(average_rating__gte = star_rating)
            search_lat,search_lon = '',''
        if sort_by_members_associated:
            ngos = ngos.annotate( total_members = Count('ngos_associated', filter=Q(ngos_associated__user_type='member'))).order_by('-total_members')
            search_lat,search_lon = '',''
        if sort_by_business_associated:
            ngos = ngos.annotate(total_members = Count('ngos_associated', filter=Q(ngos_associated__user_type='business'))).order_by('-total_members')
            search_lat,search_lon = '',''
        if search_lat and search_lon:
            ngos = nearest_users(ngos, search_lat, search_lon)


        if pagination_on:
            return paginated_data(ngos,UserProfileSerializer,request, items_per_page)
        else:
            serializer = UserProfileSerializer(ngos, many = True, context={'user': request.user})
            return Response({
                'status': True,
                'data': serializer.data
            })    

    
class BusinessProfileListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        pagination_on = self.request.GET.get('pagination_on')
        items_per_page = self.request.GET.get('items_per_page')
        search_key = request.GET.get('search_key')
        business_category = request.GET.get('business_category')
        sort_by_date_joined = request.GET.get('sort_by_date_joined')
        star_rating = request.GET.get('star_rating')
        remove_user = request.GET.get('remove_user')
        
        business_profiles = active_businesses().filter(user_type='business').exclude(id=request.user.id)
        
        search_by_ngo = request.GET.get('ngo')
        if search_by_ngo:
            business_user_ids = [usr.id for usr in MyUser.objects.filter(ngo = search_by_ngo)]
            if business_user_ids:
                business_profiles = business_profiles.filter(id__in = business_user_ids)
            else:
                business_profiles = business_profiles.none()

        if business_category:
            business_profiles = business_profiles.filter(business_category=business_category)

        if search_key:
            business_profiles = business_profiles.filter(Q(name__icontains = search_key) | Q(email__icontains = search_key))

        if sort_by_date_joined:
            business_profiles = business_profiles.order_by("-created_at")
        if star_rating:
            business_profiles = business_profiles.annotate(average_rating = Avg('reviews__rating')).filter(average_rating__gte = star_rating)


        if remove_user:
            business_profiles = business_profiles.exclude(id=remove_user)


        if pagination_on:
            return paginated_data(business_profiles,UserProfileSerializer,request, items_per_page)
        else:
            serializer = UserProfileSerializer(business_profiles, many=True, context={'user': request.user})
            return Response({
                'status': True,
                'data': serializer.data
            })
        

class MemberUserListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        pagination_on = self.request.GET.get('pagination_on')
        items_per_page = self.request.GET.get('items_per_page')
        search_key = request.GET.get('search_key')
        sort_by_date_joined = request.GET.get('sort_by_date_joined')
        star_rating = request.GET.get('star_rating')
        
        members = active_users().filter(user_type='member').exclude(id=request.user.id)
        
        search_by_ngo = request.GET.get('ngo')
        if search_by_ngo:
            member_user_ids = [usr.id for usr in MyUser.objects.filter(ngo = search_by_ngo)]
            if member_user_ids:
                members = members.filter(id__in = member_user_ids)
            else:
                members = members.none()

        if search_key:
            members = members.filter(Q(firtsname__icontains = search_key)| Q(lastname__icontains = search_key) | Q(email__icontains = search_key))

        if sort_by_date_joined:
            members = members.order_by("-created_at")
        if star_rating:
            members = members.annotate(average_rating = Avg('reviews__rating')).filter(average_rating__gte = star_rating)


        if pagination_on:
            return paginated_data(members,UserProfileSerializer,request, items_per_page)
        else:
            serializer = UserProfileSerializer(members, many=True, context={'user': request.user})
            return Response({
                'status': True,
                'data': serializer.data
            })


class AddRemoveFavouriteNgoVideoView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, video_id):

        try:
            video = NgoVideo.objects.get(id=video_id)
        except:
            return Response({
                'status': False,
                'message':_("This video does not exist.")
            })

        if video in request.user.favourite_ngo_video.all():
            request.user.favourite_ngo_video.remove(video)
            status = "removed from"
        else:
            request.user.favourite_ngo_video.add(video)
            status = "added to"

        message = "Video {} favourite videos".format(status)

        return Response({
            'status': True,
            'message': _(message)
        })


class AllFavoiriteWishlist(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self,request,type):

        search_key = request.GET.get('search_key')

        if type == 'user':
            favourite_users = request.user.favourite_user.all()
            user_type = request.GET.get('user_type')
            if user_type == 'business':
                favourite_users = favourite_users.filter(user_type='business')
            elif user_type == 'member':
                favourite_users = favourite_users.filter(user_type='member')
            elif user_type == 'ngo':
                favourite_users = favourite_users.filter(user_type='ngo')
            if search_key:
                favourite_users = favourite_users.filter(Q(firstname__icontains = search_key) | Q(lastname__icontains = search_key)| Q(name__icontains = search_key)| Q(email__icontains = search_key))
            return paginated_data(favourite_users,UserProfileSerializer,request,6)
        
        if type == 'listing':
            favourite_deals = request.user.favourite_deal.all()
            favourite_deals = favourite_deals.filter(weekly=False)
            if search_key:
                favourite_deals = favourite_deals.filter(Q(title__icontains = search_key) | Q(description__icontains = search_key))
            return paginated_data(favourite_deals, BusinessDealSerializer, request, 6)
        
        if type == 'weekly':
            favourite_deals = request.user.favourite_deal.all()
            favourite_deals = favourite_deals.filter(weekly=True)
            if search_key:
                favourite_deals = favourite_deals.filter(Q(title__icontains = search_key) | Q(description__icontains = search_key))
            return paginated_data(favourite_deals, BusinessDealSerializer, request, 6)
        
        if type == 'classified':
            favourite_classified = request.user.favourite_classified.all()
            if search_key:
                favourite_classified = favourite_classified.filter(Q(title__icontains = search_key) | Q(description__icontains = search_key))
            return paginated_data(favourite_classified, ClassifiedSerializer, request, 6)
        
        if type == 'business':
            favourite_users = request.user.favourite_user.all()
            favourite_users = favourite_users.filter(user_type='business')
            if search_key:
                favourite_users = favourite_users.filter(Q(firstname__icontains = search_key) | Q(lastname__icontains = search_key)| Q(name__icontains = search_key)| Q(email__icontains = search_key))
            return paginated_data(favourite_users,UserProfileSerializer,request,6)
        
        
        if type == 'video':
            favourite_videos = request.user.favourite_ngo_video.all()
            print('favourite_videos',favourite_videos)
            if search_key:
                favourite_videos = favourite_videos.filter(title__icontains = search_key)
            return paginated_data(favourite_videos,NgoVideoSerializer,request,6)
        
        if type == 'job':
            favourite_jobs = request.user.favourite_job.all()
            if search_key:
                favourite_jobs = favourite_jobs.filter(title__icontains = search_key)
            return paginated_data(favourite_jobs,JobDetailSerializer,request,6)
        

class PopularNewsAgencyListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        pagination_on = self.request.GET.get('pagination_on')
        media_houses = active_users().filter(user_type='news_agency').exclude(id=request.user.id)
        
        if pagination_on:
            return paginated_data(media_houses,NewsAgencySerializer,request, 6)
        else:
            serializer = NewsAgencySerializer(media_houses, many=True, context={'user': request.user})
            return Response({
                'status': True,
                'data': serializer.data
            })
        

# class NewsAgencyDetailsView(APIView):

#     permission_classes = (IsAuthenticated, IsNormalUser)

#     def get(self, request, user_id):

#         user = get_valid_other_user(request,user_id)
        
#         if not user:
#             return Response({
#                 'status': False,
#                 'message':_("This user does not exist.")
#             })

#         serializer = NewsAgencyDetailSerializer(user)

#         return Response({
#             'status': True,
#             'data': serializer.data
#         })
    

class UnitProductCostListView(APIView):

    def get(self, request):

        to_currency = self.request.GET.get('to_currency')

        if to_currency:
            convert_to = to_currency
        else:
            convert_to = request.user.currency.iso_code


        deal_amount_in_usd = get_single_product_cost(request.user,'deal', 'listing', 'main_amount')
        weekly_deal_amount_in_usd = get_single_product_cost(request.user,'deal', 'weekly', 'main_amount')
        classified_amount_in_usd = get_single_product_cost(request.user,'classified', '', 'main_amount')

        SINGLE_LOCATION_COST = ProductPrice.objects.get(product_name="SINGLE_LOCATION_COST")

        return Response({
            "status": True,
            "deal": __(deal_amount_in_usd, 'usd', convert_to),
            "weekly_deal": __(weekly_deal_amount_in_usd, 'usd', convert_to),
            "classified": __(classified_amount_in_usd, 'usd', convert_to),
            "location": __(SINGLE_LOCATION_COST.cost, 'usd', convert_to),
            "tax": __(settings.SHUKTV_TAX_COST, 'usd', convert_to),
        })
    

class AddUserFlagView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request):

        serializer = AddUserFlagSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        other_user = get_valid_other_user(request,request.data["user"])
        
        if not other_user:
            return Response({
                "status": False,
                "message":_("Invalid User")
            })
        
        try:
            already_flagged = Flagged.objects.get(user = other_user, flagged_by = request.user)
        except:
            serializer.save()
            return Response({
                'status': True,
                'data': serializer.data,
                'message': _("Flagged successfully.")
            })

        if already_flagged:
            return Response({
                'status': False,
                'message':_("Already flagged.")
            })


class UserTypeCategoryView(APIView):

    def get(self, request, user_type):

        categories = UserTypeCategory.objects.filter(user_type = user_type)
        serializer = UserTypeCategorySerializer(categories, many=True, context={"request": request})

        return Response({
            "status": True,
            "data": serializer.data
        })  


class PaymentHistoryView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        items_per_page = self.request.GET.get('items_per_page')
        pagination_on = self.request.GET.get('pagination_on')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        to_currency = self.request.GET.get('to_currency')

        payments = PaymentDetail.objects.filter(user=request.user, status='complete').order_by("-created_at")

        # date filter
        if start_date and end_date:
            try:
                payments = payments.filter(created_at__date__gte = start_date, created_at__date__lte = end_date)
            except:
                return Response({
                    "status": False,
                    "message": _("The date format seems wrong. Please send date as: 2024-02-01")
                })
        

        if pagination_on:
            return paginated_data(payments, PaymentDetailSerializer, request, items_per_page)
        else:
            serializer = PaymentDetailSerializer(payments, many=True, context = {'to_currency': to_currency, 'request': request})
            return Response({
                "status": True,
                "data": serializer.data
            }) 


class PaymentInvoiceDownloadView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, payment_id):

        try:
            payment = PaymentDetail.objects.get(id=payment_id, user=request.user, status='complete')
        except:
            return Response({
                "status": False,
                "message": _("Invalid payment.")
            })
        

        currency = Currency.objects.get(iso_code = payment.currency)
        
        data={
            "payment" : payment,
            "payment_currency_sign": currency.name
        }
        
        pdf = render_to_pdf('account/payment-invoice.html', data)
        
        # below returns the pdf view in browser
        # return HttpResponse(pdf, content_type='application/pdf')
        
        # to start force download
        if pdf:
            
            response = HttpResponse(pdf, content_type = 'application/pdf')
            filename = f"INVOICE-%s.pdf" %(payment.created_at.strftime("%Y-%m-%d"))
            content = 'attachement; filename= "%s"' %(filename)
            response['Content-Disposition'] = content
            return response
        
        return HttpResponse("not found")

        
class NGOPaymentHistoryView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        items_per_page = self.request.GET.get('items_per_page')
        pagination_on = self.request.GET.get('pagination_on')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

        payments = NGOPayout.objects.filter(ngo=request.user).order_by("-created_at")

        # date filter
        if start_date and end_date:
            try:
                payments = payments.filter(created_at__date__gte = start_date, created_at__date__lte = end_date)
            except:
                return Response({
                    "status": False,
                    "message": _("The date format seems wrong. Please send date as: 2024-02-01")
                })

        # filter start
        filter_by = self.request.GET.get('filter_by')
        if filter_by == 'businesses':
            payments = payments.filter(user__user_type = 'business')
        elif filter_by == 'members':
            payments = payments.filter(user__user_type = 'member')
        # filter end
        

        if pagination_on:
            return paginated_data(payments, NGOPayoutSerializer, request, items_per_page)
        else:
            serializer = NGOPayoutSerializer(payments, many=True)
            return Response({
                "status": True,
                "data": serializer.data
            })  


class NGOPaymentReportView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        items_per_page = self.request.GET.get('items_per_page')
        pagination_on = self.request.GET.get('pagination_on')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

        payments = NGOPayout.objects.filter(ngo=request.user)

        # date filter
        if start_date and end_date:
            try:
                payments = payments.filter(created_at__date__gte = start_date, created_at__date__lte = end_date)
            except:
                return Response({
                    "status": False,
                    "message": _("The date format seems wrong. Please send date as: 2024-02-01")
                })
        else:
            first_date_current_month = datetime.datetime.today().replace(day=1).date()
            dt = datetime.datetime.now()
            first_date_next_month = (dt.replace(day=1) + datetime.timedelta(days=32)).replace(day=1).date()
            payments = payments.filter(created_at__date__gte = first_date_current_month, created_at__date__lt = first_date_next_month)
        
        # business start
        free_business_under_ngo = active_users().filter(user_type = 'business', ngo = request.user, plan__amount=0).count()
        paid_business_under_ngo = active_users().filter(user_type = 'business', ngo = request.user, plan__amount__gt = 0).count()
        
        free_business_payments = payments.filter(user__user_type = 'business', user__plan__amount = 0)
        free_business_subscription_payments = free_business_payments.filter(payment_detail__item_type = 'plan').aggregate(Sum('amount'))
        free_business_deal_payments = free_business_payments.filter(payment_detail__item_type = 'deal').aggregate(Sum('amount'))
        free_business_weekly_deal_payments = free_business_payments.filter(payment_detail__item_type = 'weekly_deal').aggregate(Sum('amount'))
        
        paid_business_payments = payments.filter(user__user_type = 'business', user__plan__amount__gt = 0)
        paid_business_subscription_payments = paid_business_payments.filter(payment_detail__item_type = 'plan').aggregate(Sum('amount'))
        paid_business_deal_payments = paid_business_payments.filter(payment_detail__item_type = 'deal').aggregate(Sum('amount'))
        paid_business_weekly_deal_payments = paid_business_payments.filter(payment_detail__item_type = 'weekly_deal').aggregate(Sum('amount'))
        # business end

        # member start
        free_members_under_ngo = active_users().filter(user_type = 'member', ngo = request.user, plan__amount=0).count()
        paid_members_under_ngo = active_users().filter(user_type = 'member', ngo = request.user, plan__amount__gt = 0).count()
        
        free_members_payments = payments.filter(user__user_type = 'member', user__plan__amount = 0)
        free_members_subscription_payments = free_members_payments.filter(payment_detail__item_type = 'plan').aggregate(Sum('amount'))
        free_members_deal_payments = free_members_payments.filter(payment_detail__item_type = 'deal').aggregate(Sum('amount'))
        free_members_weekly_deal_payments = free_members_payments.filter(payment_detail__item_type = 'weekly_deal').aggregate(Sum('amount'))
        free_members_classified_payments = free_members_payments.filter(payment_detail__item_type = 'classified').aggregate(Sum('amount'))
        
        paid_members_payments = payments.filter(user__user_type = 'member', user__plan__amount__gt = 0)
        paid_members_subscription_payments = paid_members_payments.filter(payment_detail__item_type = 'plan').aggregate(Sum('amount'))
        paid_members_deal_payments = paid_members_payments.filter(payment_detail__item_type = 'deal').aggregate(Sum('amount'))
        paid_members_weekly_deal_payments = paid_members_payments.filter(payment_detail__item_type = 'weekly_deal').aggregate(Sum('amount'))
        paid_members_classified_payments = paid_members_payments.filter(payment_detail__item_type = 'classified').aggregate(Sum('amount'))
        # member end

        donation_sub_total = convert_to_int(free_business_subscription_payments['amount__sum']) + convert_to_int(paid_business_subscription_payments['amount__sum']) + convert_to_int(free_members_subscription_payments['amount__sum']) + convert_to_int(paid_members_subscription_payments['amount__sum'])
        deal_sub_total = convert_to_int(free_business_deal_payments['amount__sum']) + convert_to_int(paid_business_deal_payments['amount__sum']) + convert_to_int(free_members_deal_payments['amount__sum']) + convert_to_int(paid_members_deal_payments['amount__sum'])
        weekly_deal_sub_total = convert_to_int(free_business_weekly_deal_payments['amount__sum']) + convert_to_int(paid_business_weekly_deal_payments['amount__sum']) + convert_to_int(free_members_weekly_deal_payments['amount__sum']) + convert_to_int(paid_members_weekly_deal_payments['amount__sum'])
        classified_sub_total = convert_to_int(free_members_classified_payments['amount__sum']) + convert_to_int(paid_members_classified_payments['amount__sum'])

        return Response({
            "status": True,
            "data":{
            
                "total_businesses": free_business_under_ngo + paid_business_under_ngo,
                "free_business_under_ngo": free_business_under_ngo,
                "free_business_subscription_payments": convert_to_int(free_business_subscription_payments['amount__sum']),
                "free_business_deal_payments": convert_to_int(free_business_deal_payments['amount__sum']),
                "free_business_weekly_deal_payments": convert_to_int(free_business_weekly_deal_payments['amount__sum']),
                "paid_business_under_ngo": paid_business_under_ngo,
                "paid_business_subscription_payments": convert_to_int(paid_business_subscription_payments['amount__sum']),
                "paid_business_deal_payments": convert_to_int(paid_business_deal_payments['amount__sum']),
                "paid_business_weekly_deal_payments": convert_to_int(paid_business_weekly_deal_payments['amount__sum']),
                
                "total_members": free_members_under_ngo + paid_members_under_ngo,
                "free_members_under_ngo": free_members_under_ngo,
                "free_members_subscription_payments": convert_to_int(free_members_subscription_payments['amount__sum']),
                "free_members_deal_payments": convert_to_int(free_members_deal_payments['amount__sum']),
                "free_members_weekly_deal_payments": convert_to_int(free_members_weekly_deal_payments['amount__sum']),
                "free_members_classified_payments": convert_to_int(free_members_classified_payments['amount__sum']),
                "paid_members_under_ngo": paid_members_under_ngo,
                "paid_members_subscription_payments": convert_to_int(paid_members_subscription_payments['amount__sum']),
                "paid_members_deal_payments": convert_to_int(paid_members_deal_payments['amount__sum']),
                "paid_members_weekly_deal_payments": convert_to_int(paid_members_weekly_deal_payments['amount__sum']),
                "paid_members_classified_payments": convert_to_int(paid_members_classified_payments['amount__sum']),

                "donation_sub_total": donation_sub_total,
                "deal_sub_total": deal_sub_total,
                "weekly_deal_sub_total": weekly_deal_sub_total,
                "classified_sub_total": classified_sub_total,

                "grand_total": donation_sub_total + deal_sub_total + classified_sub_total
            }
        })


class UpdateNGOView(APIView):
    
    def post(self, request):

        if request.user.user_type == 'ngo':
            return Response({
                "status": False,
                "message": _("Non profitable organizations cannot choose another Non profitable organizations.")
            })

        if "ngo" not in request.data:
            return Response({
                "status": False,
                "message": _("Please select ngo to update"),
                "field": "ngo"
            })

        try:
            ngo = active_ngos().get(id=request.data.get("ngo"), user_type="ngo")
        except:
            return Response({
                "status": False,
                "message": _("Invalid Non Profitable Organization")
            })
        
        request.user.ngo = ngo
        request.user.save()

        return Response({
            "status":True,
            "message": _("Non Profitable Organization updated successfully")
        })
