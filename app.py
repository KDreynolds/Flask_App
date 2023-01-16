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
    "CREATE TABLE IF NOT EXISTS timeline (post_id SERIAL PRIMARY KEY, post TEXT, post_user TEXT, date TIMESTAMP);"
)

CREATE_PROFILE_TABLE = (
    "CREATE TABLE IF NOT EXISTS profiles (profile_id SERIAL PRIMARY KEY, bio TEXT, user_name TEXT UNIQUE, trophy INTEGER);"
)

INSERT_USER = (
    "INSERT INTO users(user_name, user_pass) VALUES (%s, %s);"
)

LOGIN_USER = (
    "SELECT EXISTS (SELECT * FROM users WHERE user_name = %s AND user_pass = %s)"
)

GATHER_TIMELINE = (
    "SELECT post, post_user FROM timeline"
)

CREATE_POST = (
    "INSERT INTO timeline(post, post_user) VALUES (%s, %s)"
)

CREATE_BIO = (
    "INSERT INTO profiles(bio, user_name, trophy) VALUES (%s, %s, %s)"
)

GET_BIO = (
    "SELECT EXISTS (SELECT * FROM profiles WHERE profile_id = %s)"
)

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)


@app.get("/")
def index():
    return render_template('index.html')

#Login endpoint, probably need to add more to logic for this to actually work
@app.get("/login")
def login_check():
    data = request.get_json()
    user_name = data["user_name"]
    user_pass = data["user_pass"]

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(LOGIN_USER, (user_name, user_pass))
    return {"login successful": user_name}, 201


#End point for signing a new user up
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
    

#Stuck here, need to add the logic to return json of all posts made and the users who made the posts
#@app.get("/timeline")
#def timeline():
#    with connection:
#        with connection.cursor() as cursor:
#            cursor.execute(CREATE_TIMELINE_TABLE)
#            cursor.execute(GATHER_TIMELINE())
            

#End point for user to add a post to the timeline
@app.post("/timeline")
def create_post():
    data = request.get_json()
    post = data["post"]
    post_user = data["post_user"]

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TIMELINE_TABLE)
            cursor.execute(CREATE_POST, (post, post_user))
    return {"Successful post by": post_user,}, 201


#End point for users to create a bio section
@app.post("/bio")
def create_bio():
    data = request.get_json()
    bio = data["bio"]
    post_user = data["post_user"]
    trophy = data["trophy"]

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_PROFILE_TABLE)
            cursor.execute(CREATE_BIO, (bio, post_user, trophy))
    return {"Bio Updated": post_user,}, 201


#End point for fetching a users bio
@app.get("/bio")
def view_bio():
    data = request.get_json()
    profile_id = data["profile_id"]

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_BIO, (profile_id))
    return {"Bio for": profile_id,}, 201
