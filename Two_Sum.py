class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {} 
          # Create a dictionary to store numbers and their indices
        
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement needed to reach the target
            if complement in num_dict:
                return [num_dict[complement], i]  # If the complement is in the dictionary, return the indices
            num_dict[num] = i  # Otherwise, store the current number and its index in the dictionary
        
        # If no solution is found, return an empty list or handle it as needed
        return [] 