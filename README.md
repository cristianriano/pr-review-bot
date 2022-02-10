# PR Review Bot

Python bot to check PRs with a given tag and remind reviewers in Slack

## Setup

- Python 3.9
- Activate the venv with
```bash
python -m venv .ven
source .venv/bin/activate
```
- Install dependencies
- `pip install -r requirements.tx`

### Adding Dependencies

- Install it via the CLI (make sure to activate venv first!)\
- `pip install ****`
- Update the requireements file
- `pip freeze > requirements.txt`

## Run

To run it from the python shell:
- `exec(open("./main.py").read())`

### Slack Message template

For designing messages Slack uses Block Kit framework.
[Here you can build how the message should look like](https://api.slack.com/tools/block-kit-builder)