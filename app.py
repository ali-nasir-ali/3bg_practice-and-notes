
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db' # with 3 /// its relaytive path with 4 its absoluite path

db = SQLAlchemy(app) # initialize databse

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)

def init_db():
    """For use on command line for setting up
    the database.
    """

    db.drop_all()
    db.create_all()
    db.session.commit()


# NOTE: this is all the way at the bottom so we can use init_db!
def database_make():
 if app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:":
    # Use memory SQLITE database! Meaning the HDD is never touched!
    # Since this database will be in the memory, we have to create
    # it at the beginning of every app run.
    init_db()

if __name__ == '__main__':

    database_make()

    app.run(debug=True)
    # app.run(debug=True, port=<desired port>) # if want on different port
