import logging
import time

logging.basicConfig(filename='example.log',level=logging.DEBUG)
k = 0
while True:
    logging.debug(str(k) + 'This message should ligkbdfg')
    time.sleep(5)
    k += 1