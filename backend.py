import os

import requests

API_KEY = os.getenv("WEATHER_API")


def get_data(place, forecast_days):
    endpoint = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(endpoint)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    get_data(place="tokyo", forecast_days=1)
