#INTRO TO PYTHON
pi = 3.14159
radius = 2.2
# area of circle equation <- this is a comment
area = pi*(radius**2)
print(area)

# change values of radius <- another comment
radius = radius + 1
print(area)     # area doesn't change
area = pi*(radius**2)
print(area)

# to comment MANY lines at a time, highlight all of them then CTRL+1 (CMD+1)
# do CTRL+1 (CMD+1) again to uncomment them

area = pi*(radius**2)
print(area)
radius = radius + 1
area = pi*(radius**2)
print(area)

# use autocomplete to write a line that prints the value of that long variable

#BRANCHING AND ITERATION

hi = "hello there"
name = "ana"
greet = hi + name  
print(greet)
greeting = hi + " " + name
print(greeting)
silly = hi + (" " + name)*3
print(silly)

x = 1
print(x)
x_str = str(x)
#different ways to concetenate
#plus just puts strings together
#commas automatically add spaces
print("my fav number is", x, ".", "x=", x)
print("my fav number is", x_str + "." + "x=" + x_str)
print("my fav number is" + x_str + "." + "x=" + x_str)

#getting input from the user
#text = input("Type anything... ") #read in as a string :/
#print(5*text)
#num = int(input("Type a number... "))
#print(5*num)

#conditionals and branching
#x = float(input("Enter a number for x: "))
#y = float(input("Enter a number for y: "))

#if statements!
#if x == y:
#    print("x and y are equal")
#    if y != 0:
#        print("therefore, x / y is", x/y)
#elif x < y:
#    print("x is smaller")
#elif x > y:
#    print("y is smaller")


#num = int(input("Enter a number: "))
#if num % 2 == 0: #modulus = remainder
#    print("number is even")
#else:
#    print("number is odd")


####################
## EXAMPLE: while loops 
## Try expanding this code to show a sad face if you go right
## twice and flip the table any more times than that. 
## Hint: use a counter
####################
#n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
#while n == "right" or n == "Right":
#    n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
#print("\nYou got out of the Lost Forest!")

n = 0
while n < 5:
    print(n)
    n = n+1


####################
## EXAMPLE: for loops
####################
for n in range(5):
    print(n)

mysum = 0
for i in range(10): #default value for start is zero
    mysum += i
print(mysum)

mysum = 0
for i in range(7, 10):
    mysum += i
print(mysum)

mysum = 0
for i in range(5, 11, 2): #increment by 2 each time
    mysum += i
    if mysum == 5:
        break
        mysum += 1
print(mysum)



####################
## EXAMPLE: perfect squares
####################
#ans = 0
#neg_flag = False
#x = int(input("Enter an integer: "))
#if x < 0:
#    neg_flag = True
#while ans**2 < x:
#    ans = ans + 1
#if ans**2 == x:
#    print("Square root of", x, "is", ans)
#else:
#    print(x, "is not a perfect square")
#    if neg_flag:
#        print("Just checking... did you mean", -x, "?")

####################
## EXAMPLE: for loops over strings
####################
s = "demo loops"
for index in range(len(s)):
    if s[index] == 'o' or s[index] == 'u':
        print("There is an o or u")

for char in s:
    if char == 'o' or char == 'u':
        print("There is an o or u")


####################
## EXAMPLE: while loops and strings
####################
#an_letters = "aefhilmnorsxAEFHILMNORSX"
#word = input("I will cheer for you! Enter a word: ")
#times = int(input("Enthusiasm level (1-10): "))
#
#i = 0
#while i < len(word):
#    char = word[i]
#    if char in an_letters:
#        print("Give me an " + char + "! " + char)
#    else:
#        print("Give me a  " + char + "! " + char)
#    i += 1
#print("What does that spell?")
#for i in range(times):
#    print(word, "!!!")


    
####################
## EXAMPLE: perfect cube 
####################
cube = 27
#cube = 8120601
for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess)
        # loops keeps going even after found the cube root
    

####################
## EXAMPLE: guess and check cube root 
####################
cube = 27
#cube = 8120601
for guess in range(abs(cube)+1):
    # passed all potential cube roots
    if guess**3 >= abs(cube):
        # no need to keep searching
        break #only breaks out of the current if statement
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))


