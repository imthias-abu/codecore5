import time

def measure_time(func, *args):
    """
    Runs the given function with arguments and returns the result and time taken.
    """
    start_time = time.time()
    result = func(*args)  # Run the function
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time
if __name__ == "__main__":
    import time

    def dummy_function(n):
        time.sleep(n)
        return n

    result, duration = measure_time(dummy_function, 2)
    print(f"Result: {result}, Time taken: {duration:.2f} seconds")
