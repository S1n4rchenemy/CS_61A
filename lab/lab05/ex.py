def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    if (not t1) and t2:
        new_label = label(t2)
    elif t1 and (not t2):
        new_label = label(t1)
    elif (not t1) and (not t2):
        return []
    else:
        new_label = label(t1) + label(t2)
    
    #print('new label is', new_label)
    new_branches = []
    if len(branches(t1)) < len(branches(t2)):
        short_branches, long_branches = branches(t1), branches(t2)
    else:
        short_branches, long_branches = branches(t2), branches(t1)

    for i in range(len(short_branches)):
        new_branches = new_branches + [add_trees(branches(t1)[i], branches(t2)[i])]
    for i in range(len(short_branches), len(long_branches)):
        new_branches = new_branches + [long_branches[i]]

    #print('new branches are', new_branches)
    return tree(new_label, new_branches)

    #return tree(new_label, )




# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])