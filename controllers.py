from flask import Flask, render_template, request, flash, redirect, url_for
from models import Task

app = Flask(__name__)
app.config['SECRET_KEY'] = 'azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register-task", methods=['GET', 'POST'])
def register_new_task():
    if request.method == "POST":
        #get form data
        task_title = request.form["task_title"]
        task_description = request.form["task_description"]
        task_due_date = request.form["task_due_date"]

        print("format de la date", task_due_date)

        #create new task object
        task = Task('taskID', task_title, task_description, task_due_date, 'taskRegistrationDate')

        #save data to database
        task.register()
        
        #redirect to confirmation page
        flash("Your task have been successfully registered !", "message")
        return redirect(url_for("home"))
    else:
        return render_template("register-task.html")