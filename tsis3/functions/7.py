def has33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

str = input()
nums = list(map(int, str.split()))

result = has33(nums)
print(result)