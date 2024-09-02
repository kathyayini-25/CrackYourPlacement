class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx=0
        for i in range(len(accounts)):
            if sum(accounts[i])>maxx:
                maxx=sum(accounts[i])
        return maxx
            