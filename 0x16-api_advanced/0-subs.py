#!/usr/bin/python3
""" Number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/124.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
