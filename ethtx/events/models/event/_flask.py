from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
db = SQLAlchemy(app)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    object_key = db.Column(db.Integer, nullable=False, index=True)
    object_verb = db.Column(db.String)
    object_name = db.Column(db.String, index=True)

    event_priority = db.Column(db.Integer, db.ForeignKey("priority.id"))
    priority = db.relationship("Priority", backref="event")

    event_time = db.Column(db.DateTime)

    event_status = db.Column(db.Integer, db.ForeignKey("status.id"))
    status = db.relationship("Status", backref="event")

    event_comment = db.Column(db.String)


class Priority(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, index=True, nullable=False)


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, index=True, nullable=False)


if __name__ == "__main__":
    t = Priority(name="HIGH")
    c = Event(object_key=1, priority=t)
    db.session.add(c)
    db.session.commit()
