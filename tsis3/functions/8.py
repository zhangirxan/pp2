def spy_game(nums):
    index_0 = 0
    index_1 = 0
    index_2 = 0
    for num in nums:
        if num == 0 and index_0 == 0:
            index_0 += 1
        elif num == 0 and index_1 == 1:
            index_1 += 1
        elif num == 7 and index_2 == 2:
            return True
        elif num == 0 and index_2 == 2:
            index_2 = 1
        elif num == 0 and index_1 == 1:
            index_1 = 0
        elif num == 0 and index_0 == 0:
            index_0 = 0
        elif num == 0 and index_0 == 1:
            index_1 += 1
        elif num == 7 and index_1 == 1:
            index_2 += 1
            return True
    else:
        return False

str = input()
nums = list(map(int, str.split()))

result = spy_game(nums)
print(result)