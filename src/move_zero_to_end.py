# Moving Zeros To The End

"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

def move_zeros(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]

"""
def move_zeros(a):
    a.sort(key=lambda v: v == 0)
    return a
"""
