class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap=set()
        for i in range(len(nums)):
            second=target-nums[i]
            if second in hashmap:
                return [i,nums.index(second)]
            hashmap.add(nums[i])
            
        