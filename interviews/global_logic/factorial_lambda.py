# factorial using lambda function
from functools import reduce
# factorial = lambda n: 1 if n==0 else reduce(lambda x, y: x*y, range(1, n+1))

print(reduce(lambda x, y: x*y, range(1, 6)))