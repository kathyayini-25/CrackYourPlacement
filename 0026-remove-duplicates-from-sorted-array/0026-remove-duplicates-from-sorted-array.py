class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap=set()
        i=0
        while i<len(nums):
            if nums[i] in hashmap:
                nums.pop(i)
            else:
                hashmap.add(nums[i])
                i+=1
        return len(nums)
        