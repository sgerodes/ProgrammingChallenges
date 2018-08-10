class Solution:
    def moveZeroes(self, nums):
        zeros=0
        for i,num in enumerate(nums):
            if num == 0:
                zeros+=1
            else:
                nums[i-zeros]=num
        if zeros == 0:
            return
        nums[-zeros:] = [0]*zeros
        return
