from flask import Blueprint, request, jsonify

from exts import db
from models.Task import Task, TaskSchema

taskApi = Blueprint('taskApi',__name__)

# Declare Schema
taskSchema = TaskSchema()
tasksSchema = TaskSchema(many=True)         


# REST APIs
@taskApi.route('',methods=['POST'])
def addTask():
    name = request.json['name']
    userId = request.headers['userId']
    newTask = Task(name,userId)
    db.session.add(newTask)
    db.session.commit() 
    return taskSchema.jsonify(newTask)  

@taskApi.route('',methods=['GET'])
def getTasks():
    allTasks = Task.query.all()
    result = tasksSchema.dump(allTasks)
    return jsonify(result)       

@taskApi.route('/<id>',methods=['GET'])
def getTaskById(id):
    task = Task.query.get(id)
    # db.session.delete(task)
    # db.session.commit()
    return taskSchema.jsonify(task)

@taskApi.route('/<id>',methods=['PUT'])
def updateTask(id):
    task = Task.query.get(id)
    task.setName(request.json['name'])
    db.session.add(task)
    db.session.commit()
    return taskSchema.jsonify(task)

@taskApi.route('/<id>/done',methods=['PATCH'])
def markTaskAsDone(id):
    task = Task.query.get(id)
    task.setDone(True)
    db.session.add(task)
    db.session.commit()
    return taskSchema.jsonify(task)    