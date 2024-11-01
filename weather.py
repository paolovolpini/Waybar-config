import geocoder
import requests
import json

def get_coords(): 
    coords = geocoder.ip('me')
    if coords.latlng is not None:
        return coords.latlng
    else:
        return None

api_key = "0262cb2ba7e3f013347550708bb083c4"
# "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
data = {}

if __name__ == '__main__':
    coords = get_coords()
    temperature = "Null"
    tooltip = "Null"
    if coords is not None:
        lat, lon = coords
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            temperature = str(round(weather_data["main"]["temp"] - 273.15)) + "°C"
            tooltip = weather_data["weather"][0]["main"]
            img_code = weather_data["weather"][0]["icon"]
            img_url = f"https://openweathermap.org/img/wn/{img_code}@2x.png"
            img_data = requests.get(img_url).content
            with open("/tmp/image_weather_script.jpg", "wb") as image:
                image.write(img_data)
    data["text"] = temperature
    data["tooltip"] = tooltip
    print(json.dumps(data))
