from flask import Blueprint, request,jsonify,make_response,session

from App.common.ResData import ResData
from App.ext import db
from App.models import User, Flight, UserBuyRecord

flightBlue =Blueprint("flight",__name__)

def init_flightBlue(app):
    app.register_blueprint(blueprint=flightBlue)


@flightBlue.route("/flight/createTable",methods=["POST"])
def createTable():
    db.drop_all()
    db.create_all()
    return "sec"

@flightBlue.route("/flight/search",methods=["POST"])
def search():
    startingPlace=request.form.get('startingPlace')
    endPlace=request.form.get('endPlace')
    startTime = request.form.get('startTime')
    flights = Flight.query.filter(Flight.startingPlace == startingPlace,
                                  Flight.endPlace == endPlace, Flight.startTime == startTime).all()
    flightList=[]
    for one in flights:
        flightList.append(one.to_json())
    flightsJson ={"flights":flightList}
    res= make_response(ResData.success(flightsJson))
    return res

@flightBlue.route("/flight/update",methods=["POST"])
def update():
    flightId=request.form.get("flightId")
    if(flightId is None):
        return ResData.paramEmpty(flightId)
    flight=Flight.query.filter(Flight.flightId==flightId).first()

    startingPlace=request.form.get('startingPlace')
    endPlace = request.form.get('endPlace')
    startTime = request.form.get('startTime')
    endTime = request.form.get('endTime')
    flightNumber = request.form.get('flightNumber')
    price = request.form.get('price')
    flightName = request.form.get('flightName')
    number = request.form.get('number')

    flight.startingPlace = startingPlace
    flight.endPlace = endPlace
    flight.startTime = startTime
    flight.endTime = endTime
    flight.flightNumber = flightNumber
    flight.price = price
    flight.flightName = flightName
    flight.number = number

    db.session.add(flight)
    db.session.commit()
    return ResData.success(None)



@flightBlue.route("/flight/insert",methods=["POST"])
def insert():
    startingPlace=request.form.get('startingPlace')
    endPlace = request.form.get('endPlace')
    startTime = request.form.get('startTime')
    endTime = request.form.get('endTime')
    flightNumber = request.form.get('flightNumber')
    price = request.form.get('price')
    flightName = request.form.get('flightName')
    number = request.form.get('number')
    flight=Flight()
    flight.startingPlace = startingPlace
    flight.endPlace = endPlace
    flight.startTime = startTime
    flight.endTime = endTime
    flight.flightNumber = flightNumber
    flight.price = price
    flight.flightName = flightName
    flight.number = number
    db.session.add(flight)
    db.session.commit()
    return ResData.success(None)


@flightBlue.route("/flight/delete",methods=["POST"])
def delete():
    flightId=request.form.get('flightId')
    if(flightId is None):
        return ResData.paramEmpty(flightId)
    flight=Flight.query.filter(Flight.flightId==flightId).first()
    db.session.delete(flight)
    db.session.commit()
    return ResData.success(None)


@flightBlue.route("/flight/buy",methods=["POST"])
def buy():
    userName = request.cookies.get('username')
    if(userName is None):
        return ResData.needLogin()
    flightId=request.form.get('flightId')
    if(flightId is None):
        return ResData.paramEmpty(flightId)
    flight=Flight.query.filter(Flight.flightId==flightId).first()
    flight.number=flight.number - 1

    userBuyRecord=UserBuyRecord()
    userBuyRecord.productId =flightId
    userBuyRecord.productType ="flight"
    userBuyRecord.userName = userName

    db.session.add(flight)
    db.session.add(userBuyRecord)
    db.session.commit()
    return ResData.success(None)
