def find_prefix_sum(arr):
    n = len(arr)
    prefix_sum = [0] * n

    prefix_sum[0] = arr[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    
    return prefix_sum

if __name__ == "__main__":
    arr = [10, 20, 10, 5, 15]
    prefixSum = find_prefix_sum(arr)
    for i in prefixSum:
        print(i, end=" ")
    print()