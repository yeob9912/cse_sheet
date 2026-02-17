import math
 
Y, W = map(int, input().split())
max_roll = max(Y, W)
successful_outcomes = 6 - max_roll + 1
total_outcomes = 6
gcd = math.gcd(successful_outcomes, total_outcomes)
numerator = successful_outcomes // gcd
denominator = total_outcomes // gcd
print(f"{numerator}/{denominator}")
