# Your names: 
# Aymaan Changai Mangalote
# Gia Buu Luong
#
#

# no other modules allowed
import random,time,sys




class Dictionary:



    #### To complete
    def __init__(self,filename=None):
        random.seed(8)
        self.__index = -1
        self.__words = list()
        self.__scores = list()
        if filename is None:
            self.__name = "N/A"
        else:
            self.__name = filename.removesuffix(".txt")
            try:
                with open(filename) as f:
                    self.__words = [line.strip() for line in f]
                print("Load %s" % filename)            
            except FileNotFoundError:
                print("File %s does not exist!" %filename)
                sys.exit(0)

        
    def get_name(self):
        return self.__name
    
    def get_size(self):
        return len(self.__words)
    
    def get_random_list(self,n):
        random_list = list()
        for i in range(n):
            random_list.append(self.__words[random.randint(0,self.get_size()-1)])
        return random_list

    def get_index(self):
        return self.__index

    def insert(self,word):
        self.__words.append(word)

    def display(self, score=False):
        for i in range(self.get_size()):
            if score:
                print(self.__words[i], self.__scores[i])
            else:
                print(self.__words[i])

    def compute_score_scrabble(self):
        points = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1,
                  "f": 4, "g": 2, "h": 4, "i": 1, "j": 8,
                  "k": 5, "l": 1, "m": 3, "n": 1, "o": 1,
                  "p": 3, "q": 10, "r": 1, "s": 1, "t": 1,
                  "u": 1, "v": 4, "w": 4, "x": 8, "y": 4,
                  "z": 10}
        self.__scores = list()
        for word in self.__words:
            score = 0
            for letter in word.lower():
                score += points.get(letter, 0)
            self.__scores.append(score)

    def score_sort(self):
        for i in range(1, self.get_size()):
            currentword = self.__words[i]
            currentscore = self.__scores[i]
            j = i
            while j > 0 and self.__scores[j-1] > currentscore:
                self.__scores[j] = self.__scores[j-1]
                self.__words[j] = self.__words[j-1]
                j -= 1
            self.__scores[j] = currentscore
            self.__words[j] = currentword

    def shuffle(self):
        start = time.process_time()
        size = self.get_size() 
        for i in range(size-1,0,-1):
            j = random.randint(0,i)
            self.__words[i], self.__words[j] = self.__words[j], self.__words[i]
        end = time.process_time()
        return end-start

    def lsearch(self,word):
        size = self.get_size()
        for i in range(size):
            if self.__words[i] == word:
                self.__index=i
                return True
        self.__index = -1
        return False

    def bsearch(self,word):
        size = self.get_size()

        lo = 0
        hi = size-1
        while lo <= hi:
            mid = (lo+hi) // 2
            if self.__words[mid] == word:
                self.__index = mid
                return True
            elif self.__words[mid] > word:
                hi = mid-1
            else:
                lo = mid +1
        self.__index = lo
        return False

    def insertion_sort(self):
        start = time.process_time()
        size = self.get_size()
        for i in range(1,size):
            currentvalue = self.__words[i]
            j = i

            while j > 0 and self.__words[j-1] > currentvalue:
                self.__words[j] = self.__words[j-1]
                j-=1
            self.__words[j]=currentvalue
        end = time.process_time()
        return end-start

    def enhanced_insertion_sort(self):
        start = time.process_time()
        size = self.get_size()
        for i in range(1,size):
            currentvalue = self.__words[i]
            lo = 0 
            hi = i-1
            while lo <= hi:
                mid = (lo+hi)//2
                if self.__words[mid] > currentvalue:
                    hi = mid-1
                else:
                    lo = mid+1
            j = i 
            while j> lo:
                self.__words[j]=self.__words[j-1]
                j-=1
            self.__words[lo] = currentvalue
        end = time.process_time()
        return end-start

    def save(self,filename):
        size = self.get_size()
        with open(filename, 'w') as f:
            for i in range(size):
                f.write(self.__words[i]+"\n")




        

    
    def selection_sort(self):    #provided to you
        """Perfom selection sort, must return the time it takes to sort the list of words
        Remark: Routine works 'in-place'"""
        t1 = time.process_time() #capture time
        n=self.get_size()
        for out in range(n-1):        #outer loop
            #find minimum between out+1 and n-1
            imin=out
            for i in range(out+1,n):  #inner loop
                if self.__words[i]<self.__words[imin]: 
                    imin=i #update  minimum index
            #swap (3 step here)
            temp=self.__words[imin]
            self.__words[imin]=self.__words[out]
            self.__words[out]=temp
        t2 = time.process_time() #capture time
        return t2-t1
        


    
    @staticmethod  # provided to you
    def get_word_combination(word, combs=['']):
        """ return a list that contains all the letter combinations (all length) of the input 'word' """
        if len(word) == 0:
            return combs
        head, tail = word[0], word[1:]
        combs = combs + list(map(lambda x: x+head, combs))
        return Dictionary.get_word_combination(tail, combs)

    

    @staticmethod
    def sort_word(word):
        """ must return a string with letters included in 'word' that are now sorted"""
        letters = list(word)
        n = len(letters)
        for out in range(n - 1):
            imin = out
            for i in range(out + 1, n):
                if letters[i] < letters[imin]:
                    imin = i
            letters[out], letters[imin] = letters[imin], letters[out]
        return "".join(letters)

    def anagram(self, word):
        result = []
        key = Dictionary.sort_word(word)
        for w in self.__words:
            if len(w) == len(word) and Dictionary.sort_word(w) == key:
                result.append(w)
        return result

    def crack_lock(self, lock):
        c = 1
        for options in lock:
            c *= len(options)

        new_dict = Dictionary()
        for _ in range(6 * c):
            word = ""
            for options in lock:
                idx = random.randint(0, len(options) - 1)
                word += options[idx]
            if self.bsearch(word):
                if not new_dict.lsearch(word):
                    new_dict.insert(word)
        return new_dict



    

    