####################
## EXAMPLE: approximate cube root 
####################
##cube = 27
#cube = 8120601
##cube = 10000
#epsilon = 0.1
#guess = 0.0
#increment = 0.01
#num_guesses = 0
### look for close enough answer and make sure
### didn't accidentally skip the close enough bound
#while abs(guess**3 - cube) >= epsilon and guess <= cube:
#    guess += increment
#    num_guesses += 1
#print('num_guesses =', num_guesses)
#if abs(guess**3 - cube) >= epsilon:
#    print('Failed on cube root of', cube, "with these parameters.")
#else:
#    print(guess, 'is close to the cube root of', cube)


####################
## EXAMPLE: bisection cube root (only positive cubes!)
####################
cube = 27
#cube = 8120601
# won't work with x < 1 because initial upper bound is less than ans
#cube = 0.25
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        # look only in upper half search space
        low = guess
    else:
        # look only in lower half search space
        high = guess
    # next guess is halfway in search space
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)

#########################
## EXAMPLE: combinations of print and return
#########################
def with_return( i ):
    return i+1 #will return the value of i+1

def without_return( i ):
    i += 1
    #nothing happens - will return "None"
    
with_return(3)
print(with_return(3))
without_return(3)
print(without_return(3)) #of course you always have to use print


##########################
### EXAMPLE: applying functions to repeat same task many times
##########################
def bisection_cuberoot_approx(x, epsilon):
    """
    Input: x, an integer
    Uses bisection to approximate the cube root of x to within epsilon
    Returns: a float approximating the cube root of x
    """
    low = 0.0
    high = x
    guess = (high + low)/2.0
    while abs(guess**3 - x) >= epsilon:
        if guess**3 < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
    return guess

x = 1
while x <= 10000:
    approx = bisection_cuberoot_approx(x, 0.01)
    print(approx, "is close to cube root of", x)
    x *= 10
#
#
##########################
### EXAMPLE: functions as arguments
##########################
def func_a():
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()

print(func_a())
print(5+func_b(2))
print(func_c(func_a)) #can call a function through parameter???
#
#
##########################
### EXAMPLE: returning function objects
##########################
def f():
    def x(a, b):
        return a+b
    return x
    
# the first part, f(), returns a function object
# then apply that function with parameters 3 and 4
val = f()(3,4)
print(val)


##########################
### EXAMPLE: shows accessing variables outside scope
##########################
def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print("here: " + str(x))

def g(y):
    print(x)
    print(x+1)
x = 5
g(x)
print(x)

def h(y):
    pass #pass is used as a placeholder: does nothing, but prevents errors
    #x += 1 #leads to an error without line `global x` inside h
x = 5
h(x)
print(x)

##########################
### EXAMPLE: harder scope example from slides
##########################
def g(x):
    def h():
        x = 'abc' #does nothing - can also just have pass instead
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)
#
#
##########################
### EXAMPLE: complicated scope, test yourself!
##########################
def f(x):
   x = x + 1
   print('in f(x): x =', x)
   return x

x = 3
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)

def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    print('in g(x) pt 2: x = ', x)
    return x

x = 3
z = g(x)
print('in main program scope: x = ', x)
print('in main program scope: z = ', z)

#########################
## EXAMPLE: returning a tuple
## About tuples: immutable
#########################
def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)
    
(quot, rem) = quotient_and_remainder(5,3)
print(quot)
print(rem) #hmmm this is really cool :o


##########################
### EXAMPLE: iterating over tuples
##########################
def get_data(aTuple):
    """
    aTuple, tuple of tuples (int, string)
    Extracts all integers from aTuple and sets 
    them as elements in a new tuple. 
    Extracts all unique strings from from aTuple 
    and sets them as elements in a new tuple.
    Returns a tuple of the minimum integer, the
    maximum integer, and the number of unique strings
    """
    nums = ()    # empty tuple
    words = ()
    for t in aTuple: #t is a tuple (int, string)
        # concatenating with a singleton tuple
        nums = nums + (t[0],)   #adding the ints
        # only add words haven't added before
        if t[1] not in words:   
            words = words + (t[1],) #adding the strings
            
    #final value of nums: (1, 2, 1, 7)
    #final value of words: ('a', 'b')
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

