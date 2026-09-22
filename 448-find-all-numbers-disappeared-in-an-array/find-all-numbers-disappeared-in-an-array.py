class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = {i for i in nums}
        not_in = []

        for i in range(1, len(nums)+1):
            if i not in s:
                not_in.append(i)
        return not_in