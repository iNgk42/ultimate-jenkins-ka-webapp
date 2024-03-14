from init_app import app
from flask import render_template, request
from models import Task
from database import task_store

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register-task", methods=['GET', 'POST'])
def register_new_task():
    if request.method == "POST":
        #get form data
        task_id = request.form["task_id"]
        task_title = request.form["task_title"]
        task_description = request.form["task_description"]
        task_due_date = request.form["task_due_date"]
        task_registration_date = request.form["task_registration_date"]

        #create new task object
        task = Task(task_id, task_title, task_description, task_due_date, task_registration_date)

        #save data to database
        task.register()
        
        #redirect to confirmation page
    else:
        return render_template("register-task.html")