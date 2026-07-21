#program to calculate the sum of odd numbers between 0 to 20

sum_odd = 0
num = 0
while num < 21:
    if num % 2 != 0:
        sum_odd += num
    num += 1

print(f"Sum of odd numbers between 0 to 20: {sum_odd}")

