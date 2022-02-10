from github import fetch_pr_by_labels;

from config import *

prs = fetch_pr_by_labels(USERNAME, ACCESS_TOKEN, labels=LABELS)

for pr in prs:
  print(pr.to_s())
