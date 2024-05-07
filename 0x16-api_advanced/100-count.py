#!/usr/bin/python3
"""
script that counts the number of times a given word appears
in the titles of hot articles for a given subreddit
"""
import requests
import sys


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}
    if after is None:
        after = ''

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if posts:
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title.split():
                        counts[word.lower()] = counts.get(word.lower(), 0) + 1
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, counts)
            else:
                sorted_counts = sorted(counts.items(),
                                       key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            return None
    else:
        return None
