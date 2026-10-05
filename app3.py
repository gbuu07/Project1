from Dictionary import *


print("Dictionaries: english french spanish")
name=input("Choose your *sorted* dictionary: ")
dict=Dictionary(name+"_sorted.txt") #instantiate and load a new dictionary

filename=input("Enter file name to spell check: ")
dict.spell_check(filename+".txt")
