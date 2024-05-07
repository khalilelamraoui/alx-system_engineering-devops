#!/usr/bin/python3
"""top_ten"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    hot_posts = response.json().get('data').get('children')
    for post in hot_posts[:10]:
        print(post.get('data').get('title'))
