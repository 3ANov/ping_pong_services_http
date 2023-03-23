import datetime
import json
import logging.config
import os
import random
import time
import requests

log_conf_file_path = os.getenv('LOG_CONF', 'logging.json')
server_port = os.getenv('SERVER_PORT', 8000)
with open(log_conf_file_path) as log_conf_file:
    logging.config.dictConfig(json.load(log_conf_file))

logger = logging.getLogger('client')

url = f'http://server:{server_port}'
session = requests.Session()

while True:
    headers = {
        'user-agent': 'client/0.0.1',
        'client_num_response': f'number-{random.randint(0, 50)}',
        'request-time': str(datetime.datetime.now())
    }
    req = session.get(url, headers=headers)
    logger.info(req.text)
    time.sleep(2)

