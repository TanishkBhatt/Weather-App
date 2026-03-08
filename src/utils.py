import requests
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

def fetch_data(city: str, API_KEY: str) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)

    if (res.status_code == 200):
        return res.json()

    elif (res.status_code == 401):
        raise Exception("Invalid API_KEY")
    elif (res.status_code == 404):
        raise Exception("City Name Not Found")
    else:
        raise Exception("Something Went Wrong")


def plot_data(res: dict) -> Figure:
    fig, ax = plt.subplots()
    values = [res["main"]["temp"], res["main"]["feels_like"], res["main"]["humidity"], res["wind"]["speed"]]
    labels = ["TEMPERATURE", "FEELS LIKE", "HUMIDITY", "WIND SPEED"]

    ax.bar(labels, values)
    ax.set_title("BASIC GRAPHICAL REPRESENTATION")
    return fig