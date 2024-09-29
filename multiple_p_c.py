import threading
import time
import random

buffer = []
buffer_size = 5

# Semaphores
empty = threading.Semaphore(buffer_size)  # Tracks how many slots are empty
full = threading.Semaphore(0)             # Tracks how many items are available to consume

# Mutex for buffer access
mutex = threading.Lock()

def producer(id):
    while True:
        item = random.randint(1, 100)
        empty.acquire()  # Wait if buffer is full
        mutex.acquire()
        buffer.append(item)
        print(f"Producer {id} produced {item}")
        mutex.release()
        full.release()  # Signal that buffer has items
        time.sleep(random.uniform(0.1, 1))

def consumer(id):
    while True:
        full.acquire()  # Wait if buffer is empty
        mutex.acquire()
        item = buffer.pop(0)
        print(f"Consumer {id} consumed {item}")
        mutex.release()
        empty.release()  # Signal that buffer has space
        time.sleep(random.uniform(0.1, 1))

# Create multiple producers and consumers
producers = []
consumers = []

for i in range(3):  # 3 producers
    producer_thread = threading.Thread(target=producer, args=(i,))
    producers.append(producer_thread)
    producer_thread.start()

for i in range(5):  # 5 consumers
    consumer_thread = threading.Thread(target=consumer, args=(i,))
    consumers.append(consumer_thread)
    consumer_thread.start()

# Wait for all threads to finish
for p in producers:
    p.join()

for c in consumers:
    c.join()
