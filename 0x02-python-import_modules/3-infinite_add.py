#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    a = 0

    for x in range(1, n):
        a = a + int(sys.argv[x])
    print(a)
