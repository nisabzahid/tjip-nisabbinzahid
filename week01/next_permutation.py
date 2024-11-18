class Solution:
    
    def reverse(self, nums, beg, end):
        while beg < end:
            nums[beg] , nums[end] = nums[end] , nums[beg]
            beg +=1
            end -=1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i > -1 and nums[i]>= nums[i+1]:
            i -=1

        self.reverse(nums, i+1 , len(nums)-1) 

        if i == -1:
            return
        
        next_num = i +1
        while next_num < len(nums) and nums[next_num] <= nums[i] :
            next_num +=1

        nums[next_num], nums[i] = nums[i] , nums[next_num]        