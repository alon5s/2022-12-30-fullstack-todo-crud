from flask import Flask, render_template, request, redirect, url_for
import crud
from classes import Task

app = Flask(__name__)

def db():
    tasks=[]
    tasks_from_db=crud.read()
    for tid,name,desc,date in tasks_from_db:
        task=Task(tid, name, desc, date)
        tasks.append(task)
    return tasks

@app.route('/', methods=['GET'])
def home():
    if request.method=='GET':
        tasks = db()
        return render_template("index.html", tasks=tasks)

@app.route('/update', methods=['GET'])
def update():
    if request.method=='GET':
        tasks = db()
    return render_template("update.html", tasks=tasks)

@app.route('/update_task/<task_id>', methods=['GET','POST'])
def update_task(task_id):
    if request.method == 'GET':
        task_from_db=crud.read_id(task_id)
        for tid,name,description,date in task_from_db:
            task=Task(tid, name, description, date)
        return render_template("update_task.html",task=task)
    if request.method == 'POST':
        category = request.form["category"]
        date_time = request.form["date_time"]
        desc = request.form["desc"]
        crud.update_description(category, desc, date_time, task_id)
        return redirect(url_for("update"))

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == "POST":
        category = request.form.get('category', None)
        date_time = request.form.get('date_time', None)
        desc = request.form.get('desc', None)
        crud.insert(category, desc, date_time)
    return render_template("add.html")

@app.route('/delete', methods=['POST'])
def del_task():
    task_id = request.form["task_id"]
    crud.delete(task_id)
    return redirect(url_for("home"))