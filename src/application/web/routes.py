from flask import render_template
from flask_smorest import Blueprint, abort


blp = Blueprint('Users', __name__, description='Operations related to webUI')


@blp.route('/')
def home():
    return render_template("index.html")


@blp.route('/assistant')
def assistant():
    return render_template("assistant.html")


@blp.route('/papers')
def papers():
    render_template("papers.html")