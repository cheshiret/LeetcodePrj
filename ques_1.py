# -*-coding:utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #遍历List，两两求和，与target 比较，返回，下标
        #已提交
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

if __name__ == '__main__':
    print "----------------- start -----------------"
    res = Solution().twoSum([2,7,1,4],9)
    print res
    print "----------------- end -------------------"
