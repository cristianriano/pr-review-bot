from github import fetch_pr_by_labels;

from config import *

if __name__ == '__main__':
  prs = fetch_pr_by_labels(USERNAME, ACCESS_TOKEN, labels=LABELS)