class Solution:
    def twoSum(self, nums, target):
        lookup = {}

        for i in range(len(nums)):
            if nums[i] in lookup:
                return [lookup[nums[i]], i]
            else:
                lookup[target - nums[i]] = i

        return None


# instance of the class
s = Solution()

# Define an input array and target value
nums = [2, 7, 11, 15]
target = 9

# twoSum method with the input
result = s.twoSum(nums, target)


print(result)
