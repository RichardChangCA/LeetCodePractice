class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        replace_tag = -1
        replace_id = -1
        for i in range(len(nums)):
            if(nums[i]==0 and replace_id>=0):
                continue
            elif(nums[i]==0 and replace_id<0):
                replace_id = i
                replace_tag = 0
            elif(replace_tag==0):
                replace_tag = 1
            else:
                continue
            if(replace_tag == 1):
                t = nums[i]
                nums[i] = nums[replace_id]
                nums[replace_id] = t
                replace_tag = 0
                replace_id += 1
        return nums

# Question:
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.