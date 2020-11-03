import psycopg2
import settings

def get_twitter_followers_timeseries():
    try:
        conn = psycopg2.connect(f"dbname={settings.POSTGRES_DB} user={settings.POSTGRES_USER} host={settings.POSTGRES_HOST} password={settings.POSTGRES_PASSWORD}")        
        cur = conn.cursor()
        cur.execute("""SELECT * FROM twitter_followers_by_date""")        
        rows = cur.fetchall()        
        return rows
    except:
        print ("Unable to connect to database")


def get_twitter_followers_as_of(as_of_date):
    return ""


if __name__ == "__main__":
    print(get_twitter_followers_timeseries())