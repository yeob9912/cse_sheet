a,b=map(int,input().split())
limak_weight=a
bob_weight=b
count=0
while limak_weight <= bob_weight:
    limak_weight=limak_weight*3
    bob_weight=2*bob_weight
    count+=1
    if limak_weight > bob_weight:
        print(count)
        break
