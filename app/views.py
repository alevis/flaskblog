iimport datetime
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm, EditForm, PostForm
from .models import User, Post
from app import app
from config import POSTS_PER_PAGE


@app.before_request
def before_request():
    g.user  = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()
        g.search_form = SearchForm()

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
@app.route('/index/<int:page>',methods=['GET','POST'])
@login_required
def index(page=1):
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data,timestamp=datetime.utcnow(),author=g.user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    posts = g.user.followed_posts().paginate(page,POSTS_PER_PAGE,False)
    return render_template('index.html',
				title='Home',
				user=user,
				posts=posts)

@app.route('/login', methods=['GET','POST'])
@oid.loginhandler
def login():
	if g.user is not None and g.user.is_authenticated:
			return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
			session['remember_me'] = form.remember_me.data
			return oid.try_login(form.openid.data, ask_for=['nickname','email'])
	return render_template('login.html',
							title='Sign In',
							form=form,
							providers=app.config['OPENID_PROVIDERS'])

@app.route('/user/<nickname>')i
@app.route('/user/<nickname>/<int:page>')
@login_required
def user(nickname,page=1):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flask('User %s not found.' % nickname)
        return redirect(url_for('index'))
    posts = user.posts.paginate(page, POSTS_PER_PAGE, False)
    return render_template('user.html',user=user,posts=posts)

@oid.after_login
def after_login(resp):
	if resp.email is None or resp.email == "":
		flash('Invalid login. Please try again. ')
		return redirect(url_for('login'))
	user = User.query.filter_by(email=resp.email).first()
	if user is None:
		nickname = resp.nickname
		if nickname is None or nickname == "":
			nickname = resp.email.split('@')[0]
		user = User(nickname=nickname, email=resp.email)
		db.session.add(user)
		db.session.commit()
	remember_me = False
	if 'remember_me' in session:
		remember_me = session['remember_me']
		session.pop('remember_me', None)
	login_user(user, remember = remember_me)
	return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/edit',methods=['GET','POST'])
@login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your change have been saved.')
        return redirect(url_for('eidt'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html',form=form)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'),500

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))
