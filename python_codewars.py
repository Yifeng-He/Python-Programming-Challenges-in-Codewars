#******************************************************************************
# Probelm 1:
# convert a string into a string of their positions 
# for example, given input: 'ab cd', the output should be '12 34'
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# the function
def string_to_integer(input_str):
    list1=list(input_str);
    list2=[]
    start=ord('a')-1
    for s in list1:
        if s.isalpha():
            list2.append(str(ord(s)-start))
    return ' '.join(list2)

# testing           
input="This is a test?"
list3=string_to_integer(input.lower())
print(list3)
#******************************************************************************

#******************************************************************************
# Probelm 2:
# If a club member is over 55 years old and has won more than 7 times, the status 
# is 'Senior', otherwise, the status is 'Open'.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++   
     
# function to determine open or senior
def openOrSenior(data):
    list1=[]
    for item in data:
        if item[0] >= 55 and item[1] > 7:
            list1.append("Senior")
        else:
            list1.append("Open") 
    return(list1) 

# testing
aa=[[45, 12],[55,21],[19, -2],[104, 20]]
print(openOrSenior(aa))
#******************************************************************************


#******************************************************************************
# Probelm 3:
# You can walk toward four directions (N, S, E, W), and it takes 1 min to walk 
# along a street block. You have exactly 10 minutes. Given the input of walking
# instrcutions, return 'True' if you arrive the starting point after 10 minutes,
# otherwise, return 'False'.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++  

# the function to determine if you return to the starting point after 10 minutes
def isValidWalk(walk):
    map1={'n':-1, 's':1, 'e':-2, 'w':+2}
    list1=[]
    for s in walk:
        list1.append(map1[s])
    if len(list1)==10 and sum(list1)==0:
        return True
    else:
        return False

# testing
test1=['n','e','n','e','s','e','s','w','w','w']
print(isValidWalk(test1))
test2=['n','e','n','e','s','e','s','w','e','w']
print(isValidWalk(test2))
#******************************************************************************


#******************************************************************************
# Probelm 4:
# You are give a series of numbers, in which there is one number is different
# from the others in terms of odd or even number. Find the location of the unique
# number.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++  

# function to find the location of the unique number
def iq_test(numbers):
    # input is a tring
    list1=numbers.split(" ")
    list2=[int(s) for s in list1]
    list3=[s%2 for s in list2]
    if sum(list3) > 1:
        list4=[1-s for s in list3]
    else:
        list4=list3
    ind=0
    for k in list4:
        if k==1:
            return (ind+1)
        else:
            ind=ind+1
            
# testing
test2="4 9 2 2"
print(iq_test(test2))
#******************************************************************************


#******************************************************************************
# Probelm 5:
# You are give a series of numbers, and asked to find the max and min numbers.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# fundtion to find the highest and the lowest number
def high_and_low(numbers):
    # input is a string
    list1=numbers.split(" ")
    list2=[int(s) for s in list1]
    max_num=max(list2)
    min_num=min(list2)
    str1=' '.join([str(max_num), str(min_num)])
    return(str1)

    # testing
test3="4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
print(high_and_low(test3))
#******************************************************************************


#******************************************************************************
# Probelm 6: Sum of two lowest positive integers
# Create a function that returns the sum of the two lowest positive numbers given 
# an array of minimum 4 integers. No floats or empty arrays will be passed.
# For example, when an array is passed like [19,5,42,2,77], the output should be 7.
# [10,343445353,3453445,3453545353453] should return 3453455.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# function
def sum_two_smallest_numbers(numbers):
    # input is a list of integers
    list1=[s for s in numbers if s>0]
    min_num1=min(list1)
    list2=[s for s in list1 if s>min_num1]
    min_num2=min(list2)
    return(min_num1+min_num2)

# testing
test4=[5, 8, 12, 18, 22]
print(sum_two_smallest_numbers(test4))
#******************************************************************************


#******************************************************************************
# Probelm 7: Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 
# below the number passed in. 
# Note: If the number is a multiple of both 3 and 5, only count it once.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def solution(number):
    list1=range(1,number)
    list2=[]
    for s in list1:
        if s%3 == 0:
            list2.append(s)
        else:
            if s%5==0:
                list2.append(s)
    
    return (sum(list2))

