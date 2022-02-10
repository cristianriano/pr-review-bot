from array import array


class PullRequest:
  def __init__(self, number: str, url: str, labels: array = []):
      self.number = number
      self.url = url
      self.labels = labels

  def to_s(self):
    print(f'PR: {self.number}\nURL: {self.url}')
