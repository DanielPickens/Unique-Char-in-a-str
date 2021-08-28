class Solution:
    def firstUniqChar(self, s: str) -> int:
        prevInv = set()
        
        for i, letter in enumerate(s):
            if letter not in prevInv:
                if letter not in s[i+1:]:
                    return i
                else:
                    prevInv.add(letter)
        return -1
		
		
	# tc: O(n) where n is the len of s
	#	sc: O(n) where n is the len of s
