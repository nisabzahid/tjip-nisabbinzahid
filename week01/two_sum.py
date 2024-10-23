class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i in range(len(nums)):
            if target - nums[i] in num_to_index:
                return [num_to_index[target - nums[i]], i]
            num_to_index[nums[i]] = i
        return []