# testing
print(solution(10))
#******************************************************************************


#******************************************************************************
# Probelm 8: 
# Write a function called validParentheses that takes a string of parentheses, 
# and determines if the order of the parentheses is valid. 
# validParentheses should return true if the string is valid, and false if it's invalid.
# Examples:
# validParentheses( "()" ) => returns true
# validParentheses( ")(()))" ) => returns false
# validParentheses( "(" ) => returns false
# validParentheses( "(())((()())())" ) => returns true
# All input strings will be nonempty, and will only consist of open parentheses 
# '(' and/or closed parentheses ')'
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def validParentheses(str1):
    list1=list(str1)
    maps={'(':1,')':-1}
    list2=[]
    for s in list1:
        list2.append(maps[s])
    temp=0
    for s in list2:
        temp=temp+s;
        if temp<0:
            return False
    return True

# testing
test_a1="()"
test_a2="(())((()())())"
test_a3=")(()))"
print(validParentheses(test_a1))
print(validParentheses(test_a2))
print(validParentheses(test_a3))
#******************************************************************************


#******************************************************************************
# Probelm 9: Equal Sides Of An Array
# You are going to be given an array of integers. Your job is to take that 
# array and find an index N where the sum of the integers to the left of N is 
# equal to the sum of the integers to the right of N. If there is no index that 
# would make this happen, return -1.
# For example:
# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array, 
# the sum of left side of the index ({1,2,3}) and the sum of the right side of 
# the index ({3,2,1}) both equal 6.
# Note: Please remember that in most programming/scripting languages the index of
#  an array starts at 0.
# Input: An integer array of length 0 &lt; arr &lt; 1000. The numbers in the array 
# can be any integer positive or negative.
# Output: The lowest index N where the side to the left of N is equal to the side 
# to the right of N. If you do not find an index that fits these rules, then you 
# will return -1.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def equalSize(arr):
    for i in range(0,len(arr)):
        list_left=arr[:i]
        list_right=arr[i+1:]
        if int(sum(list_left))==int(sum(list_right)):
            return i
    return -1

# testing    
input_a1=[1,2,3,4,3,2,1]
input_a2=[1,100,50,-51,1,1] 
input_a3=[10,-80,10,10,15,35,20]
print(equalSize(input_a1))
print(equalSize(input_a2))
print(equalSize(input_a3))  
#******************************************************************************


#******************************************************************************
# Probelm 10: Directions Reduction
'''
Once upon a time, on a way through the old wild west,…
a man was given directions to go from one point to another. The directions were 
"NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, 
"WEST" and "EAST" too. Going to one direction and coming back the opposite direction 
is a needless effort. Since this is the wild west, with dreadfull weather and 
not much water, it's important to save yourself some energy, otherwise you might 
die of thirst! How I crossed the desert the smart way.

The directions given to the man are, for example, the following:
plan = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST'].
You can immediatly see that going "NORTH" and then "SOUTH" is not reasonable, 
better stay to the same place! So the task is to give to the man a 
simplified version of the plan. A better plan in this case is simply:
plan = ['WEST']
Other examples: In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" 
is going north and coming back right away. 
What a waste of time! Better to do nothing. The path becomes ["EAST", "WEST"], 
now "EAST" and "WEST" annihilate each other, 
therefore, the final result is [] (nil in Clojure). 
In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are 
not directly opposite but they become directly opposite after the 
reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].
Task:
You have to write a function dirReduc which will take an array of strings and 
returns an array of strings with the needless directions removed (W<->E or S<->N 
side by side).The Haskell version takes a list of directions with data Direction 
= North | East | West | South. The Clojure version returns nil when the path is 
reduced to nothing.
Examples
dirReduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']) =&gt; ['WEST']
dirReduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH']) =&gt; []

Note
All paths can't be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is 
not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not 
directly opposite of each other and can't become such. Hence the result path is 
itself : ["NORTH", "WEST", "SOUTH", "EAST"].
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def dirReduc(arr):
    # define matched pairs
    map1={'NORTH':'SOUTH', 'SOUTH':'NORTH', 'EAST':'WEST', 'WEST':'EAST'}    
    list1=arr
    list2=[1]*len(list1)
    while True:
        cancellation =0
        for i in range(0,len(list1)-1):
            if list2[i]>0 and map1[list1[i]]==list1[i+1]:
                list2[i]=0
                list2[i+1]=0
                cancellation =1
        
        # shrink list1
        list3=[]
        for j in range(0,len(list2)):
            if list2[j]>0:
                list3.append(list1[j])
        list1=list3
        list2=[1]*len(list1)
         # determine if quit
        if cancellation==0:
             break
    
    return list1

# testing                
test1=['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']
print( dirReduc(test1))
test2=['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH']
print( dirReduc(test2))           
test3=["NORTH", "WEST", "SOUTH", "EAST"]
print( dirReduc(test3))         
#******************************************************************************



#******************************************************************************
# Probelm 11: Is Prime
'''
Define a function isPrime that takes one integer argument and returns true or 
false depending on if the integer is a prime. Per Wikipedia, a prime number 
(or a prime) is a natural number greater than 1 that has no positive divisors 
other than 1 and itself.
Example
isPrime(5)
=&gt; true
Assumptions: You can assume you will be given an integer input. You can not assume 
that the integer will be only positive. You may be given negative numbers.

