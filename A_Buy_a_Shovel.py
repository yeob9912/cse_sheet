price,coins=map(int,input().split())
for i in range(1,11):
   total=price*i
   if total%10==0 or total%10==coins:
       print(i)
       break
