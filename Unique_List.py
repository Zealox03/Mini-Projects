nums = [1,2,2,3,3,4,4,5,5,5]
unique = []


# Take note between is not and not in
for n in nums:
    if n not in unique:
        unique.append(n)

print(unique)