import base64
import requests
from django.conf import settings

PAYPAL_CLIENT_ID = settings.PAYPAL_CLIENT_ID
PAYPAL_CLIENT_SECRET = settings.PAYPAL_CLIENT_SECRET 
BASE_URL = settings.BASE_URL


def generateAccessToken():
    if not PAYPAL_CLIENT_ID or not PAYPAL_CLIENT_SECRET:
        raise Exception("PAYPAL_CLIENT_ID or PAYPAL_CLIENT_SECRET is not set")
    auth = f"{PAYPAL_CLIENT_ID}:{PAYPAL_CLIENT_SECRET}"
    auth = base64.b64encode(auth.encode()).decode("utf-8")

    response = requests.post(
            BASE_URL+"/v1/oauth2/token",
            data={"grant_type": "client_credentials"},
            headers={"Authorization": f"Basic {auth}"}
    )
    data = response.json()
    #print(data["access_token"])
    return data["access_token"]


def create_order(productos):
    print(productos)
    try:
        accsess_token = generateAccessToken()
        url = BASE_URL + "/v2/checkout/orders"
        payload = {
            "intent":"CAPTURE",
            "purchase_units":[
                {
                     "description": "Suscripción de un año",
                    "amount":{
                        "currency_code":"USD",
                        "value":"7"
                    }
                }
            ]
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {accsess_token}"
        }

        response = requests.post(url, headers=headers , json=payload)
        
        #print("---response---", response.json())
        return response.json()
    except Exception as e:
        print("*******")
        print(e)
        
def capture_order(orderID):
    access_token = generateAccessToken()
    url = BASE_URL + f"/v2/checkout/orders/{orderID}/capture"
    print(url)

    headers = {
        "Content-Type":"application/json",
        "Authorization":f"Bearer {access_token}"
    }

    response = requests.post(url, headers=headers)
    print("---response---", response.json())
    return response.json()
