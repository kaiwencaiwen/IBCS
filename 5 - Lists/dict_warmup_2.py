import random
# Q1
nums = {i: 0 for i in range(10)}
for k in range(10000):
    nums[random.randint(0, 9)] += 1
print(nums)

# Q2
nums2 = {i: [] for i in range(9)}
for k in range(10000):
    somenum = random.uniform(0, 9)
    nums2[int(somenum)].append(somenum)
print(nums2)
