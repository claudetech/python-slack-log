# Python Slack log handler

Simple Python log handler for Slack using Slack webhooks.

# Installation

```sh
$ pip install slack_log_handler
```

## Usage

The only required argument for `SlackLogHandler` is the webhook URL.
You can pass the `channel`, `username`, or a dictionary of `emojis` for each
log level as named arguments.

Sample usage:

```python
import os
import logging
from slack_log_handler import SlackLogHandler

WEBHOOK_URL = os.getenv('SLACK_URL')

slack_handler = SlackLogHandler(WEBHOOK_URL)
slack_handler.setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
logger.addHandler(slack_handler)

logger.error('Oh my god, an error occurred!')
```
