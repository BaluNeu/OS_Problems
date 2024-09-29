import threading

counter = 0

# lock = threading.Lock()

def inc_counter():

    global counter

    for i in range(10000000):
        # lock.acquire()
        try:
            counter+=1
        finally:
            # lock.release()
            pass

threads = []

# Create multiple threads
for i in range(10):
    thread = threading.Thread(target=inc_counter)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")
