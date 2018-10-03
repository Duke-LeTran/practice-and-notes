import pandas as pd
import numpy as np
import collections

#returns the greatest common factor
def gcf (num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    for x in range (num1, 0, -1):
        if num1 % x == 0 and num2 % x == 0:
            return x

#returns the least common mutiple
def lcm(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    for x in range (num2, num1 * num2 + 1, num2):
        if x % num1 == 0:
            return x

def print_exp_primes(ls_primes):
    ls_result = []
    c = collections.Counter(ls_primes)
    for k,v in c.items():
        ls_result.append(str(k) + '^' + str(v))
    print("As exponents:", ls_result)

# DataFrame of primes
d = {'col1': [11, np.nan, 31, 41, np.nan, 61, 71, np.nan, np.nan, 101], 
     'col3': [13, 23, np.nan, 43, 53, np.nan, 73, 83, np.nan, 103],
          'col7': [17, np.nan, 37, 47, np.nan, 67, np.nan, np.nan, 97, 107],
               'col9': [19, 29, np.nan, np.nan, 59, np.nan, 79, 89, np.nan, 109]}

df = pd.DataFrame(data=d)

def print_primes(ordered=False):
    if ordered:
        print("##### Misc. Patterns")
        print(1, 3, 5, 7, "//", 11, 13, 17, 19)
        print(101, 103, 107, 109, 113)
        print("##### 3-9 Pattern")
        print(23, 29)
        print(53, 59)
        print(83, 89, "//87=1*3*29")
        print("##### 1-7 Pattern")
        print(31, 37)
        print(61, 67)
        print("X", 97)
        print("###### 1-3-7/9* Pattern")
        print(41, 43, 47)
        print(71, 73, 79)
        print("####### End")
    else:
        for i,j in df.iterrows():
        	print(j.dropna(how='all').apply(lambda x: int(x)).tolist())

def primes(n):
    ls_primes = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            ls_primes.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        ls_primes.append(n)
    #print
    print_exp_primes(ls_primes)
    return ls_primes

# Times Table
ls_15 = []
for i in range(1, 16):
    ls_15.append(i)

df_tt=pd.DataFrame(index=range(1,16), columns=range(1,16), dtype=np.int64)
for i in ls_15:
    ls_temp = []
    for j in ls_15:
            ls_temp.append(i*j)
    df_tt.iloc[:,i-1] = ls_temp

def print_tt():
    for row in range(1,16):
        print(("{:3}".format(row*col)
            for col in range(1, 18)))


