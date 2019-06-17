import os

from flask import Flask, render_template, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

#контекст оболочки flask shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Users': Users, 'Questions': Questions, 'Answers': Answers}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-questions')
def getQuestions():
    resp = Questions.query.all()
    questions = []
    for item in resp:
        questions.append(item.question)
    return jsonify(questions)




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
    # app.run()