def count_stair_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    count = 0
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        for i in range(k):
            count = count + count_k(n - i - 1, k)
        return count 
        
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [x * s[x] for x in range(0, len(s), 2)]

def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    def product(s):
        if s == []:
            return [1]
        else: 
            return [x * s[0] for x in product(s[2:])] + product(s[1:])
    
    return max(product(s))