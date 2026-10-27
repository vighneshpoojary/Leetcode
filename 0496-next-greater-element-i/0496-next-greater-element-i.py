class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
    """
        # Dictionary to store the next greater element for each number in nums2
        nge_map = {}
        stack = []
        
        # Traverse nums2 from right to left
        for num in reversed(nums2):
            # Pop elements from the stack that are smaller than or equal to the current number
            while stack and stack[-1] <= num:
                stack.pop()
            
            # If the stack is empty, there is no greater element to the right
            if not stack:
                nge_map[num] = -1
            else:
                # The top of the stack is the next greater element
                nge_map[num] = stack[-1]
                
            # Push the current element onto the stack
            stack.append(num)
            
        # For each element in nums1, look up its pre-calculated next greater element from the map
        return [nge_map[num] for num in nums1]