'''
Created on 28 Sep 2015

@author: chris
'''
import multiprocessing as mp
import random
import string

# Define an output queue
output = mp.Queue()

# define a example function
def rand_string(length, output):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    rand_str = ''.join(random.choice(
                    string.ascii_lowercase
                    + string.ascii_uppercase
                    + string.digits)
               for _ in range(length))
    output.put(rand_str)

# Setup a list of processes that we want to run
processes = [mp.Process(target=rand_string, args=(5, output)) for x in range(4)]

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

# Get process results from the output queue
results = [output.get() for p in processes]

print(results)


# import concurrent.futures
# import math
# import time
# 
# PRIMES = [
#     1122725350952935,
#     1125827059421715,
#     1122725350952935,
#     1152800951907735,
#     1157978480770995,
#     1099726899285419]
# 
# def is_prime(n):
#     if n % 2 == 0:
#         return False
# 
#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in range(3, sqrt_n + 1, 2):
#         if n % i == 0:
#             return False
#     return True
# 
# def main():
#     
#     start = time.time()
#     
#     with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
#         for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
#             print('%d is prime: %s' % (number, prime))
#             
#     end = time.time()
#     
#     print end - start
# 
# if __name__ == '__main__':
#     main()