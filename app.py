from flask import Flask, render_template, redirect, request
from flask_scss import Scss 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

#my app setup
app = Flask(__name__)
os.makedirs(app.instance_path, exist_ok=True)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(app.instance_path, "mydatabase.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
# create a model for the database (row of data)
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__ (self) -> str:
        return f"Task {self.id}"

with app.app_context():
    db.create_all() 
# routes to webpage
@app.route("/", methods=['POST', 'GET'])
def index():
# add a task 
    if request.method == 'POST':
        current_task = request.form['content']
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')  # update home page
        except Exception as e: #catches error and stores it in 'e'
            print(f"ERROR: {e}")
            return f"ERROR: {e}"

    # see all current tasks
    else:
        tasks = MyTask.query.order_by(MyTask.created).all() # order by created date
        return render_template('index.html', tasks=tasks) # pass tasks to index.html


# delete a task 
#ex: https://www.home.com/delete
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id) # get task by id, if not found return 404 error
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"ERROR: {e}"
    

# update a task 
@app.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id:int):
    update_task = MyTask.query.get_or_404(id)
    if request.method == 'POST':
        update_task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"ERROR: {e}" 
    else:
        return render_template('update.html', task=update_task)

# runner and debugger 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)