## Euclidian div algo:

"""Pusedo code:
gcd(a, b):
    if a = b:
        return a
    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)"""

def gcd(a, b):
    # Everything divides 0
    if a == 0:
        return b
    if b == 0:
        return a
   
   # base condition
    if a == b:
        return a

    if a > b:
        return gcd(a%b, b)
    else:
        return gcd(a, b%a)
   

if __name__ == '__main__':
    a = 98
    b = 56

    print(f"GCD of {a} and {b} is {gcd(a, b)}")


## Time Complexity: O(log(min(a,b))) 
## Auxiliary Space: O(log(min(a,b))) 