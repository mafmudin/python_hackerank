def split_and_join(text):
    return "-".join(text.split(" "))


line = input()
result = split_and_join(line)
print(result)
