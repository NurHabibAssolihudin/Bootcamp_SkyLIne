# PYTHON DECORATOR
import time
import math

def calculateTime(func):
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner

@calculateTime
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

factorial(10)