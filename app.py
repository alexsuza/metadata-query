import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#migrate = Migrate(app, db)



class VProduct(db.Model):
    __tablename__ = 'V_PRODUCT'
    
    PROD_ID = db.Column(db.Numeric(38, 0), primary_key=True)
    PARENT_PROD_ID = db.Column(db.Numeric(38, 0))
    JNLITM_ID = db.Column(db.Numeric(38, 0))
    TASK_ID = db.Column(db.Numeric(38, 0))
    STRINGOFORIGIN = db.Column(db.String(16))
    PRODUCTSTART_DTM = db.Column(db.DateTime)
    PRODUCTEND_DTM = db.Column(db.DateTime)
    GROUNDSTATION = db.Column(db.String(32))
    CLASSMARK = db.Column(db.String(32))
    CONTROLMARK = db.Column(db.String(64))
    PRODTYPE = db.Column(db.String(3))
    TFRITM_ID = db.Column(db.Numeric(38, 0))
    FILESIZE = db.Column(db.Numeric(38, 0))
    CLASSIFICATION = db.Column(db.String(128))
    TAGS = db.Column(db.Text)
    FILENAME = db.Column(db.String(128))
    FILEPATH = db.Column(db.String(256))
    PAYLOADNUMBER = db.Column(db.String(32))
    PAYLOADENV = db.Column(db.String(32))
    CORRELATED = db.Column(db.String(1))
    CURRENT_STRINGLOC = db.Column(db.String(5))
    ORIGINATING_STRINGLOC = db.Column(db.String(5))
    ORIGINATING_DATASOURCE = db.Column(db.String(8))
    CURRENT_DATASOURCE = db.Column(db.String(8))
    ON_DISK = db.Column(db.String(1))
    ON_TAPE = db.Column(db.String(1))
    CURRENT_ENTITYLOC = db.Column(db.String(32))
    DEMO_PRODUCT_FLAG = db.Column(db.String(1))
    DO_NOT_DELETE_FLAG = db.Column(db.String(1))
    NOTETEXT = db.Column(db.Text)
    PRODUCT_INSERT_DTM = db.Column(db.DateTime)
    PRODUCT_SUBTYPE = db.Column(db.String(32))
    STORED_FROM = db.Column(db.String(10))
    TASKNAME_FROMFILE = db.Column(db.String(120))
    COMPRESSION_RATIO = db.Column(db.Numeric(38, 0))
    OUTSTANDING_AUTOXFER = db.Column(db.String(256))
    AUTOXFEREND_DTM = db.Column(db.DateTime)
    SWVERSION = db.Column(db.String(32))
    PAYLOADID = db.Column(db.String(32))
    ORIGINATING_FILENAME = db.Column(db.String(128))
    UPDATED_DTM = db.Column(db.DateTime)
    EM_DETECT_ID = db.Column(db.String(128))
    PRIORITY = db.Column(db.Numeric(38, 0))

@app.route('/')
def index():
    query = db.session.query(VProduct)
    
    for column_name in VProduct.__table__.columns.keys():
        column_value = request.args.get(column_name)
        
        if column_value:
            if isinstance(VProduct.__table__.columns[column_name].type, db.DateTime):
                try:
                    dtm = datetime.strptime(column_value, '%Y-%m-%d %H:%M:%S')
                    query = query.filter(getattr(VProduct, column_name) == dtm)
                except ValueError:
                    return f"Invalid date format for {column_name}, use 'YYYY-MM-DD HH:MM:SS'"
            else:
                query = query.filter(getattr(VProduct, column_name) == column_value)
                
    products = query.all()
    return render_template('index.html', products=products)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
