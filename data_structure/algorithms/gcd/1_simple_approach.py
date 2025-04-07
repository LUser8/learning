## One by One Check
def gcd(a, b):
    # Find the minimum of a and b
    result = min(a, b)

    while True:
        if (a%result == 0) and (b%result == 0):
            break
        result -= 1
    
    # Return the gcd of a and b
    return result


if __name__ == '__main__':
    a = 97
    b = 56

    print(f"GCD of {a} and {b} is {gcd(a, b)}")


## Time Complexity: O(min(a,b)) 
## Auxiliary Space: O(1)