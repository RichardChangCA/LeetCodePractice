# this is time limit exceeded
def maxSubArray_expired(nums):
    new_nums = []
    item = 0
    n_list = []
    n = 1
    tag = 0
    while(True):
        if(n==len(nums)):
            break
        for i in range(len(nums)-n):
            if(n==1):
                if(item==0):
                    item = nums[i]
                if(item+nums[i+1]>max(item,nums[i+1])):
                    item += nums[i+1]
                    if(len(nums)==2):
                        return item
                    if(i==(len(nums)-n-1) and item!=nums[i]):
                        tag = 1
                        new_nums.append(item)
                        item = 0
                else:
                    new_nums.append(item)
                    item = 0
            else:
                if(n_list==[]):
                    for k in range(n+1):
                        n_list.append(nums[i+k])
                if(sum(n_list)>max(n_list)):
                    new_nums = new_nums + [sum(n_list)] + nums[i+n+1:] 
                    n_list=[]
                    tag = 1
                    break
                else:
                    new_nums.append(nums[i])
                    n_list=[]
        if(tag!=1):
            for k in range(n):
                new_nums.append(nums[i+k+1])
        n += 1
        if(tag == 1):
            n = 1
            tag = 0
        nums = new_nums
        print(nums)
        new_nums = []
    return max(nums)


def maxSubArray(nums):
    windowSum = nums[0]
    maxSum = nums[0]
    
    for i in range(1,len(nums)):
        windowSum = max(windowSum+nums[i], nums[i])
        maxSum = max(windowSum, maxSum)
    return maxSum


# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4,8,3,-5,0]))
# maxSubArray([-2, 1, -3, 6, -5, 4])
# maxSubArray([2,-1,1,1])
print(maxSubArray([-1,1,2,1]))

# Question:
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



