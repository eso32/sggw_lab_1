import time

def timed(func):
    def wrapper(self, *args, **kwargs):
        start = time.perf_counter()
        result = func(self, *args, **kwargs)
        end = time.perf_counter()
        print(f"Time: {end - start:.6f} s")
        return result
    return wrapper