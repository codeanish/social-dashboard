from dotenv import load_dotenv
import os

load_dotenv()

TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_USER_NAME = os.getenv("TWITTER_USER_NAME")