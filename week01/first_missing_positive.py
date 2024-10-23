class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l=len(nums)

        def get_position(i):
            while 0 < nums[i] <= l and nums[i] != nums[nums[i]-1]:
                nums[nums[i] - 1], nums[i]  = nums[i] ,nums[nums[i]-1] 


        for i in range(l):
            get_position(i)
        
        for i in range(l):
             if nums[i] != i+1:
                return i+1    
        return l+1