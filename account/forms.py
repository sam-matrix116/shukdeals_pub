from django import forms
from account.models import Plan, DeliveryPartner, Vendor, VendorExpense, ProductPrice

class AdminLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
        attrs={'class' : 'form-control','placeholder': 'Enter Email Address'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter the password'}
        )
    )


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('name', 'amount')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Plan Name'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ProductPriceForm(forms.ModelForm):
    class Meta:
        model = ProductPrice
        fields = ('product_name', 'cost')

        widgets = {
            'product_name': forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class DeliveryPartnerForm(forms.ModelForm):
    class Meta:
        model = DeliveryPartner
        fields = ('name','image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'})
        }


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('name','phone','email','address')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address'})
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = VendorExpense
        fields = ('vendor','invoice_number','file','amount','date','remarks')

        widgets = {
            'vendor': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Vendor'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Invoice Number'}),
            'file': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Select Invoice'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'id':"my_date_picker", 'placeholder': 'Enter Date'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add Remarks'})
        }