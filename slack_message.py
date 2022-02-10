class SlackMessage:

  MESSAGE_BLOCK = {
      "type": "section",
      "text": {
          "type": "mrkdwn",
          "text": "Hello, your have a PR review pending more than 24 hours ago. Please take a look!"
      }
  }
  BUTTONS_BLOCK = {
      "type": "actions",
      "elements": [
          {
              "type": "button",
              "text": {
                  "type": "plain_text",
                  "text": "Pull Request",
                  "emoji": "true"
              },
              "url": "https://api.github.com/repos/{org}/{repo}/pulls/{number}"
          }
      ]
  }
  DIVIDER_BLOCK = {"type": "divider"}

  def __init__(self, channel: str, url: str, username: str = "App Test", icon_emoji: str = ":robot_face:") -> None:
    self.channel = channel
    self.url = url
    self.username = username
    self.icon_emoji = icon_emoji

  def get_message_payload(self) -> dict:
    return {
        "channel": self.channel,
        "username": self.username,
        "icon_emoji": self.icon_emoji,
        "blocks": [
            self.MESSAGE_BLOCK,
            self.DIVIDER_BLOCK,
            self._get_buttons_block()
        ]
    }

  def _get_buttons_block(self):
    block = self.BUTTONS_BLOCK.copy()
    block['elements']['url'] = self.url
    return block
