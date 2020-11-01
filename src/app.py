import requests
import settings

def get_twitter_followers():
    bearer_token = settings.TWITTER_BEARER_TOKEN
    headers = {"Authorization": f"Bearer {bearer_token}"}
    user_name = settings.TWITTER_USER_NAME
    response = requests.get(f'https://api.twitter.com/1.1/followers/ids.json?screen_name={user_name}', headers=headers)
    response.raise_for_status()
    return (len(response.json()['ids']))

if __name__ == '__main__':
    print(get_twitter_followers())