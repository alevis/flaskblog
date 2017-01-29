import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
WHOOSH_BASE = os.path.join(basedir,'search.db')
MAX_SEARCH_RESULTS = 50
# pagination
POSTS_PER_PAGE = 3

# mail server settings
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['leevopergmail.com']


LANGUAGES = {
    'en':'English',
    'es':'Espanol'
}

OPENID_PROVIDERS = [
	{ 'name':'Google','url':'https://www.google.com/accounts/08/id' },
	{ 'name':'Yahoo', 'url':'https://me.yahoo.com' },
	{ 'name':'AOL', 'url':'http://openid.aol.com/<username>' },
	{ 'name':'Flickr','url':'http://www.flickr.com/<username>' },
	{ 'name':'MyOpenID','url':'https://www.myopenid.com'}
]
