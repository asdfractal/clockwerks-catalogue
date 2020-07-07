import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.getenv('DBNAME')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.secret_key = os.getenv('SECRET_KEY')
mongo = PyMongo(app)

users = mongo.db.users


@app.route('/')
def index():
	"""
	Renders the home page.
	"""
	return render_template('pages/index.html', title='Home',
	main_wrapper='index-main-wrapper', content_wrapper='index-content-wrapper')


@app.route('/heroes')
def heroes():
	"""
	Renders the page to display all heroes. Checks if a user exists and if so,
	exposes data for the template.
	"""
	try:
		current_user = users.find_one({'name': session['username']})
		current_user_fav = current_user['favourites']
		return render_template('pages/heroes.html', title='Heroes',
		heroes=mongo.db.heroes.find(), user_favourites=current_user_fav,
		main_wrapper='heroes-main-wrapper',
		content_wrapper='heroes-content-wrapper')
	except:
		return render_template('pages/heroes.html', title='Heroes',
		heroes=mongo.db.heroes.find(),main_wrapper='heroes-main-wrapper',
		content_wrapper='heroes-content-wrapper')


@app.route('/add-to-favourites/<hero_id>', methods=['POST'])
def add_to_favourites(hero_id):
	"""
	Adds a hero to the current user's list.
	"""
	current_user = users.find_one({'name': session['username']})
	mongo.db.users.update_one(current_user,
	{"$push": {"favourites": ObjectId(hero_id)}})
	return redirect(url_for('user_list'))


@app.route('/remove-from-favourites/<hero_id>', methods=['POST'])
def remove_from_favourites(hero_id):
	"""
	Removes a hero from the current user's list.
	"""
	current_user = users.find_one({'name': session['username']})
	mongo.db.users.update_one(current_user,
	{"$pull": {"favourites": ObjectId(hero_id)}})
	return redirect(url_for('user_list'))


@app.route('/favourites')
def user_list():
	"""
	If a user is logged in, renders the page to show their list, otherwise
	redirects to create account page.
	"""
	if session:
		current_user = users.find_one({'name': session['username']})
		current_user_fav_id = current_user['favourites']
		current_user_fav = []

		for fav in current_user_fav_id:
			hero = mongo.db.heroes.find_one({'_id': fav})
			current_user_fav.append(hero)

		return render_template('pages/user-list.html', title='Favourites',
		heroes=mongo.db.heroes.find(), user_favourites_id=current_user_fav_id,
		user_favourites=current_user_fav,
		main_wrapper='favourites-main-wrapper',
		content_wrapper='favourites-content-wrapper')
	else:
		return redirect(url_for('create_account'))


def set_password(password):
	"""
	Encrypts user password.
	"""
	return generate_password_hash(password)


def check_password(hash, password):
	"""
	Decrypts user password.
	"""
	return check_password_hash(hash, password)


def check_user(username):
	"""
	Check if user exists in database.
	"""
	return users.find_one({'name': request.form['username']})


def create_user(username, password):
	"""
	Create new user in database.
	"""
	users.insert_one({
		'name': username,
		'password': password,
		'favourites': []
	})


@app.route('/user/create', methods=['GET', 'POST'])
def create_account():
	"""
	If a user is logged in, renders the page to show their list, otherwise
	renders the page to create account and creates a new user in the database
	upon form submission.
	"""
	if session:
		return redirect(url_for('user_list'))

	if request.method == 'POST':
		username = request.form['username'].lower()
		user_exists = check_user(username)
		password = request.form['password']
		password_confirm = request.form['password_confirm']
		if password == password_confirm:
			if user_exists is None:
				hash_pw = set_password(password)
				create_user(username, hash_pw)
				session['username'] = username
				return redirect(url_for('heroes'))
			flash('Username is taken, please try another one.')
		else:
			flash('Password does not match, please re-enter.')

	return render_template('pages/user-account.html', title="Create Account",
	create_account=True, main_wrapper='account-main-wrapper',
	content_wrapper='account-content-wrapper')


@app.route('/user/login', methods=['GET', 'POST'])
def login():
	"""
	If a user is logged in, renders the page to show their list, otherwise
	renders the page to login and handles requests.
	"""
	if session:
		return redirect(url_for('user_list'))

	if request.method == 'POST':
		username = request.form['username'].lower()
		password = request.form['password']
		current_user = users.find_one({'name': username})
		if current_user:
			current_user_pw = current_user['password']
			check_pw = check_password_hash(current_user_pw, password)
			if check_pw == True:
				session['username'] = request.form['username']
				return redirect(url_for('user_list'))
			else:
				flash('Incorrect password, please try again.')
		else:
			flash('That username does not exist.')

	return render_template('pages/user-account.html', title="Login",
	create_account=False, main_wrapper='account-main-wrapper',
	content_wrapper='account-content-wrapper')


@app.route('/user/logout')
def logout():
	"""
	Logs user out by clearing the session and redirects to home page.
	"""
	session.clear()
	return redirect(url_for('index'))


@app.errorhandler(404)
def error_page_not_found(e):
	"""
	Renders a 404 error page.
	"""
	error = str(e)
	return render_template('pages/error.html', error=error,
	main_wrapper='error-main-wrapper',
	content_wrapper='error-content-wrapper'), 404


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    ip = os.environ.get('IP', '127.0.0.1')
    app.run(host=ip, port=port, debug=True)
