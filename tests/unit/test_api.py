import pytest
from datetime import date, datetime, timedelta
from app import api
from app import twitter
from app import followers_repository
from flask import request

def test_health_check():
    assert api.health_check() == "OK"


def test_is_today():
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    assert api.is_today(today) == True
    assert api.is_today(yesterday) == False
    assert api.is_today(tomorrow) == False
    

def test_is_today_invalid_input():
    with pytest.raises(TypeError):
        api.is_today("today")
        api.is_today(1)
        api.is_today(True)
        api.is_today(-0.9327)

def test_date_in_the_past():
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    last_year = today - timedelta(days=365)
    tomorrow = today + timedelta(days=1)

    assert api.date_in_the_past(today) == False
    assert api.date_in_the_past(tomorrow) == False
    assert api.date_in_the_past(yesterday) == True
    assert api.date_in_the_past(last_year) == True

    # This will be true once a day. Potential bug    
    one_second_ago = today - timedelta(seconds=1)
    assert api.date_in_the_past(one_second_ago) == False


def test_date_in_the_past_invalid_input():
    with pytest.raises(TypeError):
        api.date_in_the_past("yesterday")
        api.date_in_the_past(-1)
        api.date_in_the_past("2020-06-01")
        api.date_in_the_past(-4324.532)

def test_get_live_followers_from_twitter(monkeypatch):
    def mock_twitter_followers():
        return 42

    monkeypatch.setattr(twitter, "get_followers", mock_twitter_followers)

    result = api.get_live_followers_from_twitter()

    assert result.get("followers") == 42

def test_get_followers_as_of(monkeypatch):
    as_of_date = date(2020,6,1)
    def mock_followers_repo_as_of(as_of):
        return {"as_of_date": "2020-06-01","followers": 100}
    monkeypatch.setattr(followers_repository, "get_twitter_followers_as_of", mock_followers_repo_as_of)

    result = api.get_followers_as_of(as_of_date)
    assert result.get("followers") == 100
    assert result.get("as_of_date") == "2020-06-01"