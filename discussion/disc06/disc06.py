# Q 1.1

def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f


# Q 2.2

def mystery(p, q):
    p[1].extend(q)
    q.append(p[1:])

p = [2, 3]
q = [4, [p]]
mystery(q, p)


# Q 2.3

def group_by(s, fn):
    """
    # the original doctest result is {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}, which I think is wrong
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for el in s:
        key = fn(el)
        if key in list(grouped.keys()):
            grouped[key].append(el)
        else:
            grouped[key] = [el]
    return grouped


# Q 2.4

def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs
    in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(2, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    for _ in range(x):
        s.append(el)


# Q 4.1

def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range (5))
    >>> list(filter(all_odd, is_even))
    []
    >>> s = filter(range(1, 5), is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for el in iterable:
        if fn(el):
            yield el 
        

# Q 4.2

def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    a_term, b_term = next(a), next(b)
    while True:
        if a_term < b_term:
            yield a_term
            a_term = next(a)
        elif a_term > b_term:
            yield b_term
            b_term = next(b)
        else:
            yield a_term
            a_term, b_term = next(a), next(b)

