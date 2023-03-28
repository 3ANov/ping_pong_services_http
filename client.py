import datetime
import logging
import os
import random
import time
import requests
import log_conf

server_port = os.getenv('SERVER_PORT', 8000)
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

