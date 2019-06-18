import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, url_for, jsonify, request
from flask_socketio import SocketIO, emit
from flask_session import Session

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

app = Flask(__name__)
app.config["SECRET_KEY"] = 'tenthorflow'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
socketio = SocketIO(app)

# engine = create_engine(os.getenv("DATABASE_URL"))
engine = create_engine('sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db'))
db = scoped_session(sessionmaker(bind=engine))


@app.route('/')
def index():
    return render_template('bdwrite.html')

@socketio.on("submit vote")
def vote():
    num = 1
    arr = []
    f = open('1001.csv')
    reader = csv.reader(f)
    for line in reader:
        db.execute('INSERT INTO questions (question) VALUES (:line)', {'line': line[0]})
        emit("announce vote", {"num": num, "question": line}, broadcast=True)
        num+=1
    db.commit()
    questions = db.execute("SELECT question FROM questions").fetchall()
    for question in questions:
        arr.append(question[0])
    emit('questions', {'questions': arr}, broadcast=True)



#   SNIPPET FOR CAESH   #
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
#   SNIPPET FOR CAESH   #

if __name__ == "__main__":
    app.run(debug=True)