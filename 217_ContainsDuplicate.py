class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # for num in range(len(nums)):
        #     for iterate in range(num + 1, len(nums)):
        #         if nums[num] == nums[iterate]:
        #             return True
        # return False
        temp = nums.sort()
        for num in range(len(nums) - 1):
            # len(nums) - 1 -> to prevent list index out of range
            if nums[num] == nums[num + 1]:
                return True
        return False

a = Solution()
b = a.containsDuplicate([1,2,3,4,6])
print(b)
