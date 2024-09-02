class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ls=list(set(nums))
        count=[0]*len(ls)
        maj=len(nums)//2
        for i in range(len(ls)):
            c=0
            for j in range(len(nums)):
                if ls[i]==nums[j]:
                    c+=1
            count[i]=c
        for i in range(len(count)):
            if count[i]>maj:
                break
        return ls[i]


                

