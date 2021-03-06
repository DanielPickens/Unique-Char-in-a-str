class Solution:
    def firstUniqChar(self, s: str) -> int:
        prevInv = set()  #using a set, initializing and creating the set for the function to test letter entries in a string of s
        
        for i, letter in enumerate(s): ##saying that for i, enumerate letter in s, since the iterable is a sequence,  if the letter in s returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating will be over iterable for str of s or not
            if letter not in prevInv: ## a sequence to test if letter is not in either s or prevInv
                if letter not in s[i+1:]: 
                    return i
                else:
                    prevInv.add(letter) ## logic that performs a mathematical operation to add the letters found to the object
        return -1
		
		
	#  tc: O(n) where n is the len of s
	#  sc: O(n) where n is the len of s
