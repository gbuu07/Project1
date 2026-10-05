from Dictionary import *


print("Dictionaries: short english french spanish")
name=input("Choose your dictionary: ")
dict=Dictionary(name+".txt") #instantiate and load a new dictionary


letters=input("Enter series of letter: ").lower()
combs=Dictionary.get_word_combination(letters)

print("List of letter combinations: ",combs)
print("Number of non-zero letter combinations found: ",len(combs)-1)

## create list of anagram
mylist=[]
for c in combs:
    if len(c)!=0: mylist+=dict.anagram(c)


## create new dictionary
danagram=Dictionary()
for w in mylist: danagram.insert(w)
## compute score and sort
danagram.compute_score_scrabble()
danagram.score_sort()
## display info
print("\n%s anagram(s) found"%danagram.get_size()," with scrabble score")
danagram.display(score=True)

