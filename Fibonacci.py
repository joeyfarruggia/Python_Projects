def fibonacci_series(n):
    a, b = 0, 1
    series = []
    while a <= n:
        series.append(a)
        a, b = b, a + b
    return series

#test the function
n = 100
fib_series = fibonacci_series(n)
print(fib_series)