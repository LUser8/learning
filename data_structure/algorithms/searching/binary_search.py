from timer import timer

@timer
def search(a, target):
    low = 0
    high = len(a) - 1 

    while low <= high:
        mid = (high + low) // 2
        if a[mid] ==  target:
            return target
        if a[mid] > target:
            high = mid - 1
        else: 
            low = mid + 1
    else:
        return -1


if __name__ == '__main__':
    arr = range(1, 1000000000000)
    target = 99999999999
    res = search(arr, target)
    if res!= -1:
        print("Element present in array")
    else:
        print("Element not present in array")