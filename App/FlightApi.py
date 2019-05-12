from flask import Blueprint, request, jsonify, make_response, session
import os
from App.common.ResData import ResData
from App.ext import db
from App.models import User, Flight, UserBuyRecord

flightBlue = Blueprint("flight", __name__)


def init_flightBlue(app):
    app.register_blueprint(blueprint=flightBlue)


@flightBlue.route("/flight/createTable", methods=["POST", "GET"])
def createTable():
    db.drop_all()
    db.create_all()
    return "sec"


@flightBlue.route("/flight/queryAll", methods=["POST", "GET"])
def queryAll():
    flights = Flight.query.filter().all()
    flightList = []
    for one in flights:
        flightList.append(one.to_json())
    flightsJson = {"flights": flightList}
    res = make_response(ResData.success(flightsJson))
    return res


@flightBlue.route("/flight/search", methods=["POST"])
def search():
    startingPlace = request.form.get('startingPlace')
    endPlace = request.form.get('endPlace')
    startTime = request.form.get('startTime')
    flights = Flight.query.filter(Flight.startingPlace == startingPlace,
                                  Flight.endPlace == endPlace, Flight.startTime == startTime).all()
    flightList = []
    for one in flights:
        flightList.append(one.to_json())
    flightsJson = {"flights": flightList}
    res = make_response(ResData.success(flightsJson))
    return res


@flightBlue.route("/flight/update", methods=["POST"])
def update():
    flightId = request.form.get("flightId")
    if(flightId is None):
        return ResData.paramEmpty(flightId)
    flight = Flight.query.filter(Flight.flightId == flightId).first()

    startingPlace = request.form.get('startingPlace')
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


@flightBlue.route("/flight/insert", methods=["POST"])
def insert():
    startingPlace = request.form.get('startingPlace')
    endPlace = request.form.get('endPlace')
    startTime = request.form.get('startTime')
    endTime = request.form.get('endTime')
    flightNumber = request.form.get('flightNumber')
    price = request.form.get('price')
    flightName = request.form.get('flightName')
    number = request.form.get('number')
    flight = Flight()
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


@flightBlue.route("/flight/delete", methods=["POST"])
def delete():
    flightId = request.form.get('flightId')
    if(flightId is None):
        return ResData.paramEmpty(flightId)
    flight = Flight.query.filter(Flight.flightId == flightId).first()
    db.session.delete(flight)
    db.session.commit()
    return ResData.success(None)


@flightBlue.route("/flight/buy", methods=["POST"])
def buy():
    flightId = request.form.get('flightId')
    userName = request.cookies.get('username')
    if(userName is None):
        return ResData.needLogin(flightId)
    if(flightId is None):
        return ResData.paramEmpty(flightId)
    flight = Flight.query.filter(Flight.flightId == flightId).first()
    flight.number = flight.number - 1

    userBuyRecord = UserBuyRecord()
    userBuyRecord.productId = flightId
    userBuyRecord.productType = "flight"
    userBuyRecord.userName = userName

    db.session.add(flight)
    db.session.add(userBuyRecord)
    db.session.commit()
    return ResData.success(None)

@flightBlue.route("/flight/initSql", methods=["POST"])
def initSql():
    PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
    p=os.path.realpath(__file__)
    cur_path = os.path.dirname(os.path.realpath(__file__))
    print(cur_path)
    path=cur_path +'\sql\init.sql'
    f = open(path,"r",encoding='UTF-8')
    txt=f.read()
    sql ="INSERT INTO `post_record` (`postBy`, `postContent`, `postTitle`, `postTime`, `postPic`) VALUES ('admin', '官方网址：http://yuilibrary.com/YUI Editor 是雅虎的 YUI 包中的一个可视化HTML编辑器组件。', '土耳其三日游', '2019-05-12 14:45:01', NULL);"
    data_query = db.session.execute(sql)
    db.session.commit()
    return ResData.success(None)