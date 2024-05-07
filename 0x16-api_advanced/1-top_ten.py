#!/usr/bin/python3
"""
Script that queries the Reddit API and returns the top 10 hot posts listed.
"""
import requests
import sys


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                print(post['data']['title'])
        else:
            print("No posts found for this subreddit.")
    else:
        print("None")
