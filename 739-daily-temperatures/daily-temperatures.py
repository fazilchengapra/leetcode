class Solution(object):
    def dailyTemperatures(self, tm):
        ans = [0 for i in range(len(tm))]
        stack = []

        for i in range(len(tm)):
            if len(stack) == 0:
                stack.append(i)
            else:
                if tm[stack[len(stack)-1]] > tm[i]:
                    stack.append(i)
                else:
                    while len(stack) > 0:
                        if tm[stack[len(stack)-1]] < tm[i]:
                            v = stack.pop()
                            ans[v] = i - v
                        else:
                            break
                    stack.append(i)
        return ans