import flask
from flask import request, jsonify
from datetime import datetime
import twitter
import followers_repository

app = flask.Flask(__name__)

@app.route('/', methods= ['GET'])
def health_check():
    return "OK"

@app.route('/twitterfollowers', methods = ['GET'])
def get_twitter_followers():
    as_of = request.args.get('as_of_date')
    if as_of is not None: 
        as_of_date = datetime.strptime(as_of, '%Y-%m-%d')
        if as_of_date.date() == datetime.now().date():
            return {"followers": twitter.get_followers()}
        if as_of_date.date() < datetime.now().date():
            return followers_repository.get_twitter_followers_as_of(as_of_date.date())
        else:
            return f"No twitter follower data on {as_of_date.strftime('%Y-%m-%d')}"
    return jsonify(followers_repository.get_twitter_followers_timeseries())


app.run(host='0.0.0.0')