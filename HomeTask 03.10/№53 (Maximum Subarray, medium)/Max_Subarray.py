class Solution(object):
    def maxSubArray(self, nums):
        pref = [0] * len(nums)
        pref[0] = nums[0]

        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] + nums[i]

        l = -1
        mx = pref[0]
        mn = 0

        for i in range(len(pref)):
            if l == -1:
                mx = max(pref[i], mx)
            else:
                mx = max(pref[i] - pref[l], mx)

            if pref[i] < mn:
                mn = pref[i]
                l = i

        return mx
