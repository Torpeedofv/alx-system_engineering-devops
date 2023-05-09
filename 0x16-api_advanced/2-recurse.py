#!/usr/bin/python3
"""Contains a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a
given subreddit. it should return none if no result is found for
the give subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'torpeedo'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=header, params=params)
    json_data = response.json()
    if 'error' in json_data:
        return None
    data = json_data.get('data')
    hot_list.extend([child.get('title') for child in data.get('children')])
    if data['after'] is not None:
        recurse(subreddit, hot_list, after=data.get('after'))
    return hot_list
