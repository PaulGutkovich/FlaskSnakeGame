from flask import Blueprint, render_template, flash, redirect, url_for, request
from app.auth.forms import LoginForm, RegistrationForm
from flask_login import login_required
from app.models import db, User
from werkzeug.urls import url_parse

game = Blueprint('game', __name__)

@login_required
@game.route('/index')
@game.route('/')
def index():
    return render_template('game/index.html')