# Strip Comments

"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:
Given an input string of:
  apples, pears # and bananas
  grapes
  bananas !apples

The output expected would be:
  apples, pears
  grapes
  bananas

The code would be called like so:

result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
result should
  apples, pears\n
  grapes\n
  bananas
"""


def solution(string, markers):
    s_list = string.split("\n")
    for marker in markers:
        s_list = [i.split(marker)[0].rstrip() for i in s_list]
    return "\n".join(s_list)
