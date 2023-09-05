def permutation(x, y, z, n):
    result = []
    for x in range(0, x + 1):
        for y in range(0, y + 1):
            for z in range(0, z + 1):
                if x + y + z != n:
                    result.append([x, y, z])
    return result


def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print(permutation(x, y, z, n))


main()
