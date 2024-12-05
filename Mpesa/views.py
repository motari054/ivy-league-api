from __future__ import unicode_literals
from . import utils

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from datetime import datetime
from .models import Payments
from .core import MpesaClient
from decouple import config

cl = MpesaClient()
stk_push_callback_url = (
    "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
)

def index(request):
    return HttpResponse("Welcome to the home of Daraja APIs")


def oauth_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)


class PaymentView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        phone_number = data.get("phoneNumber")
        amount = data.get("amount")
        account_reference = data.get("accountReference", "The Ivy League Beauty Shop")
        transaction_desc = data.get("transactionDesc", "Payment for Beauty Products")
        callback_url = data.get("callbackUrl", stk_push_callback_url)

        # Initiate STK Push
        response = cl.stk_push(
            phone_number, amount, account_reference, transaction_desc, callback_url
        )
        return Response(response)


class MpesaCallbackView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            callback_data = request.data
            body = callback_data.get("Body", {})
            stk_callback = body.get("stkCallback", {})
            result_code = stk_callback.get("ResultCode")
            result_desc = stk_callback.get("ResultDesc")
            merchant_request_id = stk_callback.get("MerchantRequestID")
            checkout_request_id = stk_callback.get("CheckoutRequestID")
            callback_metadata = stk_callback.get("CallbackMetadata", {}).get("Item", [])

            transaction_details = {
                item["Name"]: item.get("Value") for item in callback_metadata
            }

            if result_code == 0:
                receipt_number = transaction_details.get("MpesaReceiptNumber")
                amount = transaction_details.get("Amount")
                phone_number = transaction_details.get("PhoneNumber")
                transaction_date = datetime.strptime(
                    str(transaction_details.get("TransactionDate")), "%Y%m%d%H%M%S"
                )

                Payments.objects.create(
                    merchant_request_id=merchant_request_id,
                    checkout_request_id=checkout_request_id,
                    receipt_number=receipt_number,
                    phone_number=phone_number,
                    amount=amount,
                    result_code=result_code,
                    result_desc=result_desc,
                    transaction_date=transaction_date,
                )
                print("Payment saved successfully.")
            else:
                print(f"Payment failed: {result_desc}")

            # Respond to Safaricom
            return Response({"Status": "success"}, status=200)

        except Exception as e:
            print(f"Error processing callback: {str(e)}")
            return Response({"error": "Failed to process callback"}, status=500)
