import random

def gen_random(num_count, begin, end):
    response = []
    for i in range(num_count):
        response.append(random.randint(begin, end))
    return response
    