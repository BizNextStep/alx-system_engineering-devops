
"""
Module for getting the number of subscribers for a given subreddit using the Reddit API.
"""

import requests

def get_subreddit_subscribers(subreddit):
    """
    Gets the number of subscribers for a given subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit to get the subscribers count for.

    Returns:
        int: The number of subscribers for the given subreddit, or 0 if the subreddit does not exist.
    """
    url = f"https://api.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
