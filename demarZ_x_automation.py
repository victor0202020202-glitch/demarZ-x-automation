#!/usr/bin/env python3
import requests
from requests_oauthlib import OAuth1Session
import json
from datetime import datetime
import os
import sys

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

if not all([CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
              print('ERROR: Missing Twitter credentials in environment variables')
              sys.exit(1)
          
TWEETS = [
              "💰 Join 2,847 Filipinos earning passive income. DeMarz: 15% APY on staking. Limited spots. Start here: demarzcommunity.netlify.app?ref=BCmLJqGe #DeFi",
              "🔥 $100 becomes $115/month. Automated staking. No experience needed. No gas fees. Join Node Operators: demarzcommunity.netlify.app?ref=BCmLJqGe #CryptoEarnings",
              "⏰ Inflation eating your savings? Earn 18% APY on BNB. Institutional-grade security. 48h setup. DeMarz: demarzcommunity.netlify.app?ref=BCmLJqGe #PassiveIncome",
              "🎯 DeMarz Node Operators. 8-generation referral commissions. Earn from your network. Top performers making $5K+/month. Apply: demarzcommunity.netlify.app?ref=BCmLJqGe",
              "✨ The new standard for intelligent wealth building. Crypto staking made simple. AI-powered. Community-driven. DeMarz Community: demarzcommunity.netlify.app?ref=BCmLJqGe #AurumX"
]

def get_next_tweet():
              day = datetime.now().day
              return TWEETS[(day - 1) % len(TWEETS)]
          
def post_tweet(tweet_text):
              oauth = OAuth1Session(
                                CONSUMER_KEY,
                                client_secret=CONSUMER_SECRET,
                                resource_owner_key=ACCESS_TOKEN,
                                resource_owner_secret=ACCESS_TOKEN_SECRET
              )
              response = oauth.post("https://api.twitter.com/2/tweets", json={"text": tweet_text})
              return response.status_code == 201
          
if __name__ == "__main__":
              tweet = get_next_tweet()
              print(f"📋 Posting tweet: {tweet[:50]}...")
              if post_tweet(tweet):
                                print("✅ SUCCESS!")
              else:
                                print("❌ Failed to post tweet")
                        #!/usr/bin/env python3
import requests
from requests_oauthlib import OAuth1Session
import json
from datetime import datetime
import os

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

# Validate that all credentials are present
if not all([CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
          raise ValueError("Missing one or more required environment variables: CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET")qx!Hh0y"

TWEETS = [
      "💰 Join 2,847 Filipinos earning passive income. DeMarz: 15% APY on staking. Limited spots. Start here: demarzcommunity.netlify.app?ref=BCmLJqGe #DeFi",
      "🔥 $100 becomes $115/month. Automated staking. No experience needed. No gas fees. Join Node Operators: demarzcommunity.netlify.app?ref=BCmLJqGe #CryptoEarnings",
      "⏰ Inflation eating your savings? Earn 18% APY on BNB. Institutional-grade security. 48h setup. DeMarz: demarzcommunity.netlify.app?ref=BCmLJqGe #PassiveIncome",
      "🎯 DeMarz Node Operators. 8-generation referral commissions. Earn from your network. Top performers making $5K+/month. Apply: demarzcommunity.netlify.app?ref=BCmLJqGe",
      "✨ The new standard for intelligent wealth building. Crypto staking made simple. AI-powered. Community-driven. DeMarz Community: demarzcommunity.netlify.app?ref=BCmLJqGe #AurumX"
]

STATE_FILE = "/tmp/demarZ_x_state.json"

def get_next_tweet():
      day = datetime.now().day
      return TWEETS[(day - 1) % len(TWEETS)]

def post_tweet(tweet_text):
      oauth = OAuth1Session(
                CONSUMER_KEY.strip(),
                client_secret=CONSUMER_SECRET.strip(),
                resource_owner_key=ACCESS_TOKEN.strip(),
                resource_owner_secret=ACCESS_TOKEN_SECRET.strip()
      )
      response = oauth.post("https://api.twitter.com/2/tweets", json={"text": tweet_text})
      return response.status_code == 201

if __name__ == "__main__":
      tweet = get_next_tweet()
      print(f"📋 Posting tweet: {tweet[:50]}...")
      if post_tweet(tweet):
                print("✅ SUCCESS!")
else:
          print("❌ Failed to post tweet")
