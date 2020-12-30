import multiprocessing
import time
from random import random

def random_log_entry_generator():
    name = multiprocessing.current_process().name
    print(name, 'Starting')
    count = 0
    while count < 5:
        number = round(random() * 10, 5)
        random_number = "%d" % number
        entry = 'The new random entry is : ' + random_number
        time.sleep(3)
        count += 1
        print(entry)
    print(name, 'Exiting')

def my_service():
    name = multiprocessing.current_process().name
    print name, 'Starting'
    time.sleep(3)
    print name, 'Exiting'

if __name__ == '__main__':
    service = multiprocessing.Process(name='my_service', target=my_service)
    random_log_entry_generator = multiprocessing.Process(name='random_log_entry_generator', target=random_log_entry_generator())
    worker_2 = multiprocessing.Process(target=random_log_entry_generator()) # use default name

    random_log_entry_generator.start()
    worker_2.start()
    service.start()
