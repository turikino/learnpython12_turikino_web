from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city('Moscow,Russia')
    # weather = False
    if weather:
        return "Температура: {}, ощущается {}.".format(weather["temp_C"], weather["FeelsLikeC"])
    else:
        return "Сервис не доступен!"

if __name__ == "__main__":
    app.run(debug=True)