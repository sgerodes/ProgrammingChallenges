class Solution:
    def twoSum(self, nums, target):
        hashmap={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if (complement in hashmap.keys()):
                return [hashmap[complement],i]
            else:
                hashmap[nums[i]]=i
