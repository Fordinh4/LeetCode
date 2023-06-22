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
    for index, num in enumerate(nums):
        res = target - num
        if res in nums and nums.index(res) != index:
            return [index, nums.index(res)]






a = twoSum([2,5,5,11], 10)
print(a)