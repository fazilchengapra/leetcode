class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        res = []
        for i in range(len(nums)):
            d[i+1] = 0
        
        for i in nums:
            d[i] += 1

        for k,v in d.items():
            if v == 0:
                res.append(int(k))
        
        return res
        