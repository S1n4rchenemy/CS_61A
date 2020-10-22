###############################
# Linked Lists Implementation #
###############################

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


################
# Question 2.1 #
################

def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk is Link.empty:
        return 0
    else:
        return lnk.first + sum_nums(lnk.rest)


################
# Question 2.2 #
################

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    first = 1
    for link in lst_of_lnks:
        if link is Link.empty:
            return Link.empty
        first *= link.first 
    rest = multiply_lnks([x.rest for x in lst_of_lnks])
    return Link(first, rest)


################
# Question 2.3 #
################

def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        lnk = lnk
    else:
        lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
        flip_two(lnk.rest.rest)


##################
# Question 2.4.1 #
##################

def filter_link_iter(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link_iter(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration      # doctest would not pass since StopIteration has more than one line of information 
    >>> list(filter_link_iter(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while not link is Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest


##################
# Question 2.4.2 #
##################

def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration       # doctest would not pass since StopIteration has more than one line of information
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    if not link is Link.empty:
        if f(link.first):
            yield link.first
        yield from filter_link(link.rest, f)
        

#############################
# Tree class implementation #
#############################

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches


################
# Question 3.1 #
################

def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    t.label = (t.label + 1 if t.label % 2 != 0 else t.label)
    if not t.is_leaf():
        for branch in t.branches:
            make_even(branch)


################
# Question 3.2 #
################

def square_tree(t):
    """
    Mutates a Tree t by squaring all its elements.
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> square_tree(t)
    >>> t.label
    1
    >>> t.branches[0].branches[0].label
    9
    """
    t.label = t.label ** 2
    if not t.is_leaf():
        for branch in t.branches:
            square_tree(branch)


################
# Question 3.3 #
################

def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    if t.is_leaf():
        if t.label == entry:
            return [[entry]]
        return []
    else:
        result = []
        for branch in t.branches:
            result += [[t.label] + sub_path for sub_path in find_paths(branch, entry) if sub_path]
        return result


################
# Question 3.4 #
################

def combine_tree(t1, t2, combiner):
    """
    >>> from operator import mul
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    new_label = combiner(t1.label, t2.label)
    new_branches = []
    for combo in zip(t1.branches, t2.branches):
        new_branches += [combine_tree(combo[0], combo[1], combiner)]
    return Tree(new_label, new_branches)


################
# Question 3.5 #
################

def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    >>> t.label
    -1
    >>> t.branches[0].label
    2
    >>> t.branches[1].label
    4
    >>> t.branches[0].branches[0].label
    -3
    """
    t.label = map_fn(t.label)
    if not t.is_leaf():
        for branch in t.branches:
            if not branch.is_leaf():
                for sub_branch in branch.branches:
                    alt_tree_map(sub_branch, map_fn)
