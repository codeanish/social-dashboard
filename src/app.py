import requests
import settings
import psycopg2

def get_twitter_followers():
    bearer_token = settings.TWITTER_BEARER_TOKEN
    headers = {"Authorization": f"Bearer {bearer_token}"}
    user_name = settings.TWITTER_USER_NAME
    response = requests.get(f'https://api.twitter.com/1.1/followers/ids.json?screen_name={user_name}', headers=headers)
    response.raise_for_status()
    return (len(response.json()['ids']))

def get_twitter_followers_timeseries():
    try:
        conn = psycopg2.connect(f"dbname={settings.POSTGRES_DB} user={settings.POSTGRES_USER} host={settings.POSTGRES_HOST} password={settings.POSTGRES_PASSWORD}")        
        cur = conn.cursor()
        cur.execute("""SELECT * FROM twitter_followers_by_date""")        
        rows = cur.fetchall()        
        return rows
    except:
        print ("Unable to connect to database")

if __name__ == '__main__':
    # print(get_twitter_followers())
    print(get_twitter_followers_timeseries())