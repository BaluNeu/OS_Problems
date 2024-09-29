import threading
import time
import random

# Create a semaphore with a maximum of 3 concurrent accesses
semaphore = threading.Semaphore(3)

def access_resource(thread_id):
    print(f"Thread {thread_id} is waiting to access the resource.")
    # Acquire a permit
    semaphore.acquire()
    try:
        print(f"Thread {thread_id} has acquired the resource.")
        # Simulate some work
        time.sleep(random.uniform(1, 3))
    finally:
        # Release the permit
        semaphore.release()
        print(f"Thread {thread_id} has released the resource.")

threads = []

# Create multiple threads
for i in range(10):
    thread = threading.Thread(target=access_resource, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
