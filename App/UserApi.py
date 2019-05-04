from flask import Blueprint, request,jsonify,make_response,session

from App.common.ResData import ResData
from App.ext import db
from App.models import User

blue =Blueprint("user",__name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route("/user/login",methods=["POST"])
def login():
    userName=request.form.get('userName')
    password=request.form.get('password')
    user=User.query.filter(User.userName==userName,User.password==password).first()
    if(user is None):
        return ResData.fail()
    res= make_response(ResData.success(user.to_json()))
    res.set_cookie('userName', userName)
    return res
    #return ResData.success(user.to_json())

    #return  jsonify(u.to_json())

@blue.route("/user/update",methods=["POST"])
def update():
    userName=request.cookies.get('username')
    #userName=request.form.get('userName')
    password=request.form.get('password')
    nickName = request.form.get('nickName')
    sex = request.form.get('sex')
    location = request.form.get('location')
    pic = request.form.get('pic')
    type = request.form.get('type')

    user=User.query.filter(User.userName==userName).first()
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









