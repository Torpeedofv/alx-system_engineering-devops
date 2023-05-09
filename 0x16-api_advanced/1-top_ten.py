#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'torpeedo'}
    params = {'limit': 10}
    response = requests.get(url, headers=header, params=params)
    json_data = response.json()
    if 'error' in json_data:
        print(None)
        return
    titles = json_data.get('data').get('children')
    elements = "\n".join(title.get('data').get('title') for title in titles)
    print(elements)
    return
