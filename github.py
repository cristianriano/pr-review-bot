import requests

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

def fetch_pr_by_labels(access_token: str, labels: str = "pim", repo: str = "Glovo/glovo-backend"):
  issues = fetch_issues(access_token, labels)
  # Filter if has ['pull_request'] value not empty
  # Query the url. Can we do it in batches?
  # Build the PR object


def fetch_issues(username: str, access_token: str, labels: str, repo: str):
  response = requests.get(
    build_issues_url(repo),
    params=BASE_PARAMS | {'labels': labels},
    headers=HEADERS,
    auth=(username, access_token))

  if response.status_code == 200:
    return response.json()
  else:
    raise Exception(f'Error when talking to Github. Got: {response.status_code} "{response.text}"')

def build_issues_url(repo: str):
  return f'{BASE_URL}/repos/{repo}/issues'
