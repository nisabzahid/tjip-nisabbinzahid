class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maxh = 0
        citations = sorted(citations)
        n = len(citations)
        for i in range(n):
            if  n-i <= citations[i] :
                print(citations[i], len(citations)-i)
                maxh =  n-i
                break
        return maxh