The Haskell version uses a wrong test case, where negative primes should also 
return True, e.g. it expects isPrime (-2) == True. 
Use abs or similar measures to take care of negative numbers. The test cases 
cannot get changed at this point. Sorry for the inconvenience.
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
def isPrime(num):
    num1=abs(num) 
    if num1>1:
        if num1==2:
            return True
        else:          
            for i in range(2,num1):
                if num1 % i ==0:
                    return False
    else:
        return False
    
    return True

# testing
test1=6;
print(isPrime(test1))
#******************************************************************************


#******************************************************************************
# Probelm 12: 
'''
Your job is to create a calculator which evaluates expressions in Reverse Polish 
notation. For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 
5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.
Note that for simplicity you may assume that there are always spaces between 
numbers and operations, e.g. 1 3 + expression is valid, but 1 3+ isn't.
Empty expression should evaluate to 0.
Valid operations are +, -, *, /.
You may assume that there won't be exceptional situations (like stack underflow 
or division by zero).
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def calc(expr):
    # input is string
    list1=expr.split()
    if len(list1)==0:
        return 0
    while True:
        for i in range(0,len(list1)):
            ind=0
            if list1[i].replace('.','',1).isdigit() == False:
                print(list1[i])
                ind=1
                if list1[i]=='+':
                    temp1 = int(list1[i-2]) + int(list1[i-1])
                    break;
                elif list1[i]=='-':
                    temp1 = int(list1[i-2]) - int(list1[i-1])
                    break;
                elif list1[i]=='*':
                    temp1 = int(list1[i-2]) * int(list1[i-1])
                    break;
                elif list1[i]=='/':
                    temp1 = float(list1[i-2]) / float(list1[i-1])
                    break;
                else:
                    print("nothing")                        
        # update the list
        if ind==1:
            list_a=[]
            list_a.append(str(temp1))
            list2=list1[0:i-2] + list_a + list1[i+1:]
            list1=list2
            # check if it is done
            if len(list1) == 1:
                return float(list1[0])
        else:
            return float(list1[-1])

# testing
test1="4 2 /"
print(calc(test1))
#******************************************************************************


#******************************************************************************
# Probelm 13: 
'''
Complete the method/function so that it converts dash/underscore delimited words 
into camel casing. The first word within the output 
should be capitalized only if the original word was capitalized.
Examples:
# returns "theStealthWarrior"
to_camel_case("the-stealth-warrior") 
# returns "TheStealthWarrior"
to_camel_case("The_Stealth_Warrior")
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            
def to_camel_case(text):
    list1=list(text)
    if len(list1)==0:
        return ''
    for i in range(0,len(list1)):
        if list1[i]=='-' or list1[i]=='_':
            list1[i+1]=list1[i+1].upper()
    list1=[s for s in list1 if s!='-' and s!='_']
    return ''.join(list1)
    
# testing
test1="the_stealth_warrior"
print( to_camel_case(test1))
#******************************************************************************



