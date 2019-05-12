from flask import Blueprint, request,jsonify,make_response,session

from App.Utils import Utils
from App.common.ResData import ResData
from App.ext import db
from App.models import User, PostRecord, UserBuyRecord,Reply

postRecordBlue =Blueprint("postRecord",__name__)

def init_postRecordBlue(app):
    app.register_blueprint(blueprint=postRecordBlue)

#查看帖子列表
@postRecordBlue.route("/postRecord/queryAll", methods=["POST", "GET"])
def queryAll():
    postRecords = PostRecord.query.all()
    postRecordList = []
    for one in postRecords:
        count=querReplyCountByPostRecordId(one.postId)
        post=one.to_json()
        post['replyCount']=count
        postRecordList.append(post)
    postRecordsJson = {"postRecords": postRecordList}
    res = make_response(ResData.success(postRecordsJson))
    return res


def querReplyByPostRecordId(postId):
    replys = Reply.query.filter(Reply.replyPostId == postId).all()
    return replys

def querReplyCountByPostRecordId(postId):
    count = Reply.query.filter(Reply.replyPostId == postId).count()
    return count
#查看一个贴子全部内容
@postRecordBlue.route("/postRecord/queryByPostRecordId",methods=["POST"])
def queryByPostRecordId():
    postRecordId = request.form.get('postRecordId')
    if(postRecordId is None):
        return ResData.paramEmpty(postRecordId)
    postRecord = PostRecord.query.filter(PostRecord.postId == postRecordId).first()
    res=postRecord.to_json()
    replys=querReplyByPostRecordId(postRecordId)
    postRecordList=[]
    for one in replys:
        postRecordList.append(one.to_json())
    res["postRecords"]=postRecordList
    return make_response(ResData.success(res))

#发帖
@postRecordBlue.route("/postRecord/insert",methods=["POST"])
def insert():
    userName = request.cookies.get('userName')
    if(userName is None):
        return ResData.needLogin(userName)
    postContent=request.form.get('postContent')
    postTitle = request.form.get('postTitle')
    postPic = request.form.get('postPic')

    postRecord=PostRecord()
    postRecord.postContent = postContent
    postRecord.postTitle = postTitle
    postRecord.postPic = postPic
    postRecord.postBy = userName
    postRecord.postTime = Utils.getCurrentTimeStr("")
    db.session.add(postRecord)
    db.session.commit()
    return ResData.success(None)

#删帖
@postRecordBlue.route("/postRecord/delete",methods=["POST"])
def delete():
    postRecordId=request.form.get('postRecordId')
    if(postRecordId is None):
        return ResData.paramEmpty(postRecordId)
    postRecord=PostRecord.query.filter(PostRecord.postId==postRecordId).first()
    db.session.delete(postRecord)
    db.session.commit()
    return ResData.success(None)

#回复帖子
@postRecordBlue.route("/postRecord/reply",methods=["POST"])
def reply():
    userName = request.cookies.get('username')
    if(userName is None):
        return ResData.needLogin(userName)

    replyContent=request.form.get('replyContent')#回复内容
    replyPostId = request.form.get('replyPostId')#回复帖子的id
    postPic = request.form.get('postPic')#回复的图片
    replyTime = Utils.getCurrentTimeStr("")

    reply=Reply()
    reply.replyBy = userName
    reply.replyContent = replyContent
    reply.replyPostId = replyPostId
    reply.postPic = postPic
    reply.replyTime = replyTime
    db.session.add(reply)
    db.session.commit()
    return ResData.success(None)

