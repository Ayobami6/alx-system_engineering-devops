#!/usr/bin/python3
"""Get all posts recursively"""

import requests
import time


def count_words(subreddit: str, word_list: list, after: str = None,
                word_counts: dict = None) -> None:
    """Recursively retrieve all posts from subreddit and count occurrences of
    words in 'word_list'.

    Args:
        subreddit: Name of subreddit to search on reddit.com.
        word_list: List of words to search for in the post titles.
        after: Pagination parameter for reddit API.
        word_counts: Dictionary to hold word counts, used in recursive calls.

    Returns:
        None
    """

    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Count Word Bot 1.0'}
    params = {'limit': 100}

    # Add 'after' parameter for pagination if it exists
    if after:
        params['after'] = after

    response = requests.get(reddit_url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    # Get post data from response
    posts = response.json().get('data').get('children')

    # Initialize word_counts dict if it doesn't exist
    word_counts = word_counts or {}

    # Count occurrences of words in each post's title
    for post in posts:
        title = post["data"]["title"]
        for word in word_list:
            if word.lower() in title.lower():
                word_counts[word.lower()] = word_counts.get(
                    word.lower(), 0) + 1

    after = response.json()["data"]["after"]

    # If end of pagination and word_counts is empty, print nothing and return
    if after is None:
        if not word_counts:
            return
        # Sort the word_counts dict by value in descending order, then key in
        # ascending order
        for key, value in sorted(word_counts.items(), key=lambda x: (-x[1],
                                                                     x[0])):
            print("{}: {}".format(key.lower(), value))
        return

    # Wait for 3 seconds before sending next request
    time.sleep(3)

    return count_words(subreddit, word_list, after, word_counts)
