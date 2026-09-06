class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
       
        anagram_groups = {} 

        for i in range(len(strs)):

            original_word = strs[i]
            sorted_key = "".join(sorted(original_word))

            if sorted_key not in anagram_groups:
                anagram_groups[sorted_key] = []

            anagram_groups[sorted_key].append(original_word)
 
        return list(anagram_groups.values())
