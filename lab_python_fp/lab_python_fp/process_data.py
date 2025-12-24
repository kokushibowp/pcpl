import json
import sys
from time import time
from functools import wraps
import chardet

def print_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

class cm_timer_1:
    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Время работы: {time() - self.start_time:.4f} сек")

path = sys.argv[1]

with open(path, 'rb') as f:
    result = chardet.detect(f.read(10000))
    encoding = result['encoding']

with open(path, encoding=encoding) as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(set(job['job-name'].lower() for job in arg if 'job-name' in job), key=str.lower)

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    import random
    salaries = [random.randint(100000, 200000) for _ in arg]
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(arg, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
