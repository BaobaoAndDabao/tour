from flask import Blueprint, request,jsonify,make_response,session

from App.common.ResData import ResData
from App.ext import db
from App.models import User, Landscape, UserBuyRecord

landscapeBlue =Blueprint("landscape",__name__)

def init_landscapeBlue(app):
    app.register_blueprint(blueprint=landscapeBlue)



@landscapeBlue.route("/landscape/search",methods=["POST"])
def search():
    address=request.form.get('address')
    landscapes=User.query.filter(Landscape.startingPlace==address).all()
    landscapeList=[]
    for one in landscapes:
        landscapeList.append(one.to_json())
    landscapesJson ={"landscapes":landscapeList}
    res= make_response(ResData.success(landscapesJson))
    return res

@landscapeBlue.route("/landscape/update",methods=["POST"])
def update():
    landscapeId=request.form.get("landscapeId")
    if(landscapeId is None):
        return ResData.paramEmpty(landscapeId)
    landscape=Landscape.query.filter(Landscape.landscapeId==landscapeId).first()

    address=request.form.get('address')
    landscapeName = request.form.get('landscapeName')
    price = request.form.get('price')
    score = request.form.get('score')
    Introduction = request.form.get('Introduction')
    pic = request.form.get('pic')

    landscape.address = address
    landscape.landscapeName = landscapeName
    landscape.price = price
    landscape.score = score
    landscape.Introduction = Introduction
    landscape.pic = pic

    db.session.add(landscape)
    db.session.commit()
    return ResData.success(None)



@landscapeBlue.route("/landscape/insert",methods=["POST"])
def insert():
    address=request.form.get('address')
    landscapeName = request.form.get('landscapeName')
    price = request.form.get('price')
    score = request.form.get('score')
    Introduction = request.form.get('Introduction')
    pic = request.form.get('pic')
    landscape=Landscape()
    landscape.address = address
    landscape.landscapeName = landscapeName
    landscape.price = price
    landscape.score = score
    landscape.Introduction = Introduction
    landscape.pic = pic
    db.session.add(landscape)
    db.session.commit()
    return ResData.success(None)


@landscapeBlue.route("/landscape/delete",methods=["POST"])
def delete():
    landscapeId=request.form.get('landscapeId')
    if(landscapeId is None):
        return ResData.paramEmpty(landscapeId)
    landscape=Landscape.query.filter(Landscape.landscapeId==landscapeId).first()
    db.session.delete(landscape)
    db.session.commit()
    return ResData.success(None)


@landscapeBlue.route("/landscape/buy",methods=["POST"])
def buy():
    userName = request.cookies.get('username')
    if(userName is None):
        return ResData.needLogin()
    landscapeId=request.form.get('landscapeId')
    if(landscapeId is None):
        return ResData.paramEmpty(landscapeId)
    landscape=Landscape.query.filter(Landscape.landscapeId==landscapeId).first()
    landscape.number=landscape.number - 1

    userBuyRecord=UserBuyRecord()
    userBuyRecord.productId =landscapeId
    userBuyRecord.productType ="landscape"
    userBuyRecord.userName = userName

    db.session.add(landscape)
    db.session.add(userBuyRecord)
    db.session.commit()
    return ResData.success(None)