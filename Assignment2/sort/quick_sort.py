import sys
import random

sys.setrecursionlimit(20000)


# Quick Sort
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    # Pick a random pivot to avoid worst‐case on sorted input
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)
