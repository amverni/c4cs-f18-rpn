#!/usr/bin/env python3
import operator
from fractions import Fraction

def d2f(dec):
    return Fraction(dec)

def f2d(frac):
    if not isinstance(frac, Fraction):
        return frac
    return frac.numerator / frac.denominator

op = {
    '+': (2, operator.add),
    '-': (2, operator.sub),
    '*': (2, operator.mul),
    '/': (2, operator.floordiv),
    '^': (2, operator.pow),
    'd2f': (1, d2f),
    'f2d': (1, f2d)
}

def calculate(args):
    # stack for caclulator
    stack = []
    # process tokens
    for arg in args.split():
        print(stack)
        token = arg
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            # look up function in the operator table
            numArgs, func = op[token]
            args = []
            for arg in range(numArgs):
                args.append(stack.pop())
            args = args[::-1]
            print(*args)
            print(func)
            result = func(*args)
            stack.append(result)
    return int(stack[0])

def main():
    while True:
        result = calculate(input('rpn cacl> '))
        print(result)

if __name__ == '__main__':
    main()

