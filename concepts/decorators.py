from functools import wraps

"""
1. Basic Decorator Without Arguments
Structure:
- A decorator function wraps a target function (func).
- The target function is wrapped using an inner wrapper function that performs the desired logic.
Steps:
1. Define the decorator function (outer function).
2. Inside the decorator, define a wrapper function to wrap the original function.
3. The wrapper modifies or enhances the original function’s behavior.
4. Return the wrapper.
"""


def basic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result

    return wrapper


@basic_decorator
def example_function():
    print("Inside the function")


# Call the function
example_function()


"""
2. Decorator with Arguments
When a decorator needs arguments, you must add an extra layer of wrapping because now you're passing arguments to the decorator itself (not just the function).

Structure:
- First Layer: A function that accepts decorator arguments.
- Second Layer: The actual decorator function that takes the target function as an argument.
- Third Layer: A wrapper function that performs the desired behavior and calls the original function.
Steps:
1. Define the outer function that accepts arguments for the decorator.
2. Inside this, define the actual decorator function (just like the basic decorator).
3. Inside the decorator, define the wrapper function to enhance the original function.
4. Return the decorator from the outer function.
"""


def decorator_with_args(arg1, arg2):  # Outer function with decorator arguments
    def actual_decorator(func):  # The real decorator
        @wraps(func)
        def wrapper(*args, **kwargs):  # The wrapper function
            print(f"Decorator arguments: {arg1}, {arg2}")
            print("Before the function call")
            result = func(*args, **kwargs)
            print("After the function call")
            return result

        return wrapper

    return actual_decorator


@decorator_with_args("hello", 42)
def example_function():
    print("Inside the function")


# Call the function
example_function()


# Examples:
def cache(func):
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key based on the function arguments
        key = (args, frozenset(kwargs.items()))
        if key in cached_results:
            print("Returning cached result")
            return cached_results[key]
        else:
            result = func(*args, **kwargs)
            cached_results[key] = result
            return result

    return wrapper


@cache
def example_function(x, y):
    print(f"Calculating {x} + {y}")
    return x + y


import time

from functools import wraps


def retry(retries=3, delay=1):
    def decorator_retry(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(
                        f"Attempt {attempt} failed: {e}. Retrying in {delay} seconds..."
                    )
                    time.sleep(delay)
            # If all retries fail, raise the last exception
            raise last_exception

        return wrapper

    return decorator_retry


@retry(retries=3, delay=1)
def example_function():
    # Example function that may fail
    raise ValueError("An error occurred!")


# Call the function
example_function()
