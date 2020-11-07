import pytest
from datetime import datetime, timedelta
from app import api

def test_health_check():
    assert api.health_check() == "OK"


def test_is_today():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    assert api.is_today(today) == True
    assert api.is_today(yesterday) == False
    assert api.is_today(tomorrow) == False


def test_date_in_the_past():
    today = datetime.now()
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