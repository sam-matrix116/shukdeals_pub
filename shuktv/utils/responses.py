from rest_framework.response import Response

def error_response(msg: str, field: str = '', key_values: dict = {}, status: int = 400):
    response = {
        "status": False,
    }
    if field: response['field'] = field
    if msg: response['message'] = msg
    response.update(key_values)
    return Response(response, status=status)


def success_response(msg: str, key_values: dict = {}, status: int = 200):
    response = {
        "status": True,
        "message": msg
    }
    response.update(key_values)
    return Response(response, status=status)