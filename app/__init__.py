import os
from flask import Flask#, request, url_for
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir#, MAIL_PORT, MAIL_USERNAME
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from .momentjs import momentjs
__all__ = ["views","models"]

app = Flask(__name__)
mail = Mail(app)
app.config.from_object('config')
db = SQLAlchemy(app)
app.jinja_env.globals['momentjs'] = momentjs

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/megapp.log','a',1*1024*1024,10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('megapp startup')
from app import views, models
