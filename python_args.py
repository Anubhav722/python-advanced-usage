# There are three types of arguments in python
# 1. Arguments which are required
# 2. Arguments which are optional
# 3. Arguments which are mutually exclusive i.e. you can select 1 option or another option but not both.

import argparse

def fib(n):
    a, b = 0,1

    for i in range(n):
        a, b = b, a+b

    return a

def Main():
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    parser.add_argument("num", help="The fibonacci number you wish to calculate", type=int)

    # Passing optional arguments
    parser.add_argument("-o", "--output", help="Output result to file.", action="store_true")

    args = parser.parse_args()

    result = fib(args.num)

    if args.verbose:
        print("The " + str(args.num) + "th fib number is "+ str(result))
    elif args.quiet:
        print(result)
    else:
        print("Fib(" + str(args.num) + ") = " + str(result))


    if args.output:
        f = open("fibonacci.txt", "a")
        f.write(str(result) + "\n")

if __name__ == '__main__':
    Main()
