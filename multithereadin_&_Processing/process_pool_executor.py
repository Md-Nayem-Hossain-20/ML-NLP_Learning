# Multiprocessing with ProcessPullExecutor

from concurrent.futures import ProcessPoolExecutor
import time


def square_number(number):
    time.sleep(1)
    return f"Square : {number * number}"


numbers = [1,2,3,4,5,6,7,8,11,12,14,2,3,50]

if __name__ == "__main__":


    with ProcessPoolExecutor(max_workers=10) as executor:
        results = executor.map(square_number, numbers)

    for result in results:
        print(result)



