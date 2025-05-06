from timer import timer

@timer
def search(a, target):
    for i in a:
        if i == target:
            return i
    else:
        return -1


if __name__ == '__main__':
    arr = range(1, 100000)
    target = 9999999999
    res = search(arr, target)
    if res!= -1:
        print("Element present in array")
    else:
        print("Element not present in array")