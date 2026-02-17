t = int(input())
prev = input()
groups = 1  

for i in range(t - 1):
    n = input()
    if n != prev:
        groups += 1  
    prev = n

print(groups)
