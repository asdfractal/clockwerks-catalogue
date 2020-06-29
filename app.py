import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'fav_dota2_heroes'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo = PyMongo(app)


@app.route('/')
def index():
	return render_template('pages/index.html')


@app.route('/heroes')
def heroes():
	return render_template('pages/heroes.html', heroes=mongo.db.heroes.find())


@app.route('/add-to-favourites/<hero_id>', methods=['POST'])
def add_to_favourites(hero_id):
	users = mongo.db.users
	current_user = users.find_one({'name': 'test'})
	mongo.db.users.update_one(current_user, {"$push": {"favourites": ObjectId(hero_id)}})
	return redirect(url_for('heroes'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    ip = os.environ.get('IP', '127.0.0.1')
    app.run(host=ip, port=port, debug=True)
