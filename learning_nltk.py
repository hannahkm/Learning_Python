#installing nltk (because I was having problems)
#in terminal: python -m nltk.downloader all (on MacOS)

#import nltk
#nltk.download()

#using tutorial from: https://www.nltk.org/book/ch01.html
#download book

#from nltk.book import *
#access each book in the collection using text1, text2, ... text9

#search for every occurance of a word in a given text:
text1.concordance("monstrous")
print("===============")
#search for what words are related to each word in the text
#occur in similar contexts
text1.similar("monstrous")
print("===============")
#similar function: common_contexts looks for related contexts between 2+ words
text2.common_contexts(["monstrous", "very"])
print("===============")

#plots!
#dispersion plot: kind of looks like the ctrl+f function
#places a line for every occurance of a word
#row: the entire text, column: the number of words from the beginning 
        #uncomment below to plot
#text4.dispersion_plot(["citizens", "democracy", "freedom"])

#generate random text??
#hmm it generates new text in a similar style to the text, but it's not 
#actually from the text :o
text3.generate()

#counting words
print("tokens in text3", len(text3)) #counts number of words + punctuation (tokens)
#obtain full vocab of the text
#set(text3) <-- not very compact
#print("sorted set of txt3", sorted(set(text3))) #alphabetized
print("number of unique tokens", len(set(text3)))
print("avg number of use per token = ", len(text3)/len(set(text3)))
print("actual number of use of word 'where' = ", text3.count("where"))
print("% of all words that 'where' is = ", 100*text3.count("where")/len(text3))

#some functions that will be used throughout
def lexical_diversity(text):
    return len(set(text))/len(text)
def percentage(count, total):
    return 100*count/total

#list of the first sentence of Moby Dick
print(sent1) #sent1 is the first sentence of text1 (Moby Dick)
#cool: can add lists together :)
print(sent4+sent1)
sent1.append("Some") #.append() changes the value of sent1
                    #every time I run this program "Some" will be added lol
print(sent1) #trying to print with .append() inside only returns None...
#the texts are similar to lists
#get the word at a certain index of a text
print("word at index 125 of text1:", text1[125])
#reverse: get the FIRST index of a certain word
print("first index of 'letter' in text1:", text1.index("letter"))
#can also get a range of indices
print(text5[1239:1258])

#playing with lists
list1 = ["first", "second", "third", "last"]
list1[1:3] = ["then"]
print(list1)








