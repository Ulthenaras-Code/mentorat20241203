from functools import lru_cache
import time
import sys

sys.set_int_max_str_digits(5000000) # type: ignore

# def return_square(x):
#     print(f"Processing {x}")
#     return x * x

# @lru_cache
# def return_square(x):
#     print(f"Processing {x}")
#     return x * x

# @lru_cache(maxsize=3)
# def return_square(x):
#     print(f"Processing {x}")
#     return x * x

# @lru_cache
# def fibonnaci(a, b):
#     start = time.perf_counter()
#     for _ in range(900000):
#         a, b = b, a+b
#     end = time.perf_counter()
#     print(end - start)
#     return b

def my_gen():
    for i in range(10):
        yield i

a = my_gen()
print(next(a))

def my_gen():
    for i in range(10):
        yield i

a = my_gen()
while True:
    try:
        print(next(a))
    except StopIteration:
        print("Il n'y a plus d'item dans l'itérateur")
        break

a = my_gen()

for i in range(10):
    print(next(a))

