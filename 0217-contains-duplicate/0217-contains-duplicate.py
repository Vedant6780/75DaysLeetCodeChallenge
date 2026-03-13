class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_={}
        for num in nums:
            if num in dict_:
                dict_[num]+=1
            else:
                dict_[num]=1
        for i in dict_:
            if dict_[i]>1:
                return True
        return False

        