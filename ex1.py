def find(s, n):
# write your implementation here
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] + s[j] == n:
                return [i, j]
    return None

print(find([2, 7, 11, 15], 9))
print(find([3, 2, 4], 6))
print(find([3, 3], 6)) 