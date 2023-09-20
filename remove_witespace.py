import json
import re

import pyperclip


def remove_white_space(text):
    regex_pattern = re.compile(r"\s")
    return regex_pattern.sub("", text)


if __name__ == "__main__":
    data = ""
    with open('example.json', 'r') as File:
        data = json.load(File)

    try:
        pyperclip.copy(remove_white_space(data['identity_image']))
        print("success copy")
    except:
        print("error copy")
