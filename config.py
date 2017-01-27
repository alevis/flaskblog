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
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = 'mthaneq'
MAIL_PASSWORD = 'password'

# administrator list
ADMINS = ['mthaneq@gmail.com']

OPENID_PROVIDERS = [
	{ 'name':'Google','url':'https://www.google.com/accounts/08/id' },
	{ 'name':'Yahoo', 'url':'https://me.yahoo.com' },
	{ 'name':'AOL', 'url':'http://openid.aol.com/<username>' },
	{ 'name':'Flickr','url':'http://www.flickr.com/<username>' },
	{ 'name':'MyOpenID','url':'https://www.myopenid.com'}
]
