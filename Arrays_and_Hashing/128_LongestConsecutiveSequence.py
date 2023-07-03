def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        count_list = []
        flag = False
        temp_nums = sorted(set(nums))

        for i in range(len(temp_nums) - 1):
            if i == len(temp_nums) - 2:
                  flag = True

            if temp_nums[i+1] - temp_nums[i] == 1:
                  max_count += 1
            else:
                  # Append the current longest sequence and reset the count
                  count_list.append(max_count + 1)
                  max_count = 0

        if flag:
            # To count the last number in the list nums
            count_list.append(max_count + 1)

        try:
            return max(count_list)
        
        except:
             if nums == []:
                return 0
             else:
                return 1



# The cool solution i found:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence 
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet: # count the sequence 
                    length += 1
                longest = max(length, longest) # compare it with other sequence and check which one is the longest
        return longest





nums = [0,3,7,2,5,8,4,6,0,1]
a = longestConsecutive(nums)
print(a)