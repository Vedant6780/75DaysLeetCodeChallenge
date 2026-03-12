class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_={}
        for i in range(len(nums)):
         a=nums[i]
         more=target-a
         if more in dict_:
            return dict_[more],i
         dict_[a]=i


        