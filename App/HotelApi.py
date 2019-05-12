from flask import Blueprint, request,jsonify,make_response,session

from App.common.ResData import ResData
from App.ext import db
from App.models import User, Flight, Hotel

hotelBlue =Blueprint("hotel",__name__)

def init_hotelBlue(app):
    app.register_blueprint(blueprint=hotelBlue)


@hotelBlue.route("/hotel/queryAll", methods=["POST", "GET"])
def queryAll():
    hotels = Hotel.query.filter().all()
    hotellist = []
    for one in hotels:
        hotellist.append(one.to_json())
    flightsJson = {"hotels": hotellist}
    res = make_response(ResData.success(flightsJson))
    return res

@hotelBlue.route("/hotel/search",methods=["POST"])
def search():
    address=request.form.get('address')
    hotels=Hotel.query.filter(Hotel.address==address).all()
    flightList=[]
    for one in hotels:
        flightList.append(one.to_json())
    flightsJson ={"hotels":flightList}
    res= make_response(ResData.success(flightsJson))
    return res

@hotelBlue.route("/hotel/update",methods=["POST"])
def update():
    hotelId=request.form.get("hotelId")
    if(hotelId is None):
        return ResData.paramEmpty(hotelId)
    hotel=Hotel.query.filter(Hotel.hotelId==hotelId).first()

    address=request.form.get('address')
    hotelName = request.form.get('hotelName')
    price = request.form.get('price')
    score = request.form.get('score')
    number = request.form.get('number')
    hotelId = request.form.get('hotelId')
    introduction = request.form.get('introduction')
    pic = request.form.get('pic')

    hotel.address = address
    hotel.hotelName = hotelName
    hotel.price = price
    hotel.score = score
    hotel.number = number
    hotel.hotelId = hotelId
    hotel.introduction = introduction
    hotel.pic = pic

    db.session.add(hotel)
    db.session.commit()
    return ResData.success(None)



@hotelBlue.route("/hotel/insert",methods=["POST"])
def insert():
    address=request.form.get('address')
    hotelName = request.form.get('hotelName')
    price = request.form.get('price')
    score = request.form.get('score')
    number = request.form.get('number')
    introduction = request.form.get('introduction')
    pic = request.form.get('pic')
    hotel=Hotel()
    hotel.address = address
    hotel.hotelName = hotelName
    hotel.price = price
    hotel.score = score
    hotel.number = number
    hotel.introduction = introduction
    hotel.pic = pic
    db.session.add(hotel)
    db.session.commit()
    return ResData.success(None)


@hotelBlue.route("/hotel/delete",methods=["POST"])
def delete():
    hotelId=request.form.get('hotelId')
    if(hotelId is None):
        return ResData.paramEmpty(hotelId)
    hotel=Hotel.query.filter(Hotel.hotelId==hotelId).first()
    db.session.delete(hotel)
    db.session.commit()
    return ResData.success(None)



@hotelBlue.route("/hotel/buy",methods=["POST"])
def buy():
    userName = request.cookies.get('username')
    if(userName is None):
        return ResData.needLogin(userName)
        hotelId=request.form.get('hotelId')
    if(hotelId is None):
        return ResData.paramEmpty(hotelId)
    hotel=Hotel.query.filter(Hotel.hotelId==hotelId).first()
    Hotel.number=Hotel.number - 1

    userBuyRecord= UserBuyRecord()
    userBuyRecord.productId =hotelId
    userBuyRecord.productType ="hotel"
    userBuyRecord.userName = userName

    db.session.add(hotel)
    db.session.add(userBuyRecord)
    db.session.commit()
    return ResData.success(None)
