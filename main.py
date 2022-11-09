import nltk
import random
import pickle
import time


wordDelay = 0
numWords = 30
autoUpdate = True

# Used when creating new pickle dataset
#with open("text.txt") as f:
#    TEXT = f.read().split()
#
#trigrams = nltk.trigrams(TEXT)
#
#trigrams = (((w0, w1), w2) for w0, w1, w2 in trigrams)
#
#cfd = nltk.ConditionalFreqDist(trigrams)


# used to import pickle dataset
with open('data.pickle', 'rb') as f:
    cfd = pickle.load(f)

# used to export pickle dataset
#with open('data.pickle', 'wb') as f:
#    pickle.dump(cfd, f)

def contains(query, lst):
    for item in lst:
        if [item[0].lower(), item[1].lower()] == [query[0].lower(), query[1].lower()]:
            return True

def search(dictionary, query):
    for i in dictionary:
        if [x.lower() for x in i] == [query[0].lower(), query[1].lower()]:
            return dictionary[i]


while True: #big loop
    fetchingKeyword = True
    while fetchingKeyword: #get input
        arg = input("Enter 1-2 keywords (or type '!' for random!):\n").lower().split()
        if arg[0] == "!":
            word = random.choice(list(cfd.keys()))
            fetchingKeyword = False
            
        if len(arg) == 1:
            for i in cfd.keys():
                if i[0].lower() in arg:
                    word = (arg[0], i[1])
                    fetchingKeyword = False
        else:
            for i in cfd.keys():
                if [x.lower() for x in i] == arg:
                    word = tuple(arg)
                    fetchingKeyword = False
        if fetchingKeyword:
            print("Keyword not found in dataset! Please try again.")
        
    # generate more!
    print(word[0], end = " ", flush = autoUpdate)
    for i in range(numWords):
        time.sleep(wordDelay)
        print(word[1], end = " ", flush = autoUpdate)
        if contains(word, cfd.keys()):
            word = (word[1], random.choice(list(search(cfd, word))))
        else:
            break
    print("")
