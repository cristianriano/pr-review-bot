from typing import List

class PullRequest:
  def __init__(self, number: str, url: str, labels: List = [], reviewers: List = []):
      self.number = number
      self.url = url
      self.labels = labels
      self.reviewers = reviewers

  def to_s(self):
    return f'PR: {self.number}\nURL: {self.url}\nReviewrs: {self.reviewers}\n\n'
