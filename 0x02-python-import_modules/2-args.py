#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    # get the length of the arguments passed on the command line
    c = sys.argv
    # remove the argument that interprets the code
    x = len(c) - 1
    # handle when there is onluy one command passed
    if x == 0:
        print(x, "arguments.")
    # handle when just one commmand is passed
    elif x == 1:
        print(x, "argument:")
        print("{}:".format(x), sys.argv[1])
    # handle when more than one command is passed
    else:
        print(x, "arguments:")
        for i in range(1, (x + 1)):
            print("{}:".format(i), sys.argv[i])
