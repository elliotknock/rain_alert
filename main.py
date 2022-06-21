import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = os.environ.get("TWILIO_ACC_SID")
print(account_sid)
auth_token = os.environ.get("KEY")
print(auth_token)

weather_params = {
    "lat": 11.731195,
    "lon": 8.526586,
    "appid": "69f04e4613056b159c2761a9d9e664d2",
    "exclude": "current,minutely,daily",
}

will_rain = False

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂",
        from_="+18575780928",
        to="+44 7930 421322"
    )
    print(message.status)
