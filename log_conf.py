import json
import logging.config
import os

log_conf_file_path = os.getenv('LOG_CONF', 'logging.json')
with open(log_conf_file_path) as log_conf_file:
    logging.config.dictConfig(json.load(log_conf_file))
