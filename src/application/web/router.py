from flask import render_template
from flask_smorest import Blueprint, abort

blp = Blueprint('Users', __name__, description='Operations related to webUI')

@blp.route('/')
def main_page():
    return render_template("home.html", active_page='home')

@blp.route('/about')
def about_page():
    return render_template("about.html", active_page='about')

@blp.route('/mywork')
def mywork_page():
    return render_template("mywork.html", active_page='mywork')

@blp.route('/publications')
def publications_page():
    return render_template("publications.html", active_page='publications')

@blp.route('/projects')
def projects_page():
    return render_template("projects.html", active_page='projects')