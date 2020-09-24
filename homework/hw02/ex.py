from operator import sub, mul 

def num_eights(x):
    if x < 10:
        if x == 8:
            return 1
        return 0
    else:
        return num_eights(x % 10) + num_eights(x // 10)


def pingpong(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        if num_eights(n - 1) or ((n - 1) % 8 == 0):
            return pingpong(n - 2)
        else:
            return 2 * pingpong(n - 1) - pingpong(n - 2)

def missing_digits(n):
    if n < 10:
        return 0
    elif n < 100:
        if n % 10 == n // 10:
            return 0
        else:
            return n % 10 - n // 10 - 1
    else:
        return missing_digits(n % 100) + missing_digits(n // 10)

def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def count_coins(total):

    def real_count(total, coin):
        if coin == None:
            return 0
        elif total - coin == 0:
            return 1
        elif total - coin < 0:
            return 0
        else:
            return real_count(total - coin, coin) + real_count(total, next_largest_coin(coin))
    
    return real_count(total, 1)


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda x: f(f, x))(lambda f, n: 1 if n == 1 else mul(n, f(f, sub(n, 1))))



