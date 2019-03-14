import requests


def weather_by_city(city_name):
    url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": "22248dc42aa747e0b08195448191403",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    result = requests.get(url, params=params)
    weather = result.json()
    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
    return False


if __name__ == "__main__":
    print(weather_by_city('Moscow'))
