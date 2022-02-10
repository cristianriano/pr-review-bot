import requests

from typing import List
from pull_request import *
from config import *

HEADERS = {
    'accept': 'application/vnd.github.v3+json'
}

BASE_PARAMS = {
    'state': 'open',
    'sort': 'created',
    'direction': 'desc',
    'pulls': 'true',
    'per_page': 10
}

BASE_URL = 'https://api.github.com'


def fetch_pr_by_labels(
    username: str,
    access_token: str,
    labels: str = "pim",
    repo: str = "Glovo/glovo-backend"
) -> List[PullRequest]:

    issues = fetch_issues(username, access_token, labels=labels, repo=repo)

    # TODO: Batching requests
    prs = (fetch_pr(issue['pull_request'], username, access_token)
           for issue in issues if 'pull_request' in issue)
    return list(prs)


def fetch_issues(username: str, access_token: str, labels: str, repo: str) -> dict:
    url = f'{BASE_URL}/repos/{repo}/issues'

    response = requests.get(
        url,
        params=BASE_PARAMS | {'labels': labels},
        headers=HEADERS,
        auth=(username, access_token)
    )

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            f'Error when talking to Github. Got: {response.status_code} "{response.text}"')


def fetch_pr(pull_request: dict, username: str, access_token: str):
    url = pull_request['url']
    response = requests.get(
        url,
        headers=HEADERS,
        auth=(username, access_token)
    )

    if response.status_code == 200:
        pr = response.json()
        reviewers = (reviewer['login']
                     for reviewer in pr['requested_reviewers'])
        return PullRequest(number=pr['number'], url=url, reviewers=list(reviewers))
    else:
        return None
