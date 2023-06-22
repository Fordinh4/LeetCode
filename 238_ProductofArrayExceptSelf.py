def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

        # First attempt:
        # import numpy
        # product_list = []

        # for i in range(len(nums)):
        #     product_list.append(int(numpy.prod(nums[:i]) * numpy.prod(nums[i+1:])))

        # return product_list

#==============================================================================
        # ===> Solution link: https://www.youtube.com/watch?v=bNvIQI2wAjk

        # prefix:
        # ->
        # |    a    |  a*b  | a*b*c | a*b*c*d |
        # postfix:
        # <-
        # | a*b*c*d | b*c*d |  c*d  |    d     |

        # the result is a multiply without the symbol in own position (the left value from prefix and the right one from postfix):
        # |  b*c*d  | a*c*d | a*b*d |   a*b*c  |

        product_list = [1]* len(nums)

        prefix = 1
        for i in range(len(nums)):
            product_list[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            product_list[i] *= postfix
            postfix *= nums[i]

        return product_list


a = productExceptSelf([1,2,3,4])
print(a)