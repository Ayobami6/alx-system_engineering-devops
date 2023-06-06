#!/usr/bin/python3
""" Get all posts recursively """

import requests
from typing import List
from typing import Optional


def recurse(subreddit: str, hot_list: Optional[List[str]] = None, after:
            Optional[str] = None) -> List[str]:
    """ Get all posts recursively

    Args:
        subreddit (str): subreddit name
        hot_list (List[str]): list of hot posts
        after (str): after post id

    Returns:
        List[str]: list of hot posts
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Ayo User Agent 1.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    posts = response.json().get('data').get('children')
    if hot_list is None:
        hot_list = []
    for post in posts:
        hot_list.append(post.get('data').get('title'))
    after = response.json().get('data').get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
