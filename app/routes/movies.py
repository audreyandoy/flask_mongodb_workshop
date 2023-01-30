from app import mongo
from flask import Blueprint, jsonify, abort, make_response, request
from datetime import date 

movies_bp = Blueprint("movies_bp", __name__, url_prefix="/movies")

@movies_bp.route("", methods=["POST"])
def add_item():
    movie = {"movie": "LOTR", "type": "fantasy"}
    print("hi")
    mongo.db.movies.insert_one(movie)
    return jsonify("hi")
    
