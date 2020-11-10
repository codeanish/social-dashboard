from datetime import date, datetime
import psycopg2
from app import settings

def get_twitter_followers_timeseries() -> list:
    try:
        conn = psycopg2.connect(f"dbname={settings.POSTGRES_DB} user={settings.POSTGRES_USER} host={settings.POSTGRES_HOST} password={settings.POSTGRES_PASSWORD}")        
        cur = conn.cursor()
        cur.execute("""SELECT as_of_date, followers FROM twitter_followers_by_date;""")        
        rows = cur.fetchall()                
        return rows_to_list_of_dict(rows)
    except:
        raise ("Unable to connect to database")


def save_twitter_followers_as_of(follower_count, as_of_date):
    try:
        conn = psycopg2.connect(f"dbname={settings.POSTGRES_DB} user={settings.POSTGRES_USER} host={settings.POSTGRES_HOST} password={settings.POSTGRES_PASSWORD}")        
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO twitter_followers_by_date(as_of_date, followers)
            VALUES (%s, %s);
            """, (as_of_date, follower_count))
        conn.commit()
        cur.close()
        conn.close()
    except:
        raise ("Unable to save data to database")


def get_twitter_followers_as_of(as_of_date: date) -> dict:
    try:
        conn = psycopg2.connect(f"dbname={settings.POSTGRES_DB} user={settings.POSTGRES_USER} host={settings.POSTGRES_HOST} password={settings.POSTGRES_PASSWORD}")        
        cur = conn.cursor()
        cur.execute("""SELECT as_of_date, followers FROM twitter_followers_by_date WHERE as_of_date = %s;""", (as_of_date,))
        rows = cur.fetchall()
        return row_to_dict(rows[0])
    except:
        raise(f"Unable to get twitter followers as of {as_of_date}")


def rows_to_list_of_dict(rows: list) -> list:
    followers = []
    for row in rows:
        followers.append(row_to_dict(row))
    return followers

def row_to_dict(row: tuple) -> dict:
    followers = {}
    # followers["as_of_date"] = datetime.strptime(row[0], "%a, %d %b %Y %H:%M:%S %Z").date()
    followers["as_of_date"] = row[0]
    followers["followers"] = row[1]    
    return followers
