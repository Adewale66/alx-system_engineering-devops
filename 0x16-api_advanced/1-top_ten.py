#!/usr/bin/python3
""" Top ten hot posts"""

import requests


def top_ten(subreddit):
    """ Returns the top 10 posts """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)
    if response.status_code == 200:
        res = response.json().get("data").get("children")
        [print(x['data']['title']) for x in res]
    else:
        print("None")
