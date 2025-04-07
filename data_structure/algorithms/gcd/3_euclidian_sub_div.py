## Euclidian Substract divide algo:

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
        if a % b == 0:
            return b
        return gcd(a-b, b)
    else:
        if b % a == 0:
            return a
        return gcd(a, b-a)
   

if __name__ == '__main__':
    a = 98
    b = 56

    print(f"GCD of {a} and {b} is {gcd(a, b)}")


## Time Complexity: O(min(a,b)) 
## Auxiliary Space: O(min(a,b)) because it uses internal stack data structure in recursion.