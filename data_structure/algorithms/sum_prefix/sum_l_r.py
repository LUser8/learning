# Given an array arr[] of size n. 
# Given q queries and in each query given i and j, Print the sum of array elements from index i to j.
from functools import reduce

def pre_compute(arr):
    n = len(arr)
    prefix_sum = [0] * n

    prefix_sum[0] = arr[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    
    return prefix_sum

def range_sum(i, j, pre):
    if i == 0:
        return pre[j]
    
    return pre[j] - pre[i-1]

if __name__ == "__main__":
    arr = [10, 20, 10, 5, 15]
    q = (1, 2)
    pre = pre_compute(arr)
    print(range_sum(1, 2, pre))
    print(range_sum(3, 4, pre))
    print()