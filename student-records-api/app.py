# API Description  
# Create and API to manage student records (Create, Read, Update and Delete)

# import libraries, modules  
from flask import Flask, request 

# Define data structure    

students = [
    {
        "id": "00001",
        "name": "John",
        "surname": "Miles",
        "class": "Architecture",
        "type": "major",
        "average grade": 6.7

    }
]

# Create Flask app  
app = Flask(__name__)

# Define endpoints and available methods  (Add, view, update delete)
# /students GET all students
@app.route('/students/', methods = ['GET'])
def get_all_students():
    return {"Students": students}

# /students/{studentId} GET student by ID
@app.route('/students/<string:id>', methods = ['GET'])
def func_name(id):
    for student in students:
        if student["id"] == id:
            return {"Student": student}
    return {"Message": "Student not found"}, 404

# /students POST Add new student
@app.route('/students/', methods = ['POST'])
def add_new_student():
    request_data = request.get_json()
    new_student = {
        "id": request_data["id"],
        "name": request_data["name"],
        "class": request_data["class"],
        "surname": request_data["surname"],
        "average grade": request_data["average grade"],
        "type": request_data["type"]
    }
    students.append(new_student)
    return {"Students": students}, 201

# /students/<string:id> PUT Update student by id
@app.route('/students/<string:id>', methods = ['PUT'])
def udpate_student_byId(id):
    request_data = request.get_json()
    for student in students:
        if student["id"] == id:
            student["average grade"] = request_data["average grade"]
            
            return {"Student updated": student}
    
    return {"Students": "Student not found"}, 404

# /students/<string:id> DELETE Remove student by id
@app.route('/students/<string:id>', methods = ['DELETE'])
def delete_student_byId(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return {"Students": "User deleted succesfully"}, 200
    
    return {"Students": "User not found"}, 404








