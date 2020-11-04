import psycopg2
import settings

def get_twitter_followers_timeseries():
    try:
        conn = psycopg2.connect(f"dbname={settings.POSTGRES_DB} user={settings.POSTGRES_USER} host={settings.POSTGRES_HOST} password={settings.POSTGRES_PASSWORD}")        
        cur = conn.cursor()
        cur.execute("""SELECT * FROM twitter_followers_by_date;""")        
        rows = cur.fetchall()                
        return rows
    except:
        print ("Unable to connect to database")


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
        print ("Unable to save data to database")


def get_twitter_followers_as_of(as_of_date):
    try:
        conn = psycopg2.connect(f"dbname={settings.POSTGRES_DB} user={settings.POSTGRES_USER} host={settings.POSTGRES_HOST} password={settings.POSTGRES_PASSWORD}")        
        cur = conn.cursor()
        cur.execute("""SELECT * FROM twitter_followers_by_date WHERE as_of_date = %s;""", (as_of_date))
        rows = cur.fetchall()
        return rows
    except:
        print(f"Unable to get twitter followers as of {as_of_date}")
