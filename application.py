import os
import requests

from flask import Flask, render_template, request, redirect
from models import *
from flask_socketio import SocketIO, emit, join_room, leave_room, send

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)

# config SocketIO
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

@app.route("/")
def index():
    channels = Channels.query.all()
    return render_template("index.html", channels=channels)

@app.route("/channels", methods = ["GET","POST"])
def channels():
    if request.method == "GET":
        return redirect("/")
    elif request.method == "POST":
        if (Channels.query.filter_by(channel=request.form.get("channel")).count() == 0):
            channel = Channels(channel=request.form.get("channel"))
            db.session.add(channel)
            db.session.commit()
        return redirect("/")

@socketio.on('send to chat')
def chat(data):
    text = data['text']
    emit('broadcast chat', {'text': text}, broadcast=True)

