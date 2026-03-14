class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_={}
        if len(s)!=len(t):
            return False
        for char in s:
            if char in dict_:
                dict_[char]+=1
            else:
                dict_[char]=1
        for char in t:
            if char not in dict_:
                return False
            dict_[char]-=1
            if dict_[char]<0:
                return False
        return True
        
        