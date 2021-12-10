import requests
import json
import logging
import time

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    while True:
        try:
            r = requests.get(url)
            data = json.loads(r.content)
            logging.info("Server is available. Time on server: %s", data['date'])
            logging.info("Request page: : %s", data['current_page'])
            logging.info("Answer of the server includes:")
            for key in data.keys():
                logging.info("Key: %s, Emount: %s", key, data[key])
        except requests.exceptions.ConnectionError:
            logging.error("There is no access to the ")
	    return 0
        time.sleep(60)

if __name__ == '__main__':
    main("http://localhost:8000/health")
