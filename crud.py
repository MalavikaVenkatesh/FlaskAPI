from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir,'crud.sqlite')

db = SQLAlchemy(app)
ma = Marshmallow(app)

#Step 2 
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50),unique = True)
    email = db.Column(db.String(60),unique = True)

    def __init__ (self,username,email):
        self.username = username
        self.email = email


class UserSchema(ma.Schema):
    class Meta:
        fields = ('username','email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# Step 3

#Routes for CRUD 

#endpoint for creating new user 
@app.route("/user",methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']
    new_user = User(username,email)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

#endpoint for reading all the users from the DB 
@app.route("/user",methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)

#endpoint for reading a specify user
@app.route("/user/<id>",methods=["GET"])
def get_user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

#endpoint for updating the DB
@app.route("/user/<id>",methods=["PUT"])
def user_update(id):
    
    user = User.query.get(id)
    
    username = request.json['username']
    email = request.json['email']

    user.email = email
    user.username = username

    db.session.commit()
    return user_schema.jsonify(user)

#endpoint for the Delete feature from the DB 
@app.route("/user/<id>",methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    
    db.session.delete(user)
    db.session.commit()
    
    return user_schema.jsonify(user)

if __name__ == "__main__":
    app.run(debug= True)