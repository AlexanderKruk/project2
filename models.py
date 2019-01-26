import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Channels(db.Model):
    __tablename__="channels"
    id = db.Column(db.Integer, primary_key=True)
    channel = db.Column(db.String, nullable=False)