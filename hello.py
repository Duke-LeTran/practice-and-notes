import os
import readline
import datetime
import collections
import pandas as pd
import numpy as np

#READ ME
# You just set your bash env variables, i.e., 


# prints current directory; option of returning list (but buggy)
def ls():
	x = os.listdir('.')
	print('Current Directory:')
	for index, file in enumerate(x):
		print(index, file)
	user = input("Return List? (y/n): ")
	if user is ('y' or 'Y' or 'Yes'):
		return x
	else:
		return
# cd()
def cd(direc):
	os.chdir(direc)

# pwd()
def pwd():
	os.system('pwd')

#prints last few python lines
def history(len):
	n = readline.get_current_history_length()
	ls_x = []
	for index, i in enumerate(range(n-len, n)):
		x = str(readline.get_history_item(i + 1))
		print(i , x)
		ls_x.append(x)
	user = input("Print to text log? (y/n): ")
	if user is ('y' or 'Y' or 'Yes'):
		file_path = '/Users/dukeletran/.pyscripts/python_cmd_hx.log'
		if os.path.exists(file_path):
			append_write = 'a'
		else:
			append_write = 'w'
		print('####This log was requested: ', datetime.datetime.now())
		s = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		f = open(file_path, append_write)
		f.write('This log was requested: ' + s + '\n' + \
			'\n'.join(ls_x) +'\n' +'####END' + '\n')
		f.close()
		user = input("Open file? (y/n): ")
		if user is ('y' or 'Y' or 'Yes'):
			os.system('subl ' + file_path)

#list all new variables
def ls_v():
	return [i for i in globals() if '__' not in i]


# runs file, input: file name; NOTE: globals does not work. variables are out of scope as soon as function returns
def run(file_name):
	exec(open(file_name).read(), globals())

# returns a new list of non-unique values from list, i.e., repeats
def not_unique(mylist): 
	myset = set()
	dups = set()
	for x in mylist:
		if x in myset:
			dups.add(x)
		else:
			myset.add(x)
	dups = list(dups)
	return dups

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

def print_primes():
    print(1, 3, 4, 7, "//", 11, 13, 17, 19)
    print(23, 29) # 3/9 pattern
    print(31, 37) # 1/7 pattern
    print(41, 43, 47) # 49 is divisible by 7
    print(53, 59) # 3/9 pattern
    print(61, 67) # 1/7 pattern
    print(71, 73, 79) # 77 is divisible by 11
    print(83, 89) # 87 is divisible by 3 (8+7 is 15)
    print(97)
    print(101, 103, 107, 109, 113)

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
            for col in range(1, 16)))