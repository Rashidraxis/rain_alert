import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "78977844ee73c6a801ab779ccb1c5803"
account_sid = "AC57159f356aa8a93daf4cddd998938c56"
auth_token = "6e4ac0db6f5f8fdf68a87cfb7675acb9"

weather_params = {
    "lat": 17.883333,
    "lon": -11.016667,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+18644007766",
        to="+919892827387"
    )
    print(message.status)
