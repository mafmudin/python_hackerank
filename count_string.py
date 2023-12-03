def count_string(string, sub_string):
    total = 0
    for i in range(0, len(string)):
        if sub_string == string[i:i+len(sub_string)]:
            total += 1
    return total


if __name__ == '__main__':
    print(count_string("ABCDCDC", "CDC"))