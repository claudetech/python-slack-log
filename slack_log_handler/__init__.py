import logging
import requests


class SlackLogHandler(logging.Handler):
    EMOJIS = {
        logging.NOTSET: ':loudspeaker:',
        logging.DEBUG: ':speaker:',
        logging.INFO: ':information_source:',
        logging.WARNING: ':warning:',
        logging.ERROR: ':exclamation:',
        logging.CRITICAL: ':boom:'
    }

    LOG_FORMAT = '[%(levelname)s] [%(asctime)s] [%(name)s] - %(message)s'

    def __init__(self, webhook_url, channel=None, username=None, emojis=None):
        logging.Handler.__init__(self)
        self.webhook_url = webhook_url
        self.channel = channel
        self.username = username
        self.emojis = emojis if emojis is not None else SlackLogHandler.EMOJIS
        self.formatter = logging.Formatter(SlackLogHandler.LOG_FORMAT)

    def _make_content(self, record):
        content = {
            'text': self.format(record),
            'icon_emoji': self.emojis[record.levelno]
        }
        if self.username:
            content['username'] = self.username
        else:
            content['username'] = "{0} - {1}".format(record.module, record.name)
        if self.channel:
            content['channel'] = self.channel
        return content

    def emit(self, record):
        try:
            content = self._make_content(record)
            requests.post(self.webhook_url, json=content)
        except:
            self.handleError(record)
