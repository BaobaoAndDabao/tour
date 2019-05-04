from flask import Flask

from App.FlightApi import init_flightBlue
from App.HotelApi import init_hotelBlue
from App.web import init_webBlue
from App.LandscapeApi import init_landscapeBlue
from App.UserApi import init_blue
from App.ext import init_ext
from App.settings import envs


def create_app():
    app = Flask(__name__)

    app.config.from_object(envs.get('dev'))

    init_blue(app)
    init_flightBlue(app)
    init_hotelBlue(app)
    init_webBlue(app)
    init_landscapeBlue(app)

    init_ext(app)

    return app

