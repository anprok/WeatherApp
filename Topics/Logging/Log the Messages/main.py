import logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG)

for _ in range(5):
    logging.info("Test")