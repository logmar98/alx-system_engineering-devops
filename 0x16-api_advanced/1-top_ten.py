#!/usr/bin/python3
"""print hot posts on Reddit subreddit."""


def top_ten(subreddit):
    """Print titles of 10 hottest posts on subreddit."""
    import requests


    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "test-api for project in alx school"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    for c in results.get("children"):
        print(c.get("data").get("title"))
