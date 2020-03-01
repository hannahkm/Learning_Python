from nltk.corpus import words

og_word = 'sin'        
            
def check_word(og_word):
    print(og_word)
    new_word = og_word
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(1,26):
        for j in range(len(og_word)+1):
            new_word = og_word[:j]+str(a[i])+og_word[j:]
            if new_word in words.words() and len(new_word)==9:
                print(new_word)
            elif new_word in words.words() and len(new_word)<9:
                check_word(new_word)
                
    print(og_word, "failed - going back")
                
check_word('pig')