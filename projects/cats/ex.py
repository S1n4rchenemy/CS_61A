from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime

ref = 'TEM is Transmission Electron Microscope.'
typed = 'TEM is Transmission Electron Microscope?'
test = split(lower('TEM is Transmission Electron Microscope.'))


def expt(s):
    for x in s:
        if x == 'transmission':
            print(x)
            return True 
        else:
            print(x) 
            # return False 

expt(test)


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    check_list = [1 for x in range(len(reference_words)) if typed_words[x] == reference_words[x]]
    return (sum(check_list) / len(typed_words)) * 100


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'

    if limit - abs(len(start) - len(goal)) < 0: # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 1024
        # END
    
    elif len(start) == 0 or len(goal) == 0:
        return abs(len(start) - len(goal))

    elif start[0] == goal[0]: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return pawssible_patches(start[1:], goal[1:], limit)
        # END

    else:
        add_diff = 1 + pawssible_patches(goal[0] + start, goal, limit - 1) # Fill in these lines
        remove_diff = 1 + pawssible_patches(start[1:], goal, limit - 1)
        substitute_diff = 1 + pawssible_patches(goal[0] + start[1:], goal, limit - 1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        return min(add_diff, remove_diff, substitute_diff)
        # END


def report_progress(typed, prompt):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    count = 0
    for i in range(len(typed)):
        if typed[i] == prompt[i]:
            count += 1
        else:
            break 
    progress = count / len(prompt)
    return progress

typed = ['I', 'have', 'begun']
prompt = ['I', 'have', 'begun', 'to', 'type']
report_progress(typed, prompt)


def time_cal(times_per_player): 
    def time_diff(s):
        return [s[i] - s[i-1] for i in range(1, len(s))]
    times = [time_diff(times_per_player[i]) for i in range(len(times_per_player))]
    return times 

p = [[1, 4, 6, 7], [0, 4, 6, 9]]
print(time_cal(p))