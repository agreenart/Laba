import time
def check_time(func):
    def run(*args, **kwargs):
        start_time = time.clock()
        func(*args, **kwargs)
        end_time = time.clock()
        return end_time - start_time
    return run
