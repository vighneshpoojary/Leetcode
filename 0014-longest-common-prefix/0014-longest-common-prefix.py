class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        start = strs[0]
        end = strs[-1]
        i = 0
        while i<len(start) and i<len(end) and start[i]==end[i]:
            i = i+1
        return start[:i]