#Sum of Numbers from 1 to N
n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)

