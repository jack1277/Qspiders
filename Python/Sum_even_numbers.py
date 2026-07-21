# WAP to get sum of even numbers between range 0 to 20

sum_even = 0
num = 0
while num <= 20:
    if num % 2 == 0:
        sum_even += num
    num += 1

print(f"Sum of even numbers between 0 to 20: {sum_even}")
