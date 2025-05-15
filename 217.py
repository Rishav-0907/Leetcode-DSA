
# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_set= set()
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False   

# Dict
        # my_dict={}
        # for num in nums:
        #     # my_dict[num] = False
        #     if num in my_dict:
        #         my_dict[num] = True
        #         return True
        #     else:
        #         my_dict[num]= False
                
        # # print(my_dict)
        # # for x in my_dict.values():
        # #     print(x)
        # #     if x == True:
        # #         return True
        # return False   

# Set one liner approach 

        return len(set(nums)) != len(nums)
