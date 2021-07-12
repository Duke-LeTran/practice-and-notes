# https://www.reddit.com/r/ProgrammerHumor/comments/8fdyf0/i_heard_were_brute_forcing_hello_world_now/
# https://imgur.com/KvFcSy5
# https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing

import random
import time
import numpy as np
#from tqdm import tqdm 

from multiprocessing import Pool

def brute_force(word):
    """Pass 'Hello, World' as an example"""
    start_time = time.time()
    target_array = list(word)
    string_array = [""] * len(target_array)
    i = 0
    while i < len(target_array):
        string_array[i] = chr(random.randint(32,126))
        if string_array[i] == target_array[i]:
            i += 1
        print("".join(string_array))
        time.sleep(0.006)
    end_time = time.time() - start_time
    return f'Done! Brute forced {word} took {end_time}.' 

def exponent(x):
    time.sleep(0.006)
    return x**2

def main():
    """
    This provides an example of a random task, ie, brute forcing random letters
    """
    # serial processing
    print("# Serial processing begins.")
    time.sleep(1)
    start_time = time.time()
    ls_words = ['pandas', 'health', 'World']
    for word in ls_words:
        brute_force(word)
    serial_end_time = time.time() - start_time 

    # parallel processing
    print("# Parallel processing begins.")
    time.sleep(1)
    start_time = time.time()
    with Pool(processes=3) as pool:
        result = pool.map(brute_force, ls_words)
    
    parallel_end_time = time.time() - start_time
    print(result)
    print(f'Serial processing time took {serial_end_time}.')
    print(f'Parallel processing time took {parallel_end_time}.')

def main2():
    """
    This provides an example of a more consistent task, ie, exponent
    """
    # serial processing
    print("# Serial processing begins.")
    time.sleep(1)
    start_time = time.time()
    ls_nums = np.linspace(1,1000,1000)
    for num in ls_nums:
        exponent(num)
    serial_end_time = time.time() - start_time 

    # parallel processing
    print("# Parallel processing begins.")
    time.sleep(1)
    start_time = time.time()
    with Pool(processes=3) as pool:
        result = pool.map(exponent, ls_nums)
    
    parallel_end_time = time.time() - start_time
    print(result)
    print(f'Serial processing time took {serial_end_time}.')
    print(f'Parallel processing time took {parallel_end_time}.')



if __name__ == '__main__':
    main2()