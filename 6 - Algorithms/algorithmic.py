# odd even
nums = [1, -3, 5, 7, 15, -4, 0, -6, -10, -11, 12]
sorte = 0
for i in range(len(nums)):
    for j in range(len(nums) - sorte):
        if nums[i] % 2 == 0:
            for k in range(i, len(nums) - 1):
                temp = nums[k + 1]
                nums[k + 1] = nums[k]
                nums[k] = temp
    sorte += 1
print(nums)

# positive negative
nums = [1, -3, 5, 7, 15, -4, 0, -6, -10, -11, 12]
sorte = 0
for i in range(len(nums)):
    for j in range(len(nums) - sorte):
        if nums[i] >= 0:
            for k in range(i, len(nums) - 1):
                temp = nums[k + 1]
                nums[k + 1] = nums[k]
                nums[k] = temp
    sorte += 1
print(nums)

# positive negative
nums = [1, -3, 5, 7, 15, -4, 0, -6, -10, -11, 12]
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[j] < 0:
            nums.append(nums.pop(j))
print(nums)

# sort names
