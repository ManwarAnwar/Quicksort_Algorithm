import time
import random
import numpy as np

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    arr = arr[:pivot_index] + arr[pivot_index+1:]
    left = [x for x in arr if x <= pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)

def measure_time(sort_fn, arr):
    start = time.time()
    sort_fn(arr)
    return time.time() - start

def main():
    sizes = [100, 500, 1000, 2000]
    for size in sizes:
        random_array = np.random.randint(0, 10000, size).tolist()
        print(f"\nInput size: {size}")
        print("Deterministic Quicksort:", measure_time(quicksort, random_array.copy()))
        print("Randomized Quicksort  :", measure_time(randomized_quicksort, random_array.copy()))

if __name__ == "__main__":
    main()
