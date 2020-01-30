import math #importing some math package ig?
import random #able to make random numbers now

#this is a comment!
#I can do (simple) math
print(1+2)
print(10-3)
print(2*6)
print(8/2)
print(2**5)
#note: looks like print automatically goes onto the next line

#more advanced math using math package
print(math.pi)
print(math.sqrt(85))

#calling random numbers
print(random.random()) #no restrictions
print(random.choice([1,5,7,10])) #choose a random number from this list

#creating Strings
S = 'string' #unlike Java, Strings use single quotes
print(S)
print(len(S))
print(S[0]) #python is zero indexed!
print(S[2])
print(S[-1]) #can also go backwards - helpful
print(S[len(S)-1]) #same as above, but the harder, Java way
print(S[1:3]) #can also get substrings
print(S[1:]) #everything except for 0th index
print(S[:4]) #everything until the 4th index (not including 4th)
print(S[0:4]) #same as above
print(S[:-1]) #everything but the last index

#concatenation! yes!!
print(S+'abc') #using single quotes for Strings feels weird
print(S*10) #woahhhhh it repeats it :o

#changing strings
#you can't replace letters individually, but
S = 'x' + S[1:] #this essentially replaces the first letter with 'x'
print(S)
#the list way
S = 'walking'
L = list(S) #turns S into a list
print(L)
L[0] = 't' #note: lists are also 0-indexed
S = ''.join(L) #rejoins lists into a String
print(S)
#the bytearray (?) way
B = bytearray(b'hello')
B.extend(b' world')
print(B)
print(B.decode())

#more complex String functions
S = 'extraordinary'
print(S.find('xt')) #first
S = S.replace('xt', 'ABC')
print(S)
print(S.replace('a', 'XYZ')) #doesn't change the actual value of S
print(S)
S= S.replace('a', 'XYZ') #replaces in both a's! (but not the A)
print(S)
line = 'h,a,n,n,a,h'
L = line.split(',')
print(L)
print(S.upper())
S = 'hello       '
S = S.rstrip()
print(S)
S = S.__add__(', world') #same thing as +
print(S)

#testing using format
S = '%s, eggs, and %s' % ('spam', 'SPAM!')
print(S)
S = '%s, english, %s, and %s' % ('math', 'science', 'history')
print(S)
S = '{0}, eggs, and {1}'.format('spam', 'SPAM!')
print(S)
S = '{0}, english, {1}, and {2}'.format('math', 'science', 'history')
print(S)
S = '{1}, english, {2}, and {0}'.format('math', 'science', 'history')
print(S)
S = '{}, eggs, and {}'.format('spam', 'SPAM!')
print(S)
S = '{}, english, {}, and {}'.format('math', 'science', 'history')
print(S)

#escape characters:
#\n = new line
#\t = tab
#note that escape characters have a length??
S = 'A\nBC'
print(S + ' ' + str(len(S)))
#since A includes \n, the length is 4

#multiline Strings; use triple quotes
multiS = '''hello
ahhhhh
hecoiehgawgea hello
world'''
print(multiS)

#pattern matching?
#i'm assuming it's like regex in acsl :)
import re
match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
print(match.group(1))
    #finds group that starts with hello,
    #zero or more tabs
    #zero or more characters
    #ends with world
match = re.match('Hello[ \t]*(.*)world', 'Hello Python, hello world')
print(match.groups())
match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
print(match.groups())
match = re.match('[/](.*)[/](.*)', '/usr/home:lumberjack')
print(match.groups())
match = re.match('[/](.*)[:](.*)', '/usr/home:lumberjack')
print(match.groups())
#can also use split for similar result
print(re.split('[/:]', '/usr/home/lumberjack'))

#LISTS!!!!!
L = ['hello', 162, 1.70] #can have different types
print("length: " + str(len(L)))
print(L[0])
print(L[:-1]) #basically similar to strings
L = L + [3,6,1]
print(L)
L += [1,2,3]
print(L)
print(L*2) #repeats entire list twice
#^^ above functions must be set equal to L in order for it to change

#list functions
L = [1, "hi"]
L.append("world") #adds "world" to the end
print(L)
L.pop(2) #removes the 2nd index
print(L)
L = ['c', 'b', 'a', 'h', 'z', 'e']
L.sort() #puts them in alphabetical order
print(L)
L.reverse()
print(L)
#L = ['1', 'a', 1, 'abc', '+']
#L.sort() --> doesn't work btwn types
#print(L)

#can also nest lists
M = [[1,2,3],[4,5,6],[7,8,9]]
print(M)
print(M[1]) #the 2nd row (0th index again!)
print(M[1][2]) #second row and third column - just like in Java

#"comprehensions"??
print([row[1] for row in M]) #gets the 2nd column - kinda annoying
print([M[i][i] for i in [0,1,2]]) #gets a diagonal
print([row[1] + 1 for row in M]) #adds one to items in column 2
print([row[1] for row in M if row[1]%2==0]) #removes odd elements from second column
print([c*2 for c in 'hannah']) #doubles each character

print(list(range(4))) #prints range from 0 to 3 (length 4)
print(list(range(10)))
print(list(range(-6, 8, 2))) #range from -6 to 6, increment by 2
    #note that the second part of range isn't inclusive

print([[x**2, x**3] for x in range(4)])
    #creates list consisting of lists of 0-3 ^2 and ^3
print([[x, x/2, x*2] for x in range(-6, 7, 2) if x>0])

#M = [[1,2,3],[4,5,6],[7,8,9]]
G = (sum(row) for row in M) #using () creates generators?
print(next(G))
print(next(G))
print(next(G))
G = [sum(row) for row in M]
print(G)





