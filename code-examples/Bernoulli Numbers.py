def bernoulli_numbers(n):
    bern = [0] * (n+1)
    bern[0] = 1
    for m in range(1, n+1):
        b = 0
        for k in range(m+1):
            b = (b * (m-k+1)) // k - bern[k] * (m-k+1) // k
        bern[m] = b
    return bern[:n+1]

print(bernoulli_numbers(10))
