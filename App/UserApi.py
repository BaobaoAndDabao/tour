from flask import Blueprint, request,jsonify,make_response,session

from App.common.ResData import ResData
from App.ext import db
from App.models import User,Landscape,Flight,Hotel,UserBuyRecord
import  operator

blue =Blueprint("user",__name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route("/user/login",methods=["POST"])
def login():
    userName=request.form.get('userName')
    password=request.form.get('password')
    user=User.query.filter(User.userName==userName,User.password==password).first()
    if(user is None):
        return ResData.fail(userName)
    res= make_response(ResData.success(user.to_json()))
    res.set_cookie('username', userName)
    return res
    #return ResData.success(user.to_json())

    #return  jsonify(u.to_json())

@blue.route("/user/update",methods=["POST"])
def update():
    userName = request.cookies.get('username')
    #userName=request.form.get('userName')
    password = request.form.get('password')
    nickName = request.form.get('nickName')
    sex = request.form.get('sex')
    location = request.form.get('location')
    pic = request.form.get('pic')
    type = request.form.get('type')

    user=User.query.filter(User.userName==userName).first()
    if (user is None):
        return ResData.fail()
    if(password is not None):
        user.password = password
    if (nickName is not None):
        user.nickName = nickName
    if (sex is not None):
        user.sex = sex
    if (location is not None):
        user.location = location
    if (pic is not None):
        user.pic = pic
    if (type is not None):
        user.type = type
    db.session.add(user)
    db.session.commit()
    return ResData.success(None)


@blue.route("/user/queryUserBuyRecord", methods=["POST", "GET"])
def queryUserBuyRecord():
  username = request.cookies.get('username')
  userBuyRecords=UserBuyRecord.query.filter(UserBuyRecord.userName ==username ).all()
  hotelList = []
  landscapeList = []
  flightList = []
  for userBuyRecord in  userBuyRecords:
      if(operator.eq(userBuyRecord.productType,'hotel') ):
          hotels = Hotel.query.filter(Hotel.hotelId == userBuyRecord.productId).all()
          for hotel in hotels:
              hotelList.append(hotel.to_json())
      if(operator.eq(userBuyRecord.productType,'landscape') ):
          landscapes = Landscape.query.filter(Landscape.landscapeId == userBuyRecord.productId).all()
          for landscape in landscapes:
              landscapeList.append(landscape.to_json())
      if(operator.eq(userBuyRecord.productType,'flight') ):
          flights = Flight.query.filter(Flight.flightId == userBuyRecord.productId).all()
          for flight in flights:
              flightList.append(flight.to_json())
  resultJson = {
    "landscapes": landscapeList,
    "flights": flightList,
    "hotels": hotelList
  }
  return make_response(ResData.success(resultJson))






