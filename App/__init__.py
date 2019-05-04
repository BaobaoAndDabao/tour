from flask import Flask

from App.FlightApi import init_flightBlue
from App.api import init_blue
from App.ext import init_ext
from App.settings import envs


def create_app():
    app = Flask(__name__)

    app.config.from_object(envs.get('dev'))

    init_blue(app)
    init_flightBlue(app)

    init_ext(app)

    return app