test = ((1,"a"),(2, "b"),
        (1,"a"),(7,"b"))
(a, b, c) = get_data(test)
print(test)
print("a:",a,"b:",b,"c:",c)
#
## apply to any data you want!
#tswift = ((2014,"Katy"),
#          (2014, "Harry"),
#          (2012,"Jake"), 
#          (2010,"Taylor"), 
#          (2008,"Joe"))    
#(min_year, max_year, num_people) = get_data(tswift)
#print("From", min_year, "to", max_year, \
#        "Taylor Swift wrote songs about", num_people, "people!")
#
#########################
## EXAMPLE: sum of elements in a list
## About lists: mutable
#########################
def sum_elem_method1(L):
  total = 0 
  for i in range(len(L)): 
      total += L[i] 
  return total
  
def sum_elem_method2(L):
    total = 0 
    for i in L: 
        total += i 
    return total
  
print(sum_elem_method1([1,2,3,4]))
print(sum_elem_method2([1,2,3,4]))
#
#
##########################
### EXAMPLE: various list operations
### put print(L) at different locations to see how it gets mutated
##########################
L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2
L1.extend([0,6])
#print(L1) #gives [2,1,3,0,6]
#print(L3) #gives [2,1,3,4,5,6]

L = [2,1,3,6,3,7,0]
L.remove(2)
L.remove(3)
del(L[1])
print(L.pop()) #gives 0 (last element of the list?)
index = L.index(3)
print('list:', L)
print('index of 3:', index)

s = "I<3 cs"
print('listed', list(s))
print('using split with <:', s.split('<'))
L = ['a', 'b', 'c']
print('join without whitespace', ''.join(L))
print('join with underscore', '_'.join(L))

L=[9,6,0,3]
print(sorted(L))
L.sort() #two ways to sort?
L.reverse()
#
#
##########################
### EXAMPLE: aliasing
##########################
a = 1
b = a
print(a)
print(b)
b += 1
print(a) #changing b doesn't change a

warm = ['red', 'yellow', 'orange']
hot = warm
hot.append('pink')
print(hot)
print(warm) #appending to hot changes both! (like linked lists iirc?)

##########################
### EXAMPLE: cloning
##########################
cool = ['blue', 'green', 'grey']
chill = cool[:]
chill.append('black')
print(chill)
print(cool) #if you clone, it's like making a copy - same but separate

##########################
### EXAMPLE: sorting with/without mutation
##########################
warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort()
print('warm:', warm)
print('sorted warm:', sortedwarm)

cool = ['grey', 'green', 'blue']
sortedcool = sorted(cool)
print('cool:', cool)
print('sorted cool:', sortedcool)

##########################
### EXAMPLE: lists of lists of lists...
##########################
warm = ['yellow', 'orange']
hot = ['red']
print('warm:', warm)
brightcolors = [warm]
print('bright colors:', warm)
brightcolors.append(hot)
print('bright colors with appended hot', brightcolors)
hot.append('pink')
print('hot with appended pink', hot)
print('new bright colors', brightcolors)


################################
### EXAMPLE: mutating a list while iterating over it
################################
def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
    #logic error: by removing element the for loop skips over one
      
def remove_dups_new(L1, L2):
    L1_copy = L1[:] #remember : is to clone
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2) #removes elements from L1 if also in L2
print(L1, L2)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups_new(L1, L2)
print(L1, L2)

################################
### EXERCISE: Test yourself by predicting what the output is and 
###           what gets mutated then check with the Python Tutor
################################
#cool = ['blue', 'green']
#warm = ['red', 'yellow', 'orange']
#print(cool)
#print(warm)
#
#colors1 = [cool]
#print(colors1)
#colors1.append(warm)
#print('colors1 = ', colors1)
#
#colors2 = [['blue', 'green'],
#          ['red', 'yellow', 'orange']]
#print('colors2 =', colors2)
#
#warm.remove('red') 
#print('colors1 = ', colors1)
#print('colors2 =', colors2)
#
#for e in colors1:
#    print('e =', e)
#
#for e in colors1:
#    if type(e) == list:
#        for e1 in e:
#            print(e1)
#    else:
#        print(e)
#
#flat = cool + warm
#print('flat =', flat)
#
#print(flat.sort())
#print('flat =', flat)
#
#new_flat = sorted(flat, reverse = True)
#print('flat =', flat)
#print('new_flat =', new_flat)
#
#cool[1] = 'black'
#print(cool)
#print(colors1)


