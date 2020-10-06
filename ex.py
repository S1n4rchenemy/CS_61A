# Trees

def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True 

def right_binarize(t):
    """Construct a right-branching binary tree."""
    return tree(label(t), binarize_branches(branches(t)))

def binarize_branches(bs):
    """Binarize a list of branches."""
    if len(bs) > 2:
        first, rest = bs[0], bs[1:]
        return [right_binarize(first), right_binarize(rest)]
    else:
        return [right_binarize(b) for b in bs]


# linked lists

empty = 'empty'
def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list'
    return [first, rest]

def first(s):
    """Return the first element of a linked list."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest onl applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def extend_link(s, t):
    """Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t 
    else:
        return link(first(s), extend_link(rest(s), t))

def apply_to_all_link(f, s):
    """Apply f to each element of s."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))


def join_link(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)

def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list."""
    if n == 0:
        return link(empty, empty)
    elif n < 0 or m == 0:
        return empty 
    else:
        using_m = partitions(n-m, m)
        #print('using_m is', using_m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        #print('with_m is', with_m)
        without_m = partitions(n, m - 1)
        #print('without_m is', without_m)
        return extend_link(with_m, without_m)

def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length 

def getitem_link(s, i):
    """Return the element at index i of linked list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)



# Lecture 16 Review Question (18sp mt2)

def combo(a, b):
    """Return the smallest integer with all of the digits of a and b (in order).

    >>> combo(531, 432)
    45312
    >>> combo(531, 4321)
    45321
    >>> combo(1234, 9123)
    91234
    >>> combo(0, 321)
    321
    """
    if a == 0 or b == 0:
        return a + b 
    elif a % 10 == b % 10:
        return combo(a // 10, b // 10) * 10 + a % 10 
    return  min(combo(a // 10, b) * 10 + a % 10, combo(a, b // 10) * 10 + b % 10)
