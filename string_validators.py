if __name__ == '__main__':
    s = "qA2"
    result = [False, False, False, False, False]
    for i in range(0, len(s)):
        if result[0] is not True and s[i].isalnum():
            result[0] = True

        if result[1] is not True and s[i].isalpha():
            result[1] = True

        if result[2] is not True and s[i].isdigit():
            result[2] = True

        if result[3] is not True and s[i].islower():
            result[3] = True

        if result[4] is not True and s[i].isupper():
            result[4] = True

    for i in result:
        print(i)