#####################################
# EXAMPLE:  Towers of Hanoi
#####################################

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))

#####################################
# EXAMPLE:  fibonacci
#####################################

def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
print(fib(5)) #fib number 1 = 1, number 2 = 2, etc
#####################################
# EXAMPLE:  testing for palindromes
#####################################
        
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
            #returns true if first and last are equal AND word
                #minus the first and last char is a palindrome

    return isPal(toChars(s))

print(isPalindrome('eve'))
print(isPalindrome('Able was I, ere I saw Elba'))
print(isPalindrome('Is this a palindrome'))

#####################################
# EXAMPLE: using dictionaries
#          counting frequencies of words in song lyrics
# About dictionaries: mutable, allows to search over values instead of index,
    #have more than one value at each index - better than having multiple lists
#####################################

#initializing:
new_dict = {'Bob':12, 'John':24, 'Hannah':18}
print(new_dict['Hannah']) #gets the value saved at index Hannah
print("Is Jimmy in new_dict?:", 'Jimmy' in new_dict) #returns true if Jimmy is a key
print("dict before delete", new_dict)
del(new_dict['Bob'])
print("dict after delete", new_dict)
new_dict["Tim"] = 129 #creates new key with label "Tim" and value 129
print("dict with Tim", new_dict)
print("all keys:", new_dict.keys()) #returns all keys
print("values:", new_dict.values()) #returns all values

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1 #creates new value at "index" 'word'
    return myDict
    
    
she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]

beatles = lyrics_to_frequencies(she_loves_you)
#print('beatles:', beatles)
#print('values:', beatles.values())


def most_common_words(freqs):   
#    print('values', freqs.values())
    best = max(freqs.values())
#    print('best', best)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
            
#    print('words', words)
    return (words, best)
    
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
#        print('temp', temp)
#        print(temp[1])
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])  #remove word from dict and also beatles variable
        else:
            done = True
    return result
    
print(words_often(beatles, 5))

#####################################
# EXAMPLE: comparing fibonacci using memoization
# Memoization according to Wikipedia: Memoization is a way to lower a 
    #function's time cost in exchange for space cost; that is, memoized 
    #functions become optimized for speed in exchange for a higher use 
    #of computer memory space.
#####################################


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans
        
d = {1:1, 2:2} #dictionary 

argToUse = 34
print("")
print('using fib')
print(fib(argToUse))
print("")
print('using fib_efficient')
print(fib_efficient(argToUse, d))

