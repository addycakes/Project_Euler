def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f

@memo        
def is_prime(num):

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def find_prime(num):
    '''num denotes the nth item of a set
       i.e. num = 100 is the 100th prime number'''
    
    x = []
    y = 2
    while len(x) != num:
        if is_prime(y):
            x.append(y)
        y += 1

    return x[-1:]


