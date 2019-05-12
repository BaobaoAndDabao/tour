from flask import Blueprint, request, jsonify, make_response, session

from App.common.ResData import ResData
from App.ext import db
from App.models import User, Coupon, UserBuyRecord

couponBlue = Blueprint("coupon", __name__)


def init_couponBlue(app):
    app.register_blueprint(blueprint=couponBlue)

#查询当前用户的优惠券列表
@couponBlue.route("/coupon/queryByUser", methods=["POST", "GET"])
def queryAll():
    userName = request.cookies.get('username')
    if(userName is None):
        return ResData.needLogin(userName)
    coupons = Coupon.query.filter(Coupon.username==userName).all()
    couponList = []
    for one in coupons:
        couponList.append(one.to_json())
    couponsJson = {"coupons": couponList}
    res = make_response(ResData.success(couponsJson))
    return res

#根据优惠券id查询优惠券详情
@couponBlue.route("/coupon/queryByCouponId", methods=["POST"])
def queryByCouponId():
    couponId = request.form.get('couponId')#优惠券Id
    coupon = Coupon.query.filter(Coupon.couponId==couponId).first()
    return ResData.success(coupon.to_json())


#获取分享的优惠券
@couponBlue.route("/coupon/getShareCoupon", methods=["POST"])
def search():
    userName = request.cookies.get('username')
    if(userName is None):
        return ResData.needLogin(userName)
    couponId = request.form.get('couponId')#优惠券Id
    coupon = Coupon.query.filter(Coupon.couponId == couponId).first()
    coupon.username=userName
    db.session.add(coupon)
    db.session.commit()
    res = make_response(ResData.success(""))
    return res




