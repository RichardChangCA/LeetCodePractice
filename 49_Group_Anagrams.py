# Question:
# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

# Time Limit Exceeded

#  class Solution:
#     def merge(self,arr,l,m,r):
#         n1 = m - l + 1
#         n2 = r- m 

#         # create temp arrays 
#         L = [0] * (n1) 
#         R = [0] * (n2) 

#         # Copy data to temp arrays L[] and R[] 
#         for i in range(0 , n1): 
#             L[i] = arr[l + i] 

#         for j in range(0 , n2): 
#             R[j] = arr[m + 1 + j] 

#         # Merge the temp arrays back into arr[l..r] 
#         i = 0     # Initial index of first subarray 
#         j = 0     # Initial index of second subarray 
#         k = l     # Initial index of merged subarray 

#         while i < n1 and j < n2 : 
#             if L[i] <= R[j]: 
#                 arr[k] = L[i] 
#                 i += 1
#             else: 
#                 arr[k] = R[j] 
#                 j += 1
#             k += 1

#         # Copy the remaining elements of L[], if there 
#         # are any 
#         while i < n1: 
#             arr[k] = L[i] 
#             i += 1
#             k += 1

#         # Copy the remaining elements of R[], if there 
#         # are any 
#         while j < n2: 
#             arr[k] = R[j] 
#             j += 1
#             k += 1
    
#     def merge_sort(self,arr,l,r):
#         if(l<r):
#             m = (l+r-1)//2
#             self.merge_sort(arr,l,m)
#             self.merge_sort(arr,m+1,r)
#             self.merge(arr,l,m,r)
#         return arr

#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         output_list = []
#         for item in strs:
#             tag = 0
#             item_list = list(item)
#             item_set = self.merge_sort(item_list,0,(len(item_list)-1))
#             if(output_list == []):
#                 output_list.append([item])
#                 continue
#             for sub_set in range(len(output_list)):
#                 sub = list(output_list[sub_set][0])
#                 if(item_set == self.merge_sort(sub,0,(len(sub)-1))):
#                     output_list[sub_set].append(item)
#                     tag = 1
#                     break
#             if(tag!=1):
#                 output_list.append([item])
#         return output_list


# second solution with time limit exceeded
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         output_list = []
#         for item in strs:
#             tag = 0
#             item_set = sorted(list(item))
#             if(output_list == []):
#                 output_list.append([item])
#                 continue
#             for sub_set in range(len(output_list)):
#                 if(item_set == sorted(list(output_list[sub_set][0]))):
#                     output_list[sub_set].append(item)
#                     tag = 1
#                     break
#             if(tag!=1):
#                 output_list.append([item])
#         return output_list

# import collections
def groupAnagrams(strs):
    # output_list = collections.defaultdict(list)
    output_list = {}
    for item in strs:
        output_list[tuple(sorted(list(item)))] = []
    for item in strs:
        output_list[tuple(sorted(list(item)))].append(item)
    return output_list.values()

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))