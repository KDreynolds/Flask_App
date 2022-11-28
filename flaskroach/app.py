from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template
from sqlalchemy import insert



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


# Routes
@app.route("/")
def index():
    return render_template('login.html')


@app.route("/login", methods=['GET'])
def login():
    return


@app.route("/signup", methods=['POST'])
def create_profile():
    user_name = request.form.get("user_name")
    user_pass = request.form.get("user_pass")

    if user_name != '' and user_pass != '':
        insert()



@app.route("/timeline", methods=['GET'])
def timeline():
    return


@app.route("/timeline", methods=['POST'])
def new_post():
    return


@app.route("/timeline", methods=['DELETE'])
def delete_post():
    return


@app.route("/bio", methods=['POST'])
def create_bio():
    return


@app.route("/bio", methods=['GET'])
def view_bio():
    return





