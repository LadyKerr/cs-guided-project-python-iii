"""
Given an array of integers `nums` and an integer `target`, 
return the indices of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.

todo:
- find the two nums in the arr that equal the target
- return the index of those nums

explanation: https://levelup.gitconnected.com/two-sum-interview-problem-in-python-c1d84b029d35
"""
def two_sum(nums, target):
    # method 1 - O(n^2)
    for num in range(len(nums)):
        for next_num in range(num+1, len(nums)):
            if nums[num] + nums[next_num] == target:
                return [num, next_num]

    #method 2 - O(n)
    new_dict = {}

    for num in range(len(nums)):
        next_num = target - nums[num]
        if(next_num in new_dict.keys()):
            next_num = nums.index(next_num)
            if(num != next_num):
                return sorted([num, next_num])
        
        new_dict.update({nums[num]: num})


print(two_sum(nums = [2,5,9,13], target = 7))
print(two_sum(nums = [4,3,5], target = 8))

