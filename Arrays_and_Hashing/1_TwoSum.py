def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # for index in range(len(nums)):
    #     for count in range(index + 1, len(nums)):
    #         if nums[index] + nums[count] == target:
    #             return [index, count]

    # # This one is O(n^2) because of two operations in line 15 (each operation is O(n) so it add up)
    # for index, num in enumerate(nums):
    #     res = target - num
    #     if res in nums and nums.index(res) != index:
    #         return [index, nums.index(res)]

    # This one will be O(n):
    Prevmap = {} # The format will be value : index

    for i, n in enumerate(nums):
        # Because sum is a + b so if we want to find the value of b we can use sum - value of a
        res = target - n
        
        if res in Prevmap: 
            # Check if b is already in the dict yet
            return [Prevmap[res], i]
        # If not, add it in the dict
        Prevmap[n] = i



a = twoSum([2,5,5,11], 10)
print(a)