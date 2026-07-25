class Solution(object):
    def majorityElement(self, nums):
        ans = [0, 0]
        h = {}

        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        
        for k, v in h.items():
            if v > ans[1]:
                ans[0] = k
                ans[1] = v
        
        return ans[0]
        