#******************************************************************************
# Probelm 14: 
''' 
My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried 
because each month a list with the weights of members is published and each month 
he is the last on the list which means he is the heaviest. I am the one who 
establishes the list so I told him: "Don't worry any more, I will modify the 
order of the list". It was decided to attribute a "weight" to numbers. The weight 
of a number will be from now on the sum of its digits. For example 99 will have 
"weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. 
Given a string with the weights of FFC members in normal order can you give this 
string ordered by "weights" of these numbers?
Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 
56 65 74 68 86 99" When two numbers have the same "weight", let us class them as 
if they were strings and not numbers: 100 is before 180 because its "weight" (1) 
is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" 
(9) it comes before as a string. All numbers in the list are positive numbers 
and the list can be empty.
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def order_weight(strng):
    list1=strng.split(' ')
    if len(list1)==0:
        return ''
    list_weight=[]
    ind=0
    for s in list1:
        ind=ind+1
        list_num=list(s)
        # convert to int
        list_num=[int(k) for k in list_num]
        list_weight.append((sum(list_num), ind))
    # order based on weight
    list_weight.sort(key=lambda x: x[0]) 
    # order the original numbers
    list2=[list1[m-1] for (w,m) in list_weight]
    # return a string
    return ' '.join(list2)

# testing
test1="2000 10003 1234000 44444444 9999 11 11 22 123"
print(order_weight(test1))
#******************************************************************************


#******************************************************************************
# Probelm 15: 
''' 
Where my anagrams at? What is an anagram? Well, two words are anagrams of each 
other if they both contain the same letters. For example:
'abba' &amp; 'baab' == true
'abba' &amp; 'bbaa' == true
'abba' &amp; 'abbba' == false
Write a function that will find all the anagrams of a word from a list. You will 
be given two inputs a word and an array with words. You should return an array 
of all the anagrams or an empty array if there are none. For example:
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) =&gt; ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) =&gt; ['carer', 
'racer'] anagrams('laser', ['lazing', 'lazy',  'lacer']) =&gt; []
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def anagrams(word, words):
    #the query word
    list_chars=list(word)
    result=[]
    for s in words:
        list_b=[[p,1] for p in list_chars]
        list_1=list(s)
        if len(list_1) != len(list_b):
           continue
           
        list_1=[[m,1] for m in list_1]
        for k in range(0,len(list_b)):
            for i in range(0,len(list_1)):
               if list_1[i][1] > 0:
                   if list_b[k][0]==list_1[i][0]:
                       list_1[i][1]=0
                       list_b[k][1]=0
                       break
        
        # check this word
        print(list_b)
        print(list_1)
        list_temp=[j for (h,j) in list_b]
        if sum(list_temp)==0: 
            # matched
            result.append(s)
    return result

# testing                       
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
#******************************************************************************


#******************************************************************************
# Probelm 16: The observed PIN
''' 
Alright, detective, one of our colleagues successfully observed our target person, 
Robby the robber. We followed him to a secret warehouse, where we assume to find 
all the stolen stuff. The door to this warehouse is secured by an electronic 
combination lock. Unfortunately our spy isn't sure about the PIN he saw, when 
Robby entered it.
The keypad has the following layout:
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘

He noted the PIN 1357, but he also said, it is possible that each of the digits 
he saw could actually be another adjacent digit (horizontally or vertically, 
but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. 
And instead of the 5 it could also be the 2, 4, 6 or 8. He also mentioned, he 
knows this kind of locks. You can enter an unlimited amount of wrong PINs, 
they never finally lock the system or sound the alarm. That's why we can try 
out all possible (*) variations.
* possible in sense of: the observed PIN itself and all variations considering 
the adjacent digits. Can you help us to find all those variations? It would be 
nice to have a function, that returns an array of all variations for an observed PIN 
with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python). 
But please note that all PINs, the observed one and also the results, must be strings, 
because of potentially leading '0's. We already prepared some test cases for you.
''' 
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      
def get_pins(observed):
    # input: '12'
    dict1={'1':['1','2','4'], '2':['1', '2', '3', '5'], '3':['2','3','6'], '4':['1','4','5','7'],
    '5':['2','4','5','6','8'],'6':['3','5','6','9'],'7':['4','7','8'],'8':['0','5','7','8','9'], 
    '9':['6','8','9'],'0':['0','8']}
    digits=list(observed)
    combination=dict1[digits[0]]
    for i in range(1, len(digits)):
        temp=[]
        d=dict1[digits[i]]
        for s1 in combination:
            for s2 in d:
                temp.append(s1+s2)
                #print(temp)
        combination=temp
        
    return combination

