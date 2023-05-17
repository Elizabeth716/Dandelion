"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def backspace_compare(first: str, second: str):
    def process_string(string: str) -> str:
        stack = []
        for c in string:
            if c == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)

    return process_string(first) == process_string(second)



"""
The backspaceCompare function takes two strings as input and returns a boolean indicating if they are equal after
processing them with the backspace rule. The process_string helper function takes a string and applies the backspace 
rule to it, returning the resulting string.

The main logic of the function is to compare the processed versions of both strings using the == operator. 
If they are equal, the function returns True, otherwise it returns False.
"""
