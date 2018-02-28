#!/usr/bin/python
import sys, getopt
import itertools
from random import *

# variables

final_list = []
leet_list = []
substring_list = []
flatten_list = []
all_combo_list = []
counter = 0
element = 0

# Function definition

# check leet for passed char
def leetPerChar(inputChar,return_list):
    sysmbol_list = {
        "a": ["A","a","4","@","^"],
        "b": ["B","8","b","6"],
        "c": ["C","c","(","<","[","{"],
        "d": ["D","d","B","b"],
        "e": ["E","e","3","M","m"],
        "f": ["F","f","4"],
        "g": ["G","g","6","9","&"],
        "h": ["H","h","|-|","#"],
        "i": ["I","!","1","|","l","L","i"],
        "j": ["J","j","7"],
        "k": ["K","k","x",],
        "l": ["L","l","1","7",],
        "m": ["M","m","3","w","nn","W"],
        "n": ["N","n","2"],
        "o": ["O","o","0","()","[]","*"],
        "p": ["P","p","9","6","q"],
        "q": ["Q","q","9","b",],
        "r": ["R","r","2"],
        "s": ["S","s","5","$","z","2"],
        "t": ["T","t","7","+"],
        "u": ["U","u","v","V"],
        "v": ["V","v","u","U","^","7",">","<"],
        "w": ["W","w","m","vv","M"],
        "x": ["X","x","%","><","*"],
        "y": ["Y","y","j","^"],
        "z": ["Z","z","2","7"],
        "A": ["A","a","4","@","^"],
        "B": ["B","8","b","6"],
        "C": ["C","c","(","<","[","{"],
        "D": ["D","d","B","b"],
        "E": ["E","e","3","M","m"],
        "F": ["F","f","4"],
        "G": ["G","g","6","9","&"],
        "H": ["H","h","|-|","#"],
        "I": ["I","!","1","|","l","L","i"],
        "J": ["J","j","7"],
        "K": ["K","k","x",],
        "L": ["L","l","1","7",],
        "M": ["M","m","3","w","nn","W"],
        "N": ["N","n","2"],
        "O": ["O","o","0","()","[]","*"],
        "P": ["P","p","9","6","q"],
        "Q": ["Q","q","9","b",],
        "R": ["R","r","2"],
        "S": ["S","s","5","$","z","2"],
        "T": ["T","t","7","+"],
        "U": ["U","u","v","V"],
        "V": ["V","v","u","U","^","7",">","<"],
        "W": ["W","w","m","vv","M"],
        "X": ["X","x","%","><","*"],
        "Y": ["Y","y","j","^"],
        "Z": ["Z","z","2","7"],
        "0": ["0","o","O","zero","*"],
        "1": ["1","won","one","l","|","][","I","i","L"],
        "2": ["two","to","too","2","z","Z"],
        "3": ["e","3","three","E"],
        "4": ["4","four","for","fore","a","A"],
        "5": ["5","five","s","S"],
        "6": ["6","six","g","b","B"],
        "7": ["7","seven","t","l","T","L"],
        "8": ["8","eight","b","B"],
        "9": ["9","nine","g","q","Q"]
    }
    for symbol in inputChar:
		if sysmbol_list.has_key(symbol):
			return_list = sysmbol_list[symbol]
    return return_list



# merge mulit demension list into one list
def flatten(input_List):
    for element in input_List:
        if type(element) in (tuple, list):
            for i in flatten(element):
                yield i
        else:
            yield element


# compare combinations with all-passwords_unique_pw
def comapreCombo(combo_list,data_list,total,return_list):
    total = 0
    for combo in combo_list:
        if combo in data_list:
            return_list.append(combo)
            total = total + 1
    return total


#*******************************************************************#
# main program

# open text file
text_file = open('all-passwords_unique_pw.txt', 'r')

# read file into list formatt
read_file = text_file.read().splitlines()

# store readed in arg to input_string
input_string = sys.argv[1]
# find length of input_string
stringLen = len(sys.argv[1])



# check argument length
if stringLen < 3:
    print'Argument not accepted'
else:

    print'Argument accepted'
    print 'Argument length <=3: ', stringLen


# find leet sysbols from input_string & store to leet_list
counter = 0
while counter < stringLen :
    temp_list = []
    temp_list = leetPerChar(input_string[counter],temp_list)
    leet_list.append(temp_list)
    counter = counter + 1


# for finding combinations
flatten_list = list(flatten(leet_list))


all_combo_list = list(itertools.combinations(flatten_list,stringLen))

# find length of all_combo_list
combo_listLen = len(all_combo_list)


counter = 0
element = 0
# find correct combinations
while (counter < combo_listLen ):
    #print " index @ 1st while : [",counter,"][",element,"]"
    #counter = counter
    # while 1st element is in leet_list[1st element]
    while (all_combo_list[counter][element] in leet_list[element]):
        #print " index @       while     :[",counter,"][",element,"]"
        # found all element in corresponding list
        if element == (stringLen - 1):
            # add combo to substring_list
            substring_list.append(''.join(all_combo_list[counter]))
            #print " index @       if     :[",counter,"][",element,"]"
            #print all_combo_list[counter]
            #reset element
            element = 0
            # check next combo
            counter = counter + 1

        # check next element
        element = element + 1
        #print " index @                               :[",counter,"][",element,"]"
    # check if next element is NOT corresponding list
    if all_combo_list[counter][element] not in leet_list[element]:
        # check next combo
        counter = counter + 1
        # reset element
        element = 0
        #print " index @         end all loop                      :[",counter,"][",element,"]"

# print all substring
for data in substring_list:
    print(data)


num = len(substring_list)
print(' Total number of substring combinations:',num)

found_num_combo = 0
found_num_combo = comapreCombo(substring_list,read_file,found_num_combo,final_list)


# print all final_list
for data in final_list:
    print(data)

print "Total: ", found_num_combo
