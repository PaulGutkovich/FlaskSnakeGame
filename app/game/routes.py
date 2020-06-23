from flask import Blueprint, render_template, flash, redirect, url_for, request
from app.game.forms import SaveScoreForm
from flask_login import login_required
from app.models import db, User
import json
import time

game = Blueprint('game', __name__)

@game.route('/index', methods=["GET", "POST"])
@game.route('/', methods=["GET", "POST"])
@login_required
def index():
    return render_template('game_html/lobby.html')

@game.route('/game_page', methods=["GET", "POST"])
@login_required
def index():
    return render_template('game_html/game_page.html')
