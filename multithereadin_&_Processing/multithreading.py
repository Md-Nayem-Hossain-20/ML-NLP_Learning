## Multithreading 
## When to use Multi Threading
### I/O-bound task : Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
### Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.


import threading
import time

def print_numbers():
    for i in range(20):
        time.sleep(0.2)
        print(f"Number : {i}")

def print_numbers1():
    for i in range(40):
        time.sleep(0.2)
        print(f"Number 2 : {i}")

def print_letters():
    for letter in "abcdefghijklmnopqrstuvwxyz":
        time.sleep(0.2)
        print(f"Letter : {letter}")



# Create 2 threads
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_numbers1)
t3 = threading.Thread(target = print_letters)




t = time.perf_counter()
# Start the threads
t1.start()
t2.start()
t3.start()

# Wait for the threads to finish
t1.join()
t2.join()
t3.join()


finished_time = time.perf_counter() - t
print(finished_time)


# t = time.perf_counter()
# print_numbers()
# print_letters()
# finished_time = time.perf_counter() - t
# print(finished_time)



