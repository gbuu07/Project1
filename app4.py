from Dictionary import *


print("Dictionaries: short english french spanish")
name=input("Choose your dictionary: ")
dict=Dictionary(name+".txt") #instantiate and load a new dictionary

word=input("Enter word to analyze: ")

mylist=dict.anagram(word)


print("\n%s anagram(s) found"%len(mylist))
for l in mylist:
    print(l)