########################################################################
########################################################################


def main():

    ### step-1 test constructor
    name=input("Enter dictionary name (from file 'name'.txt): ")    
    dict1=Dictionary(name+".txt")
    
    

    ### step-2 test get_name, get_size, get_random_list        
    print('Name main dictionary:',dict1.get_name())   
    print('Size main dictionary:',dict1.get_size()) 
    print("Five random words:",end=" ")
    rlist=dict1.get_random_list(5) # 5 means the number of random words we want
    for w in rlist: print(w,end=" ")
    print("\n")

    ### step-3 test constructor again
    dict2=Dictionary()
    print('Name extracted dictionary:',dict2.get_name())
    
    ### step-4 test insert and display
    for w in rlist: dict2.insert(w)
    print('Display extracted dictionary:')
    dict2.display()

    ### step-5 test shuffle 
    t=dict2.shuffle()
    print('\nExtracted dictionary shuffled in %ss:'%t)
    print('Display extracted dictionary:')
    dict2.display()

    ### step-6 test linear search
    word="morning"
    print("\nLinear search for the word '%s' in extracted dictionary"%word)
    status=dict2.lsearch(word)
    print("Is '%s' found: %s at index %s"%(word,status,dict2.get_index()))

    ### step-7 sort extracted using selection sort (provided to you)
    t=dict2.selection_sort()
    print('\nExtracted dictionary sorted in %ss:'%t)
    print('Display extracted dictionary:')
    dict2.display()

    ### step-8 test binary search (find it)
    words=["morning","night"]
    for word in words:
        print("\nBinary search for the word '%s' in extracted dictionary"%word)
        status=dict2.bsearch(word) # binary search
        if (status):  # found it!!
            print("Is '%s' found: %s at index %s"%(word,status,dict2.get_index()))
        else:          # Nope did not find it
            print("'%s' is not found so it must be inserted at index %s"%(word,dict2.get_index()))



            
## call the main function if this file is directly executed
if __name__=="__main__":
    main()
