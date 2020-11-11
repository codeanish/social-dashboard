import flask
from flask import request, jsonify
from datetime import date, datetime

from flask.wrappers import Request
import requests
from app import twitter
from app import followers_repository
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

@app.route('/', methods= ['GET'])
def health_check():
    return "OK"

@app.route('/twitterfollowers', methods = ['GET'])
def get_twitter_followers():    
    as_of_date = get_as_of_date_from_request(request)
    if as_of_date is not None:         
        if is_today(as_of_date):
            return get_live_followers_from_twitter()
        if date_in_the_past(as_of_date):
            print("As of date in the past")
            return get_followers_as_of(as_of_date)
        else:
            return f"No twitter follower data on {as_of_date.strftime('%Y-%m-%d')}"
    return get_twitter_timeseries()


@app.route('/followers', methods = ['POST'])
def save_twitter_followers_as_of():
    content = request.get_json()
    followers_repository.save_twitter_followers_as_of(content['followers'], content['as_of_date'])
    return "OK"


def get_twitter_timeseries() -> dict:
    return jsonify(followers_repository.get_twitter_followers_timeseries())


def get_followers_as_of(as_of_date: date) -> dict:
    return followers_repository.get_twitter_followers_as_of(as_of_date)


def get_live_followers_from_twitter() -> dict:
    return {"followers": twitter.get_followers()}


def get_as_of_date_from_request(request: Request) -> date:
    date_in_request = request.args.get('as_of_date')
    if date_in_request is not None:
        return datetime.strptime(date_in_request, '%Y-%m-%d').date()
    return None


def is_today(date_to_check: date) -> bool:
    if type(date_to_check) != date:
        raise TypeError(f"Expected a type of datetime for the parameter date_to_check. Instead received  {date_to_check} a type {type(date_to_check)}")
    if date_to_check == datetime.now().date():
        return True
    return False


def date_in_the_past(date_to_check: date) -> bool:
    if type(date_to_check) != date:
        raise TypeError(f"Expected a type of datetime for the parameter date_to_check. Instead received  {date_to_check} a type {type(date_to_check)}")
    if date_to_check < datetime.now().date():
        return True
    return False

if __name__ == "__main__":
    app.run(host='0.0.0.0')