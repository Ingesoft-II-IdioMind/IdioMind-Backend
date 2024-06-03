import base64
import requests
from django.conf import settings

# Configuración de PayPal obtenida de Django settings
PAYPAL_CLIENT_ID = settings.PAYPAL_CLIENT_ID
PAYPAL_CLIENT_SECRET = settings.PAYPAL_CLIENT_SECRET 
BASE_URL = settings.BASE_URL

def generateAccessToken():
    if not PAYPAL_CLIENT_ID or not PAYPAL_CLIENT_SECRET:
        raise Exception("PAYPAL_CLIENT_ID or PAYPAL_CLIENT_SECRET is not set")

    auth = f"{PAYPAL_CLIENT_ID}:{PAYPAL_CLIENT_SECRET}"
    auth = base64.b64encode(auth.encode()).decode("utf-8")

    try:
        response = requests.post(
            BASE_URL + "/v1/oauth2/token",
            data={"grant_type": "client_credentials"},
            headers={"Authorization": f"Basic {auth}"}
        )
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        data = response.json()
        return data["access_token"]
    except requests.RequestException as e:
        print("Error generating access token:", e)
        raise

def create_order(description, amount):
    try:
        access_token = generateAccessToken()
        url = BASE_URL + "/v2/checkout/orders"
        payload = {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "description": description,
                    "amount": {
                        "currency_code": "USD",
                        "value": amount
                    }
                }
            ]
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        return response.json()
    except requests.RequestException as e:
        print(f"Error creating {description} order:", e)
        raise

def create_order_annual(productos):
    print(productos)
    return create_order("Suscripción de un año", "70")

def create_order_mensual(productos):
    print(productos)
    return create_order("Suscripción de un mes", "7")

def capture_order(orderID):
    try:
        access_token = generateAccessToken()
        url = BASE_URL + f"/v2/checkout/orders/{orderID}/capture"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.post(url, headers=headers)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        return response.json()
    except requests.RequestException as e:
        print(f"Error capturing order {orderID}:", e)
        raise
