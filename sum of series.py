def sum_series(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

n = int(input("Enter the number of terms in the series: "))
result = sum_series(n)
print("The sum of the series is:", result)