########################################
### EXAMPLE: Buggy code to reverse a list
### Try to debug it! (fixes needed are explained below)
########################################
##def rev_list_buggy(L):
##    """
##    input: L, a list
##    Modifies L such that its elements are in reverse order
##    returns: nothing
##    """
##    for i in range(len(L)):
##        j = len(L) - i
##        L[i] = temp
##        L[i] = L[j]
##        L[j] = L[i]
#
## FIXES: --------------------------
## temp unknown
## list index out of range -> sub 1 to j
## get same list back -> iterate only over half
## --------------------------
def rev_list(L):
    """
    input: L, a list
    Modifies L such that its elements are in reverse order
    returns: nothing
    """
    for i in range(len(L)//2):
        j = len(L) - i - 1
        temp = L[i]
        L[i] = L[j]
        L[j] = temp
        
L = [1,2,3,4]
rev_list(L)
print(L)
#
#
########################################
### EXAMPLE: Buggy code to get a list of primes
### Try to debug it! (fixes needed are explained below)
########################################
#def primes_list_buggy(n):
#    """
#    input: n an integer > 1
#    returns: list of all the primes up to and including n
#    """
#    primes = []
#    # initialize primes list
#    if i == 2:
#        primes.append(2)
#    # go through each elem of primes list
#    for i in range(len(primes)):
#        # go through each of 2...n
#        for j in range(len(n)):
#            # check if not divisible by elem of list
#            if i%j != 0:
#                primes.append(i)


## FIXES: --------------------------
## = invalid syntax, variable i unknown, variable primes unknown
## can't apply 'len' to an int
## division by zero -> iterate through elems not indices
##                  -> iterate from 2 not 0
## forgot to return 
## primes is empty list for n > 2
## n = 3 goes through loop once -> range to n+1 not n
## infinite loop -> append j not i
##               -> list is getting modified as iterating over it!
##               -> switch loops around
## n = 4 adds 4 -> need way to stop going once found a divisible num
##              -> use a flag
## --------------------------
def primes_list(n):
    """
    input: n an integer > 1
    returns: list of all the primes up to and including n
    """
    # initialize primes list
    primes = [2]
    # go through each of 3...n
    for j in range(3,n+1):
        is_div = False
        # go through each elem of primes list
        for p in primes:
            if j%p == 0:
                is_div = True
        if not is_div:
            primes.append(j)
    return primes

print(primes_list(2) )               
print(primes_list(15)  )              


######################################
# EXAMPLE: Exceptions and input
######################################
#a = int(input("Tell me one number: "))
#b = int(input("Tell me another number: "))
#print("a/b = ", a/b)
#print("a+b = ", a+b)

try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
except:
    print("Bug in user input.")


try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
    print("a+b = ", a+b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Something went very wrong.")



######################################
# EXAMPLE: Raising your own exceptions
######################################
def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
        else:
            print(index, "success")
        finally:
            print(index, "executed no matter what!")
    return ratios
    
#print(get_ratios([1, 4], [2, 4]))


#######################################
## EXAMPLE: Exceptions and lists
#######################################
def get_stats(class_list):
	new_stats = []
	for person in class_list:
		new_stats.append([person[0], person[1], avg(person[1])])
	return new_stats 

# avg function: version without an exception
#def avg(grades):
#    return (sum(grades))/len(grades)
    
# avg function: version with an exception
def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('warning: no grades data')
        return 0.0


# avg function: version with assert
#def avg(grades):
#    assert len(grades) != 0, 'warning: no grades data'
#    return sum(grades)/len(grades)

    
test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], 
              [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
              [['captain', 'america'], [80.0, 70.0, 96.0]],
              [['deadpool'], []]]

print(get_stats(test_grades))
#using 1st avg function (using print) allows program to run normally
#using 2nd avg function (using assert) prints normal error message plus
    #additional, custom message
    
#################
## EXAMPLE: simple Coordinate class
#################
class Coordinate(object):
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def distance(self, other):
        """ Returns the euclidean distance between two points """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5


c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.x, origin.x)
print(c.distance(origin))
print(Coordinate.distance(c, origin))
print(origin.distance(c))
print(c)


#################
## EXAMPLE: simple class to represent fractions
## Try adding more built-in operations like multiply, divide
### Try adding a reduce method to reduce the fraction (use gcd)
#################
class Fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom
    def __str__(self):
        """ Retunrs a string representation of self """
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom
    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b # c is a Fraction object
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))
##c = Fraction(3.14, 2.7) # assertion error
##print a*b # error, did not define how to multiply two Fraction objects


##############
## EXAMPLE: a set of integers as class
##############
class intSet(object):
    """
    An intSet is a set of integers
    The value is represented by a list of ints, self.vals
    Each int in the set occurs in self.vals exactly once
    """
    def __init__(self):
        """ Create an empty set of integers """
        self.vals = []

    def insert(self, e):
        """ Assumes e is an integer and inserts e into self """
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """ Assumes e is an integer
        Returns True if e is in self, and False otherwise """
        return e in self.vals

    def remove(self, e):
        """ Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self """
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """ Returns a string representation of self """
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'


s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
print(s)
s.member(3)
s.member(5)
s.insert(6)
print(s)
#s.remove(3)  # leads to an error
print(s)
s.remove(3)







   
