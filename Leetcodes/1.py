# class Solution(object):
#     def twoSum(self, nums:[2,7,9,11], target:9):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """

#         for x in range(len(nums)):
#             for i in range(x+1,len(nums)):
#                 if i==target-nums[x]:
#                     return [x,i]
#                     print(x,i)
#         return []


# class Solution(object):
#     def twoSum(self, nums=[2,7,9,11], target=9):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         h={}
#         for i ,num in enumerate(nums):
#          h[num]=i
#         for x in range(len(nums)):
#            req=target-nums[x]
#            if req in h and h[req]!=x:
#               return [x,h[req]]
