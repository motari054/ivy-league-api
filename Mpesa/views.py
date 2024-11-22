from __future__ import unicode_literals
from .import utils

from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from .core import MpesaClient
from decouple import config
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'

def index(request):

	return HttpResponse('Welcome to the home of daraja APIs')

def oauth_success(request):
	r = cl.access_token()
	return JsonResponse(r, safe=False)


class PaymentView(APIView):
    permission_classes = [AllowAny]  # Set permission class to allow any user (authenticated or not)

    def post(self, request):
        data = request.data
        phone_number = data.get('phoneNumber')
        amount = data.get('amount')
        account_reference = data.get('accountReference', 'Ivy League Beauty')
        transaction_desc = data.get('transactionDesc', 'Payment for Beauty Products')
        callback_url = data.get('callbackUrl', 'https://darajambili.herokuapp.com/express-payment')

        cl = MpesaClient()
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

        # Return the response
        return Response(response)
