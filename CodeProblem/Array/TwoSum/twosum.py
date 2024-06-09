# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# First we have simple solution where we are doing nested looping on the list and coparing numbers in both loop and addition of those elemets should be equal to target.

# But the problem with this approach is that the time complaxity of this algo is O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]



# Here is the optimize soultion with O(n) time complaxity.

# What we are doing here is that we are first taking single element from the list and minus with target element if the result is in the list that means we have to return the indices
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target - nums[i]
            if (temp in nums and i != nums.index(temp)):
                return [i,nums.index(temp)]


obj = Solution.twoSum([3,2,4],6)

