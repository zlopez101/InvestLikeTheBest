from flask import Flask, render_template, url_for, jsonify, redirect
from flask_pymongo import PyMongo
import re


app = Flask(__name__)
app.config[
    "MONGO_URI"
] = "mongodb+srv://Zach:X.oEyXBdG3C62@cluster0.b4an6.mongodb.net/InvestLikeTheBest?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route("/")
def home():
    return redirect(url_for("transcript", episode_id=184))


@app.route("/<int:episode_id>")
def transcript(episode_id):
    episode = mongo.db.Podcasts.find_one({"_id": str(episode_id)})
    quotes = list(mongo.db.Quotes.find({"episode": episode_id}))
    return render_template("episode.html", episode=episode, quotes=quotes)


@app.route("/get-episode/<episode_id>")
def get_episode(episode_id):
    episode = mongo.db.Podcasts.find({"_id": episode_id})
    return jsonify(episode)


@app.route("/api/quotes/<int:episode>/")
def quote(episode):
    # quote API that returns quotes for episode and quote_number
    quote = mongo.db.Quotes.find_one({"episode": episode})
    return jsonify(quote)


@app.route("/post-episode/<episode_id>/<guest>/<title>", methods=["GET", "POST"])
def create_new_episode(episode_id, guest, title):
    """
    underscores _ not spaces
    """
    episode = {
        "_id": episode_id,
        "guest": guest.replace("_", " "),
        "title": title.replace("_", " "),
        "link": "http://investorfieldguide.com/podcast",
    }
    mongo.db.Podcasts.insert_one(episode)
    return redirect(url_for("home"))

