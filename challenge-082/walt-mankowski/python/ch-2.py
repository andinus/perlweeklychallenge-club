from sys import argv

def is_interleave(a, b, c):
    if a == '' and b == '' and c == '':
        return 1

    try:
        if a[0] == c[0]:
            return is_interleave(a[1:], b, c[1:])
    except IndexError:
        pass

    try:
        if b[0] == c[0]:
            return is_interleave(a, b[1:], c[1:])
    except IndexError:
        pass

    return 0

a, b, c = argv[1:]

print(is_interleave(a, b, c))
