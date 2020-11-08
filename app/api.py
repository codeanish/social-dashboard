import flask
from flask import request, jsonify
from datetime import datetime
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
    as_of = request.args.get('as_of_date')
    if as_of is not None: 
        as_of_date = datetime.strptime(as_of, '%Y-%m-%d')
        if is_today(as_of_date):
            return get_live_followers_from_twitter()
        if date_in_the_past(as_of_date):
            return followers_repository.get_twitter_followers_as_of(as_of_date.date())
        else:
            return f"No twitter follower data on {as_of_date.strftime('%Y-%m-%d')}"
    return jsonify(followers_repository.get_twitter_followers_timeseries())


@app.route('/followers', methods = ['POST'])
def save_twitter_followers_as_of():
    content = request.get_json()
    followers_repository.save_twitter_followers_as_of(content['followers'], content['as_of_date'])
    return "OK"


def get_live_followers_from_twitter():
    return {"followers": twitter.get_followers()}


def is_today(date_to_check):
    if type(date_to_check) != datetime:
        raise TypeError(f"Expected a type of datetime for the parameter date_to_check. Instead received  {date_to_check} a type {type(date_to_check)}")
    if date_to_check.date() == datetime.now().date():
        return True
    return False


def date_in_the_past(date_to_check):
    if type(date_to_check) != datetime:
        raise TypeError(f"Expected a type of datetime for the parameter date_to_check. Instead received  {date_to_check} a type {type(date_to_check)}")
    if date_to_check.date() < datetime.now().date():
        return True
    return False

if __name__ == "__main__":
    app.run(host='0.0.0.0')