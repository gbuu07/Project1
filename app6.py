from Dictionary import *
import time

print("Dictionaries: short english french spanish")
name=input("Choose your *sorted* dictionary: ")
dict=Dictionary(name+"_sorted.txt") #instantiate and load a new dictionary


### Code breaker helper
nbletter=int(input("How many code letters to crack?: "))

lock=[]
# Ask for all options
for i in range(nbletter):
    lock.append(input("Enter all the options for letter " +str((i+1))+": ").split())
    
print("All lock combinations to consider:")    
for i in range(len(lock)):
    print(lock[i][:])

    
### get the dictionary of lock code, sort and display it
dlock_code=dict.crack_lock(lock)
dlock_code.insertion_sort()
print("\n%s word(s) found:"%dlock_code.get_size())
dlock_code.display()



