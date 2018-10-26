#!/usr/bin/env python3
import operator

op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}

def calculate(args):
    # stack for caclulator
    stack = []
    # process tokens
    # while len(stack) > 1:
    for arg in args.split():
        token = arg
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            val2 = int(stack.pop())
            val1 = int(stack.pop())

            # look up functino in the operator table
            func = op[token]
            result = func(val1, val2)
            stack.append(str(result))
    return int(stack[0])

def main():
    while True:
        result = calculate(input('rpn cacl> '))
        print(result)

if __name__ == '__main__':
    main()

