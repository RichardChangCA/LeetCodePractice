# Question:
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

# solution 1, this solution is fater than the second with less memory usage
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 1
        zero_index = []
        for i in range(len(nums)):
            if(nums[i]==0):
                zero_index.append(i)
            else:
                count *= nums[i]
        output = []
        for i in range(len(nums)):
            if(len(zero_index)>1):
                output.append(0)
            elif(len(zero_index)==0):
                 output.append(int(count/nums[i]))
            else:
                 if(nums[i]==0):
                    output.append(int(count))
                 else:
                    output.append(0)
        return output

# solution 2:
import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = 1
        R = 1
        L_list = [L]
        R_list = [R]
        length = len(nums)
        for i in range(length-1):
            L *= nums[i]
            L_list.append(int(L))
            R *= nums[length-1-i]
            R_list.append(int(R))
        R_list.reverse()
        output = np.array(L_list) * np.array(R_list)
        return output

