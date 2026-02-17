for i in range(5):
    row=list(map(int,input().split()))
    if 1 in row:
        r=i+1
        c=row.index(1) + 1
print(abs(r-3) + abs(c-3) )
