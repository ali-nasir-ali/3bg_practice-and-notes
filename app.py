
from flask import Flask, render_template
from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db' # with 3 /// its relaytive path with 4 its absoluite path
db = SQLALchemy(app) # initialize databse

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    Look
