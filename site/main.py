from flask import Flask, render_template, request, redirect

from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app )

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable =False)
    picture = db.Column(db.String(100), nullable =False)
    points = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f'<User {self.name}>'
    


@app.route("/")
def leader():
    users = User.query.order_by(User.points.desc()).filter(User.points > 0).all()
    return render_template("leader.html",
                           users = users)

@app.route("/filtr")
def filtr():
    users = User.query.order_by(User.points.asc()).filter(User.points > 0).all()
    return render_template("leader.1.html",
                           users = users)
    
if __name__ == "__main__":
    app.run(debug=True)

