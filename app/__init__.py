from flask import Flask, render_template, flash
from flask_migrate import Migrate
from flask_login import LoginManager, login_required
from app.auth.routes import auth
from app.game.routes import game
from app.config import Config
from app.models import db, User

app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth.login'

db.init_app(app)

from app import models

@app.route('/index')
@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    print("recieved ajax request")

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(game, url_prefix='/game')