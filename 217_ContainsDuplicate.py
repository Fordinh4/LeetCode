class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # ====== These are O(N^2) because i have to iterate thru every number on the list to check the duplicate
        # for num in range(len(nums)):
        #     for iterate in range(num + 1, len(nums)):
        #         if nums[num] == nums[iterate]:
        #             return True
        # return False

        # ======= These are O(n log n)
        # temp = nums.sort()
        # for num in range(len(nums) - 1):
        #     # len(nums) - 1 -> to prevent list index out of range
        #     if nums[num] == nums[num + 1]:
        #         return True
        # return False

        # =======
        # Another solution I found but in O(Log n) because of set(nums):
        # return len(set(nums)) != len(nums)
    
        # ----------
        # This solution use hash set so it's in O(1):
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)

        return False



a = Solution()
b = a.containsDuplicate([1,2,3,4,6])
print(b)
