#!/usr/bin/python
import sys
from collections import Counter

# open password text file
#all_pw = open('LUDS.txt', 'r')
all_pw = open('all-passwords_unique_pw.txt', 'r')
#example_pw = open('example_pw1.txt','r')

# read files into list formatt
compare = all_pw.read().splitlines()
#compare = example_pw.read().splitlines()

final_list = []
length = []

# loop thru list check LUDS
for password in compare:
    # check if the string contains any lowercase letter
    lower = any(data.islower() for data in password)
    #print("lower:\t",lower,password)
    # check if the string contains any uppercase letter
    upper = any(data.isupper() for data in password)
    #print("upper:\t",upper,password)
    # check if the string contains any digit
    digit = any(data.isdigit() for data in password)
    #print("digit:\t",digit,password)
    # check if the string contains any special characters
    if set('[~!@#$%^&*()_+":;\']+$').intersection(password):
        special = "True"
        #print ("special:\t",special,password)
    else:
        special = "False"
    if special == "True" and lower and upper and digit :
        final_list.append(password)
        #print ("append                                                  ",password)


# find total number of unique LUDS passwords
num = len(final_list)
print(' Total number of unique data:',num)

# loop thru list check the LUDS length
for data in final_list:
    length.append(len(data))

#for data in final_list:
#    print(data)

#print(Counter(length))


# output unique LUDS password to file
orig_stdout = sys.stdout
f = open('LUDS.txt', 'w')
sys.stdout = f

# print all LUDS passwords
for data in final_list:
    print(data)

# print the number of occurance
print(Counter(length))

# close output file
sys.stdout = orig_stdout
f.close()
