def paths(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)


def max_subseq_sucks(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maxumum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"
    digits = []
    x, next_n = n, 0 

    while x > 0:
        digits = [x % 10] + digits 
        x = x // 10
    
    if t == 0:
        return 0
    else:
        if t > len(digits):
            for _ in range(t - len(digits)):
                digits = [0] + digits 

        digit_chosen =  max(digits[0: (len(digits) - t + 1)])

        for i in range(len(digits) - t + 1):
            if digits[i] == digit_chosen:
                index_chosen = i
                break

        for i in range(index_chosen + 1, len(digits)):
            next_n = digits[i] * 10 ** (len(digits) - i - 1) + next_n

        return digit_chosen * 10 ** (t - 1)  + max_subseq_sucks(next_n, t - 1)


def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"

    def subseq(n, r):
        if r == 0 or n == 0:
            return [0]
        else:
            addition = (n % 10) * 10 ** (t - r)
            return [x + addition for x in subseq(n // 10, r - 1)] + subseq(n // 10, r)
    
    return max(subseq(n, t))


def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    """
    "*** YOUR CODE HERE ***"
    if w1 == '':
        return w2
    else:
        if w1[0] == w2[0]:
            # print('case 1: w1, w2 are', w1, ', ', w2)
            return add_chars(w1[1 : len(w1)], w2[1 : len(w2)])
        else:
            # print('case 2: w1, w2 are', w1, ', ', w2)
            return w2[0] + add_chars(w1, w2[1 : len(w2)])
    