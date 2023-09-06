import re


def solve_with_re(s):
    # Keep the leading and trailing spaces
    s_list = re.split(r'(\s+)', s)
    s_list = [string.capitalize() if string[0].isalpha() else string for string in s_list]
    return "".join(s_list)

