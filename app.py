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


@app.route('/hero/<hero_id>')
def hero_page(hero_id):
	hero = mongo.db.heroes.find_one({"_id": ObjectId(hero_id)})
	return render_template('pages/hero.html', hero=hero)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    ip = os.environ.get('IP', '127.0.0.1')
    app.run(host=ip, port=port, debug=True)
