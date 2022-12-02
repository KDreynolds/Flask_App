import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template

CREATE_USERS_TABLE = (
    "CREATE TABLE IF NOT EXISTS users (user_id SERIAL PRIMARY KEY, user_name TEXT UNIQUE, user_pass TEXT);"
)

CREATE_TIMELINE_TABLE = (
    "CREATE TABLE IF NOT EXISTS timeline (post_id SERIAL PRIMARY KEY, post TEXT, post_user TEXT, date TIMESTAMP, FOREIGN KEY(post_user) REFERENCES users(user_name);"
)

CREATE_PROFILE_TABLE = (
    "CREATE TABLE IF NOT EXISTS profiles (profile_id SERIAL PRIMARY KEY, bio TEXT, user_profile_id INTEGER, trophy INTEGER, FOREIGN KEY(user_profile_id) REFERENCES users(id);"
)

INSERT_USER = (
    "INSERT INTO users(user_name, user_pass) VALUES (%s, %s);"
)

LOGIN_USER = (
    "SELECT EXISTS (SELECT * FROM users WHERE user_name = %s AND user_pass = %s)"
)

GATHER_TIMELINE = (
    ""
)

DISPLAY_TIMELINE = (

    ""
)

CREATE_POST = (
    ""
)




load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)


@app.get("/")
def index():
    return 

@app.get("/login")
def login_check():
    data = request.get_json()
    user_name = data["user_name"]
    user_pass = data["user_pass"]

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(LOGIN_USER, (user_name, user_pass))
    return {"login successful": user_name}, 201


@app.post("/signup")
def create_profile():
    data = request.get_json()
    user_name = data["user_name"]
    user_pass = data["user_pass"]

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(INSERT_USER, (user_name, user_pass))
    return {"user name": user_name,}, 201
    


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
