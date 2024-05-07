#!/usr/bin/python3
""" Number of subscribers """

import requests
import sys


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        subscribers = response.json().get('data').get('subscribers')
        if subscribers is not None:
            return subscribers
        return 0
    return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument")
    else:
        print(number_of_subscribers(sys.argv[1]))
