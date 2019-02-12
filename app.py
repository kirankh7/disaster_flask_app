from flask import Flask,render_template,request
from datetime import datetime
import pytz
from flask_sqlalchemy import SQLAlchemy




# Creating an instance of the Flask
app = Flask(__name__)


#DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
#database settings
app.config.update(
    SECRET_KEY= 'Avankia1',
    SQLALCHEMY_DATABASE_URI='postgresql://rooter:Avankia1@kiran-db.c09ylvqoqhhn.eu-west-1.rds.amazonaws.com/flaskdb',
    SQLALCHEMY_TRACK_MODIFICATIONS=True
)

# pass db instance
db = SQLAlchemy(app)


# First / root of the flask app
@app.route('/index.html') # same hello_world
@app.route('/')
def hello_world():
    message = "Hello World!  {}".format(get_pst_time())
    image_src = "https://s3.amazonaws.com/kiran-test-2/cruiser80.jpg"

    return render_template("index.html",
                           src_hello=message,
                           image_name=image_src
                           )
    # return message


def get_pst_time():
    # date_format = '%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(pytz.timezone('US/Pacific'))
    return str(date) + " PST"

# pass some values
@app.route('/surnames/')
def get_surname(surname="Enter Name=Some Name"):
    query_val = request.args.get("Name", surname)
    get_surname = query_val.split()
    return '<p>Name Is : {}<p/>'.format("".join(get_surname[1:]))

# This route must print database connetion
# Check Connection Auth in infinete While loop & sleep for 5 minute
# Configure db config using chef
# SQLAlchemy
@app.route('/health')
def health_rds():
    return "OK"

# '/diag' must print
# 1. Number of instance in the region
# 2. Version from the Nginx(Configure something into setting with using chef)
# 3. Health of each instance name: try to get instance IP get /health


@app.route('/diag')
def status_cheker():
    return "OK"

class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'The id is {}, Name is is {}'.format(self.id, self.name)

# db.create_all()
# Run the file direct... do not import to anything else
if __name__ == '__main__':
    print("Kiran")
    db.create_all()
    app.run(host='0.0.0.0', port=8080)
