import requests
import keys
from datetime import datetime
import base64
from requests.auth import HTTPBasicAuth

#generate timestamp
unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

#generate password
data_to_encode = keys.business_shortcode + keys.mpesa_passkey + formatted_time
encoded_bytes = base64.b64encode(data_to_encode.encode("utf-8"))
encoded_string = str(encoded_bytes, "utf-8")



#authentication



consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))


json_response = r.json()
sauda_token = json_response['access_token']
print(sauda_token)


def lipa_na_mpesa():


    access_token = sauda_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
      "BusinessShortCode": keys.business_shortcode,
      "Password": encoded_string,
      "Timestamp": formatted_time,
      "TransactionType": "CustomerPayBillOnline",
      "Amount": "5",
      "PartyA": keys.phone_number,
      "PartyB": keys.business_shortcode,
      "PhoneNumber": keys.phone_number,
      "CallBackURL": "https://fullstackdjango.com/lipanampesa",
      "AccountReference": "31643",
      "TransactionDesc": "Donate to Mshauri"
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

lipa_na_mpesa()
