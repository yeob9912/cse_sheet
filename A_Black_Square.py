a = list(map(int, input().split()))
s = input()
s = [int(c) for c in s]  
count = 0

for l in range(len(s)):
    count += a[s[l] - 1]  

print(count)
