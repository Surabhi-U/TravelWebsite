# Python standard libraries
import json
import os
import sqlite3
from click import password_option
from flask import Flask,redirect,url_for,render_template,request,flash,g,session

# Third-party libraries
#from flask import Flask, redirect, request, url_for
# from flask_login import (
#     LoginManager,
#     current_user,
#     login_required,
#     login_user,
#     logout_user,
# )



from db import init_db_command
from user import User

# Flask app setup
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
flag=1

    
# @app.route("/booknow")
# def book_now():
#     return render_template("booknow.html")

# @app.route("/review")
# def review():
#     return render_template("review.html")

# @app.route("/post")
# def post():
#     return render_template("post.html")

# @app.route("/login")
# def login():
#     return render_template("login.html")





#@app.route("/login",methods=["POST","GET"])  
#def login():
 #   if request.method=="POST":
  #      userID=request.form["Uname"]
   #     pw=request.form["Pass"]
    #    if userID=="admin" and pw=="1234":
     #       global flag
      #      flag=0
       #     user = User(
        #    id_="12345", name="admin", email="admin@gmail.com", profile_pic="placeholder")
         #   if not User.get("12345"):
          #      User.create("12345", "admin","admin@gmail.com", "placeholder")

#            Begin user session by logging the user in
 #           login_user(user)
  #          return redirect(url_for("index"))

   #3 return render_template('login.html')
    
    


# @app.route("/logout")
# #@login_required
# def logout():
#     logout_user()
#     global flag
#     if(flag==0):
#         flag=1
#     return redirect(url_for("index"))




    
# if __name__ == "__main__":
#     app.run(ssl_context="adhoc",debug=True)

from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3'
app.config['SECRET_KEY']="random string"

db = SQLAlchemy(app)

class users(db.Model):
    id=db.Column('user_id',db.Integer,primary_key=True)
    email=db.Column(db.String(100))
    password=db.Column(db.String(100))
    
def __init__(self,email,password):
    self.email= email
    self.password=password
    
@app.route("/booknow")
def book_now():
    return render_template("booknow.html")

@app.route("/review")
def review():
    return render_template("review.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route('/')
def index():
    return render_template('index.html', users= users.query.all() )

    
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        if not request.form['email'] or not request.form['password']:
            flash('Please enter all the fields ','error')
        else:
            user=user(request.form['email'],request.form['password'])
        
            db.session.add(user)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('index'))
    return render_template('login.html')
if __name__=='__main__':
    db.create_all()
    app.run(ssl_context="adhoc",debug=True)

