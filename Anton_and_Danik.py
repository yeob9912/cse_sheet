n=int(input())
s=input()
s=s.upper()
Danik=s.count("D")
Anton=s.count("A")
if Anton > Danik:
    print("Anton")
elif Anton < Danik:
    print("Danik")
else:
    print("Friendship")
