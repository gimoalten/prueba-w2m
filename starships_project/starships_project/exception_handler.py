""" exception_handler.py """
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler


def custom_exception_handler(exc, context):
    """ custon exception handler """
    response = drf_exception_handler(exc, context)
    if response is None:
        return Response(
            {"error": str(exc)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return response
