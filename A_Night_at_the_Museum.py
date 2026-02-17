t = "abcdefghijklmnopqrstuvwxyz"

prev = 'a'          # start from 'a'
rotation_sum = 0

s = input()

for i in range(len(s)):
    curr = s[i]

    p1 = ord(prev) - ord('a')
    p2 = ord(curr) - ord('a')

    clockwise = abs(p1 - p2)
    anticlockwise = 26 - clockwise

    min_rotation = min(clockwise, anticlockwise)
    rotation_sum += min_rotation

    prev = curr     # move pointer

print(rotation_sum)
