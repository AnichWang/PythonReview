'''
斐波那契数列
f0 = 0
f1 = 1
fn = f[n-1] + f[n-2] (n>=2)
'''


# recurrence
def fib(n):
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print
    fib(10)