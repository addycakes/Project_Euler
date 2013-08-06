import math

def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

def is_prime(num):

    for i in range(2, (int(math.sqrt(num)))+1):
        if num % i == 0:
            return False
    return True

prime = memo(is_prime)

def sum_primes_below(num):
    '''the sum of all primes below the number num'''

    primes = []

    for i in range(2, num):
        if prime(i):
            primes.append(i)
    return sum(primes)

print(sum_primes_below(2000000))
