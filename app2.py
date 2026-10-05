from Dictionary import *
import time

print("Dictionaries: short english french spanish")
name=input("Choose your *sorted* dictionary: ")
dict=Dictionary(name+"_sorted.txt") #instantiate and load a new dictionary
print("**Dictionary %s contains %s words\n"%(dict.get_name(),dict.get_size()))


m=int(input("How many random words would you like to search? "))

print("first few random words:")
random_words=dict.get_random_list(m)
for i in range(min(len(random_words),5)):
  print(random_words[i])


######### binary search
t1 = time.process_time() #capture time
total_steps=0 # total counter for steps
for word in random_words:
  is_found=dict.bsearch(word)        # search the word
  total_steps+=dict.get_steps()
t2 = time.process_time() #capture time
print("Search time is: %s, with %s average number of steps"%(t2-t1,total_steps//m))
