class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
    
        hashMapS = {}
        hashMapT = {}

        # Populate hashmap of string s
        for char in s:
            if char not in hashMapS.keys():
                hashMapS[char]=0
            else:
                hashMapS[char]+=1


        # Populate hashmap of string t
        for char in t:
            if char not in hashMapT.keys():
                hashMapT[char]=0
            else:
                hashMapT[char]+=1

        # They have different number of unique characters
        if len(hashMapS.keys())!=len(hashMapT.keys()):
            return False

        for key,value in hashMapS.items():
            if key not in hashMapT.keys():
                return False
            else:
                if value != hashMapT[key]:
                  return False
        return True