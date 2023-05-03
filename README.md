# Test Globant >
Technical test: WeatherAPI

This tests use an external API [www.openweathermap.org](https://openweathermap.org).

## Instructions
Install
```sh
git clone git@github.com:osvaldomx/test-globant.git
cd test-globant
pip install requirements.txt
```

## Get Started
Run project
```sh
python app.py
```

### Web App
In your browser access to url 127.0.0.1:5000 and in the bar menu click on 'weather'.
### API
Postman
```sh
GET 127.0.0.0:5000/weather/<string:city>/<string:code>
```