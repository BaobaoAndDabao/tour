from flask import Blueprint, request, jsonify, make_response, session

from App.common.ResData import ResData
from App.ext import db
from App.models import User, Flight, UserBuyRecord, Landscape, Hotel
# from support import support

recommendBlue = Blueprint("recommend", __name__)


def init_recommendBlue(app):
    app.register_blueprint(blueprint=recommendBlue)


@recommendBlue.route("/recommend/test", methods=["POST", "GET"])
def test():
    return 'success'


def isSameLocation(location1, location2):
  return location1 == location2

# 根据用户的登录信息推荐
@recommendBlue.route("/recommend/send", methods=["POST", "GET"])
def send():
  username = request.cookies.get('userName')
  user = User.query.filter(User.userName == username).first()
  userlocation = user.location.split('-', 2)
  landscapes = Landscape.query.filter().all()
  landscapeslist = []
  for one in landscapes:
    addresslist = one.address.split('-', 2)
    if (addresslist[0] == userlocation[0] and addresslist[1] == userlocation[1]):
      landscapeslist.append(one.to_json())
  landscapesJson = {"landscapes": landscapeslist}
  return make_response(ResData.success(landscapesJson))


@recommendBlue.route("/recommend/raiders", methods=["POST", "GET"])
def raiders():
  username = request.cookies.get('userName')
  user = User.query.filter(User.userName == username).first()
  userlocation = user.location.split('-', 2)
  landscapes = Landscape.query.filter().all()
  landscapeslist = []
  for one in landscapes:
    addresslist = one.address.split('-', 2)
    if (addresslist[0] == userlocation[0] and addresslist[1] == userlocation[1]):
      landscapeslist.append(one.to_json())

  flights = Flight.query.filter().all()
  flightList = []
  for one in flights:
    endPlacelist = one.endPlace.split('-', 2)
    if (endPlacelist[0] == userlocation[0] and endPlacelist[1] == userlocation[1]):
      flightList.append(one.to_json())

  hotels = Hotel.query.filter().all()
  hotellist = []
  for one in hotels:
    addresslist = one.address.split('-', 2)
    if (addresslist[0] == userlocation[0] and addresslist[1] == userlocation[1]):
      hotellist.append(one.to_json())

  resultJson = {
    "landscapes": landscapeslist,
    "flights": flightList,
    "hotels": hotellist
  }
  return make_response(ResData.success(resultJson))
