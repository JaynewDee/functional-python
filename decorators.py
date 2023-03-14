import time


def generic_decorator(func):
    def modifier(*args):
        return func(*args)
    return modifier


def timer(func):
    """
        \*args allow us to pass any number of anonymous arguments,
        preserving the function's original implementation.
    """
    def wrapper(*args):
        start_time = time.process_time()
        result = func(*args)
        elapsed = time.process_time() - start_time
        print(f"Python: {elapsed:.3f} ")
        return result
    return wrapper


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Getting result from cache for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@timer
@memoize
def cpu_spinner(x):
    values = [x for _ in range(x)]
    return sum(values)


cpu_spinner(100000000)
cpu_spinner(100000000)

"""
Adding authentication to functions:

We can create a decorator function that checks if the user is authenticated before allowing them to execute a function. This can be useful in creating secure APIs or web applications.

python
Copy code
def authenticate_decorator(func):
    def wrapper(*args, **kwargs):
        if is_authenticated():
            return func(*args, **kwargs)
        else:
            raise Exception("User is not authenticated!")
    return wrapper

@authenticate_decorator
def secure_function():
    return "Sensitive information"

def is_authenticated():
    return False

secure_function()
"""
