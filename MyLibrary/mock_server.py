from flask import Flask, request, jsonify
appFlask = Flask(__name__)
@appFlask.route('/data/2.5/weather')
def test():
    q = request.args.get('q')
    
    appid = request.args.get('appid')
    dict = {

        "coord": {
            "lon": 123.26,
            "lat": 44.56
            },
        "weather": [
            {
            "id": 801,
            "main": "Clouds",
            "description": "few clouds",
            "icon": "02n"
            }
            ],
        "base": "stations",
            "main": {
                "temp": 280.18,
                "feels_like": 278.01,
                "temp_min": 280.18,
                "temp_max": 280.18,
                "pressure": 1024,
                "humidity": 38,
                "sea_level": 1024,
                "grnd_level": 1006
            },
        "visibility": 10000,
        "wind": {
            "speed": 3.13,
            "deg": 161,
            "gust": 3.22
        },
        "clouds": {
            "all": 17
        },
        "dt": 1666602189,
        "sys": {
            "country": "CN",
            "sunrise": 1666563175,
            "sunset": 1666601354
        },
        "timezone": 28800,
        "id": 2036338,
        "name": "Kaitong",
        "cod": 200  
    }
    return jsonify(dict)
appFlask.run(debug=True, port=5000) 