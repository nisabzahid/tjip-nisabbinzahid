class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        end = sum(weights)
        start = max(weights)

        while start <= end:
            mid = (start+end+1)//2
            day_needed = 1
            curr_w = 0
            
            for w in weights: #1,2,3,4,5,6,7,8,9,10
                if curr_w+ w > mid:
                    day_needed +=1 
                    curr_w = w
                else:
                    curr_w += w
            if day_needed > days:
                start = mid + 1  # need more capacity
            else:
                end = mid - 1  # try to lower capacity

        return start

