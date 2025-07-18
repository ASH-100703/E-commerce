from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Ash#100703@e-commerce'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Product(db.Model):
id = db.Column(db.Integer , primary_key=True)
name = db.Column(db.String(100), nullable=False)
price = db.Column(db.Float, nullabe=False)


