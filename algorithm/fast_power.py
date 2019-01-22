# recursion

def power(x, n):
    if n == 0:
        return 1
    
    if n % 2 == 0:
        tmp = power(x, n // 2)
        return tmp * tmp
    else:
        tmp = power(x, n // 2)
        return tmp * tmp * x

# non-recursion
def power(x, n):
    ans = 1
    base = x
    while n > 0:
        if n % 2 == 1:
            ans *= base
        base *= base
        n = n // 2
    return ans
