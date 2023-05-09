#!/usr/bin/python3
"""A recursive function that queries the reddit api parses the title of all
hot articles and prints a sorted count of given keywords(case-insensitive),
delimited by spaces."""
import requests


def count_words(subreddit, word_list, after='', counts=None):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'torpeedo'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=header, params=params)
    json_data = response.json()
    if 'error' in json_data:
        return
    counts = {word.lower(): 0 for word in word_list}
    data = json_data.get('data')
    children = data.get('children')
    for title in children:
        title = title.get('data').get('title').lower()
        for word in word_list:
            if word.lower() in title:
                counts[word.lower()] += 1
    if data.get('after'):
        count_words(subreddit, word_list, after=data.get('after'),
                    counts=counts)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    counts_str = ' '.join([f'{word}:{count}' for word, count in sorted_counts])
    print(counts_str)
    return counts