# testing
print(get_pins('11'))
#******************************************************************************



#******************************************************************************
# Probelm 17: Valid Braces
''' 
Write a function called validBraces that takes a string of braces, and determines 
if the order of the braces is valid. validBraces should return true if the string 
is valid, and false if it's invalid. This Kata is similar to the Valid Parentheses 
Kata, but introduces four new characters. Open and closed brackets, and open and 
closed curly braces. Thanks to @arnedag for the idea!
All input strings will be nonempty, and will only consist of open parentheses '(' , 
closed parentheses ')', open brackets '[', closed brackets ']', 
open curly braces '{' and closed curly braces '}'.
What is considered Valid? A string of braces is considered valid if all braces 
are matched with the correct brace.
For example:
'(){}[]' and '([{}])' would be considered valid, while '(}', '[(])', and '[({})](]' 
would be considered invalid.
Examples:
validBraces( "(){}[]" ) => returns true
validBraces( "(}" ) => returns false
validBraces( "[(])" ) => returns false
validBraces( "([{}])" ) => returns true
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def validBraces(string):
    # input: '[(])'
    dict1={')':'(', ']':'[', '}':'{'}
    set_start=['(','[','{']
    list1=list(string)
    tracker=[]
    for s in list1:
        if s in set_start:
            tracker.append(s)
        else:
            if len(tracker)==0:
                return False
            else:
                top=tracker[-1]
                if dict1[s]==top:
                    tracker=tracker[:-1] # delete the top item
                else:
                    return False
    if not tracker: # check if it is empty
        return True
    else:
        return False

# test
print(validBraces("[()]"))
#******************************************************************************


#******************************************************************************
# Probelm 18: Recover a secret string from random triplets
''' 
There is a secret string which is unknown to you. Given a collection of random 
triplets from the string, recover the original string. A triplet here is defined 
as a sequence of three letters such that each letter occurs somewhere before the 
next in the given string. "whi" is a triplet for the string "whatisup".
As a simplification, you may assume that no letter occurs more than once in the 
secret string. You can assume nothing about the triplets given to you other than 
that they are valid triplets and that they contain sufficient information to deduce 
the original string. In particular, this means that the secret string will never 
contain letters that do not occur in one of the triplets given to you.
'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def recoverSecret(triplets):
    '''
    ['t','u','p'],
    ['w','h','i'],
    ['t','s','u'],
    ['a','t','s'],
    ['h','a','p'],
    ['t','i','s'],
    ['w','h','s']
    '''
    list1=[]
    for s in triplets:
       list1=list1+s
    # distinct elements
    list2=list(set(list1))
    # dictionary containing parent and child
    dict1={}
    for s in list2:
        parent=[]
        child=[]
        dict1[s]=(parent, child)
    # fill in dictionary
    for arr in triplets:
        # the second element is the child of the first one
        if arr[1] not in dict1[arr[0]][1]:
            dict1[arr[0]][1].append(arr[1])
        # the third element is the child of the second one
        if arr[2] not in dict1[arr[1]][1]:
            dict1[arr[1]][1].append(arr[2])
        # the first element is the parent of the second one
        if arr[0] not in dict1[arr[1]][0]:
            dict1[arr[1]][0].append(arr[0])
        # the second element is the parent of the third one
        if arr[1] not in dict1[arr[2]][0]:
            dict1[arr[2]][0].append(arr[1])  
    # find the string
    str_found=[]
    while len(str_found)<len(list2):
        if len(str_found)==len(list2):
            break
        for (m,n) in dict1.items():
            if len(n[0])==0 and m not in str_found:
                str_found.append(m)
                # update dict1: remove m from parent list
                for (m1, n1) in dict1.items():
                    if m in n1[0]:
                        n1[0].remove(m)    
    return ''.join(str_found)

# testing 
test1=[ ['t','u','p'],['w','h','i'],
    ['t','s','u'],
    ['a','t','s'],
    ['h','a','p'],
    ['t','i','s'],
    ['w','h','s']]
print(recoverSecret(test1) )       
#******************************************************************************
 
