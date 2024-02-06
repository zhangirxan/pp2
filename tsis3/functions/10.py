def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

str = input()
nums = list(map(int, str.split()))

result = unique_elements(nums)
print(result)
