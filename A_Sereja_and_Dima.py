n = int(input())
a = list(map(int, input().split()))
#use two pointer algorithm
l = 0
r = n - 1
serja_score = 0
dima_score = 0
turn = 0  # 0 = Sereja, 1 = Dima

while l <= r:
    if a[l] > a[r]:
        chosen = a[l]
        l += 1
    else:
        chosen = a[r]
        r -= 1

    if turn % 2 == 0:
        serja_score += chosen
    else:
        dima_score += chosen

    turn += 1

print(serja_score, dima_score)
