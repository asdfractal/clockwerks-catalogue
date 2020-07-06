import os
from flask import Flask, render_template, redirect, request, url_for, session
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
	return render_template('pages/index.html', main_wrapper='index-main-wrapper', content_wrapper='index-content-wrapper')


@app.route('/heroes')
def heroes():
	current_user = users.find_one({'name': 'test'})
	current_user_fav = current_user['favourites']
	return render_template('pages/heroes.html', heroes=mongo.db.heroes.find(), user_favourites=current_user_fav, main_wrapper='heroes-main-wrapper', content_wrapper='heroes-content-wrapper')


@app.route('/add-to-favourites/<hero_id>', methods=['POST'])
def add_to_favourites(hero_id):
	current_user = users.find_one({'name': 'test'})
	mongo.db.users.update_one(current_user, {"$push": {"favourites": ObjectId(hero_id)}})
	return redirect(url_for('user_list'))


@app.route('/remove-from-favourites/<hero_id>', methods=['POST'])
def remove_from_favourites(hero_id):
	current_user = users.find_one({'name': 'test'})
	mongo.db.users.update_one(current_user, {"$pull": {"favourites": ObjectId(hero_id)}})
	return redirect(url_for('user_list'))


@app.route('/favourites')
def user_list():
	current_user = users.find_one({'name': 'test'})
	current_user_fav_id = current_user['favourites']
	current_user_fav = []

	for fav in current_user_fav_id:
		hero = mongo.db.heroes.find_one({'_id': fav})
		current_user_fav.append(hero)

	return render_template('pages/user-list.html', heroes=mongo.db.heroes.find(), user_favourites_id=current_user_fav_id, user_favourites=current_user_fav, main_wrapper='favourites-main-wrapper', content_wrapper='favourites-content-wrapper')


def set_password(password):
	return generate_password_hash(password)


def check_password(hash, password):
	return check_password_hash(hash, password)


@app.route('/user/create', methods=['GET', 'POST'])
def create_account():

	if session:
		return redirect(url_for('user_list'))

	if request.method == 'POST':
		password = request.form['password']
		password_confirm = request.form['password_confirm']
		if password == password_confirm:
			hash_pw = set_password(password)
			users.insert_one({
				'name': request.form['username'].lower(),
				'password': hash_pw,
				'favourites': []
			})
			session['username'] = request.form['username']
			print('ok')
			print(session)
			print(hash_pw)
			return redirect(url_for('heroes'))

	return render_template('pages/user-account.html', create_account=True, main_wrapper='account-main-wrapper', content_wrapper='account-content-wrapper')


@app.route('/user/login', methods=['GET', 'POST'])
def login():

	if session:
		return redirect(url_for('user_list'))

	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		current_user = users.find_one({'name': username})
		current_user_pw = current_user['password']
		check_pw = check_password_hash(current_user_pw, password)
		if check_pw == True:
			print(check_pw)
			session['username'] = request.form['username']
			return redirect(url_for('user_list'))

	return render_template('pages/user-account.html', create_account=False, main_wrapper='account-main-wrapper', content_wrapper='account-content-wrapper')


@app.route('/user/logout')
def logout():
	session.clear()
	return redirect(url_for('index'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    ip = os.environ.get('IP', '127.0.0.1')
    app.run(host=ip, port=port, debug=True)
