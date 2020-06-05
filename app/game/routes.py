from flask import Blueprint, render_template, flash, redirect, url_for, request
from app.game.forms import SaveScoreForm
from flask_login import login_required
from app.models import db, User

game = Blueprint('game', __name__)

@game.route('/index', methods=["GET", "POST"])
@game.route('/', methods=["GET", "POST"])
@login_required
def index():
    form = SaveScoreForm()
    return render_template('game/index.html', form=form)