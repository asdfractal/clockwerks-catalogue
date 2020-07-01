import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'fav_dota2_heroes'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo = PyMongo(app)

users = mongo.db.users


@app.route('/')
def index():
	return render_template('pages/index.html')


@app.route('/heroes')
def heroes():
	current_user = users.find_one({'name': 'test'})
	current_user_fav = current_user['favourites']
	print(current_user_fav)
	return render_template('pages/heroes.html', heroes=mongo.db.heroes.find(), user_favourites=current_user_fav)


@app.route('/add-to-favourites/<hero_id>', methods=['POST'])
def add_to_favourites(hero_id):
	current_user = users.find_one({'name': 'test'})
	mongo.db.users.update_one(current_user, {"$push": {"favourites": ObjectId(hero_id)}})
	return redirect(url_for('heroes'))


@app.route('/remove-from-favourites/<hero_id>', methods=['POST'])
def remove_from_favourites(hero_id):
	current_user = users.find_one({'name': 'test'})
	mongo.db.users.update_one(current_user, {"$pull": {"favourites": ObjectId(hero_id)}})
	return redirect(url_for('heroes'))


@app.route('/favourites')
def user_list():
	current_user = users.find_one({'name': 'test'})
	current_user_fav_id = current_user['favourites']
	current_user_fav = []

	for fav in current_user_fav_id:
		hero = mongo.db.heroes.find_one({'_id': fav})
		current_user_fav.append(hero)

	print(current_user_fav)
	return render_template('pages/user-list.html', heroes=mongo.db.heroes.find(), user_favourites_id=current_user_fav_id, user_favourites=current_user_fav)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    ip = os.environ.get('IP', '127.0.0.1')
    app.run(host=ip, port=port, debug=True)
