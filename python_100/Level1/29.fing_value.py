# 29.Given an array of integers
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。示例:给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] = 2+7 =9,所以返回[0,1]

nums = [2,7,11,15]
target = 9

res = []


for i in nums:
    b = target - i 
    if b in nums:
        res.append(nums.index(i))
        res.append(nums.index(b))
        break

print(res)