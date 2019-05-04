from App.ext import db
from App.models import User, Flight, UserBuyRecord
from flask import Blueprint, request,jsonify,make_response,session,render_template

webBlue = Blueprint("web", __name__)

def init_webBlue(app):
    app.register_blueprint(blueprint=webBlue)


@webBlue.route('/login.html')
def index():
    return render_template('login.html')
