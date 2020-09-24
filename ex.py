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