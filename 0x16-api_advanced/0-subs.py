#!/usr/bin/python3
"""A function that queries the Reddit API and returns the
number of users for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-Agent': 'torpeedo'}
    response = requests.get(url, headers=header)
    json_response = response.json()
    if 'error' in json_response:
        return 0
    return json_response.get('data').get('subscribers')
