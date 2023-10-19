num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

sum1 = 0
for i in range(2, num1):
    if num1 % i == 0:
        sum1 += i

sum2 = 0
for j in range(2, num2):
    if num2 % j == 0:
        sum2 += j

if sum1 == num2 and sum2 == num1:
    print(f"{num1} and {num2} are amicable numbers.")
else:
    print(f"{num1} and {num2} are not amicable numbers.")
