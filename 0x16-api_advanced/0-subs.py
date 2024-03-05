#!/usr/bin/python3
"""query a number of subscription."""
import requests


def number_of_subscribers(subreddit):
    """Return total number of subscribers subreddit."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "test-api for project in alx school"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0

    results = response.json().get("data")
    return results.get("subscribers")
