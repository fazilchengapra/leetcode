class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != (m*n):
            return []

        res = []
        t = []
        for i in original:
            if len(t) < n:
                t.append(i)
            else:
                res.append(t)
                t = []
                t.append(i)
        res.append(t)

        return res