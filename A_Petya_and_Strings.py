s=input()
t=input()
s=s.lower()
t=t.lower()
for i in range(len(s)):
    if s[i]<t[i]:
        print(-1)
        break
    elif s[i]>t[i]:
        print(1)
        break
else:
    print(0)
