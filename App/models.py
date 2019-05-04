from App.ext import db


class User(db.Model):
    __table__name = 'user'
    id = db.Column(db.Integer,primary_key=True)
    userName = db.Column(db.String(50))
    sex = db.Column(db.String(50))
    password = db.Column(db.String(50))
    nickName = db.Column(db.String(50))
    location = db.Column(db.String(50))
    pic = db.Column(db.Text)
    type = db.Column(db.String(50))

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class Flight(db.Model):
    __table__name = 'flight'
    flightId = db.Column(db.Integer,primary_key=True)
    startingPlace = db.Column(db.String(50))
    endPlace = db.Column(db.String(50))
    startTime = db.Column(db.String(50))
    endTime = db.Column(db.String(50))
    flightNumber = db.Column(db.String(50))
    price = db.Column(db.String(50))
    flightName = db.Column(db.String(50))
    number = db.Column(db.Integer)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict




class Hotel(db.Model):
    __table__name = 'hotel'
    hotelId = db.Column(db.Integer,primary_key=True)
    hotelName = db.Column(db.String(50))
    price = db.Column(db.String(50))
    score = db.Column(db.String(50))
    number = db.Column(db.String(50))
    address = db.Column(db.String(50))
    introduction = db.Column(db.Text)
    pic = db.Column(db.Text)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict



class UserBuyRecord(db.Model):
    __table__name = 'userBuyRecord'
    Id = db.Column(db.Integer,primary_key=True)
    productId = db.Column(db.String(50))
    productType = db.Column(db.String(50))
    userName = db.Column(db.String(50))


    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
