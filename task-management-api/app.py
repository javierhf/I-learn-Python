# API Description  
# Create and API to manage student records (Create, Read, Update and Delete)

# import libraries, modules  
from flask import Flask, request 

# Define data structure    

tasks_list = [
    {
        "Id": "00001",
        "Summary": "Clean my room",
        "Description": "Sweeping, dusting and mopping my room"

    },
    {
        "Id": "00002",
        "summary": "Sort CDs",
        "description": "Sort CDs in TV room and aisle shelves"

    },
]

# Create Flask app  

app = Flask(__name__)

# Define endpoints and available methods    

# /TASKS
# GET all tasks  

@app.route('/tasks/', methods = ['GET'])

def all_tasks():
    return {'All Tasks': tasks_list}

# GET task by ID

@app.route('/tasks/<string:taskId>/', methods = ['GET'])

def get_taskById(taskId):
    for task in tasks_list:
        if task["Id"] == taskId:
            return task
    return{"Message": "Task not found in list"}, 404

# POST Add new task  

@app.route('/tasks/', methods = ['POST'])
def add_newTask():
    request_data = request.get_json()
    new_task = {
        "Id": request_data["Id"], 
        "Summary": request_data["Summary"], 
        "Description": request_data["Description"] 
        }
    tasks_list.append(new_task)

    return {"New task": new_task}, 201

# DELETE task by Id  

@app.route('/tasks/<string:taskId>/', methods = ['DELETE'])

def delete_taskById(taskId):
    for task in tasks_list:
        if task["Id"] == taskId:
            tasks_list.remove(task)
            return {"Message": "Task deleted"}, 200
    return {"Message": "Task not found"}, 404
    


