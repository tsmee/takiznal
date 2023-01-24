import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'example.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Integer)
    created = db.Column(db.Integer)
    finished = db.Column(db.Integer)
    description = db.Column(db.String)

@app.route("/events")
def events_list():
    events = db.session.execute(db.select(Events).order_by(Events.id)).scalars()
    return render_template('show_all.html', events=events)

if __name__ == '__main__':
    app.run()

