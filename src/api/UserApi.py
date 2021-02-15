from flask import Blueprint, request, jsonify

from exts import db
from models.User import User, UserSchema

userApi = Blueprint('userApi',__name__)

# Declare Schema
userSchema = UserSchema()
usersSchema = UserSchema(many=True)

# REST APIs
@userApi.route('',methods=['POST'])
def addUser():
    username = request.json['username']
    newUser = User(username)
    db.session.add(newUser)
    db.session.commit() 
    return userSchema.jsonify(newUser)

@userApi.route('',methods=['GET'])
def getAllUsers():
    allUsers = User.query.all()
    return usersSchema.jsonify(allUsers)    

@userApi.route('/<id>',methods=['GET'])
def getUserById(id):
    user = User.query.get(id)
    return userSchema.jsonify(user)

@userApi.route('/<id>',methods=['PUT'])
def updateUserById(id):
    username = request.json['username']
    user = User.query.get(id)
    user.setUsername(username)
    db.session.add(user)
    db.session.commit() 
    return userSchema.jsonify(user)
