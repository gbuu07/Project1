from Dictionary import *


print("Dictionaries: short english french spanish")
name=input("Choose your dictionary: ")
dict=Dictionary(name+".txt") #instantiate and load a new dictionary
print("**Dictionary %s contains %s words\n"%(dict.get_name(),dict.get_size()))


print("1-insertion\n2-enhanced insertion sort")
opt=int(input("Choose your sorting algorithm: "))

t=dict.shuffle()
print("**Dictionary %s shuffled in %s seconds\n"%(dict.get_name(),t))

if opt==1:
    t1=dict.insertion_sort()
    print("**Dictionary %s sorted with -insertion- in %s seconds\n"%(dict.get_name(),t1))
elif opt==2:
    t2=dict.enhanced_insertion_sort()
    print("**Dictionary %s sorted with -enhanced insertion- in %s second\n"%(dict.get_name(),t2))


#save sorted dictionary
dict.save(name+"_sorted.txt")
######################################################################
