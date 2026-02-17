import sys
from collections import Counter
input = sys.stdin.readline 
n = int(input())
total = 0  
for _ in range(n):
  k= list(map(int, input().split()) )
  l = k.count(1)  
  if l >= 2:
     total += 1
 
print(total)
