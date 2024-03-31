### This script will read all the posts in the `blogs` folder and post them to the GitHub issue tracker.

import os
import requests

token = "ghp_TOKEN"

def post_to_github_issue(title, body, category):
    url = "https://api.github.com/repos/dada878/dcard-homework/issues"
    headers = {
        "Authorization": f"token {token}"
    }
    data = {
        "title": title,
        "body": body,
        "labels": [f"category:{category}"]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code

def get_all_posts():
    posts = []
    for category in os.listdir('./blogs'):
        category_path = os.path.join('./blogs', category)
        for post in os.listdir(category_path):
            post_path = os.path.join(category_path, post)
            posts.append([category, post, post_path])
    return posts


def post_all_posts():
    for category, post, post_path in get_all_posts():
        with open(post_path, 'r') as f:
            title = f.readline().strip().replace('# ', '')
            body = f.read()
        status_code = post_to_github_issue(title, body, category)
        print(f"Post {post} with status code {status_code}")

post_all_posts()