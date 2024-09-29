import threading
import time
import random


shared_buffer = []
buffer_size = 5


# declare 3 semaphores
mutex = threading.Lock() # to maintain one thread access at once
empty = threading.Semaphore(buffer_size)
full = threading.Semaphore(0)

def producer():

    item = random.randint(1,100)
    empty.acquire() # decrement slots that says its filled
    mutex.acquire()
    shared_buffer.append(item)
    print(f"produced : {item}")
    mutex.release()
    full.release() # increment items in the buffer to consume
    time.sleep(random.uniform(0.1, 1)) 

def consumer():

    item = random.randint(1,100)
    full.acquire() # decrement item to consume
    mutex.acquire()
    shared_buffer.pop(0)
    print(f"consumed : {item}")
    mutex.release()
    empty.release() # increment empty slots in the buffer
    time.sleep(random.uniform(0.1, 1))


producer_thread = threading.Thread(target = producer)
consumer_thread = threading.Thread(target = consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()