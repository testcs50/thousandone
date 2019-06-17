from app import db

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False, index=True)
    answers = db.relationship('Answers', backref='question', lazy=True)

    def __repr__(self):
        return f'{self.question}'

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    answers = db.relationship('Answers', backref='author', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

