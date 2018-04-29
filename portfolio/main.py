from flask import request, redirect, render_template, session, flash
from app import app
# from flask_sqlalchemy import SQLAlchemy
# from models import User, Movie
import cgi




@app.route('/')
def home():

    return render_template("home.html")


@app.route('/github')
def github():
    return render_template("github.html")















if __name__ == "__main__":
    app.run()