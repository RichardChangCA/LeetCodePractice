class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # new_nums = nums
        # i = 0
        # while(i<len(new_nums)):
        #     j = i + 1
        #     tag = 1
        #     while(j<len(new_nums)):
        #         if(new_nums[i]==new_nums[j]):
        #             tag = 0
        #             break
        #         else:
        #             j += 1
        #     if(tag==0):
        #         new_nums = new_nums[1:j]+new_nums[j+1:]
        #     else:
        #         return new_nums[i]
        
        empty_nums = []
        for i in nums:
            if(i not in empty_nums):
                empty_nums.append(i)
            else:
                empty_nums.remove(i)
        return empty_nums[0]

# Question:
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4