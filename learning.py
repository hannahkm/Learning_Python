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













