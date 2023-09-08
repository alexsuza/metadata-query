from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    salary = db.Column(db.Integer)
    currency = db.Column(db.String(10))
    responsibilities = db.Column(db.String(2000))
    requirements = db.Column(db.String(2000))
    date_posted = db.Column(db.Date)

@app.route('/')
def index():
    title_filter = request.args.get('title')
    if title_filter:
        jobs = Job.query.filter(Job.title.ilike(f"%{title_filter}%")).all()
    else:
        jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
