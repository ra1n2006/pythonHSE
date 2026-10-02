class Solution(object):
    def hIndex(self, citations):
        m = [0] * (max(citations) + 1)
        for i in citations:
            m[i] += 1

        if len(m) == 1: return 0
        for i in range(len(m) - 1, 0, -1):
            if i != len(m) - 1:
                m[i] += m[i + 1]
            if m[i] >= i:
                return i
