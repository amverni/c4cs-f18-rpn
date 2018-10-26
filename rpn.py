#!/usr/bin/env python3

def caclulate(args):
    # stack for caclulator
    stack = []
    
    # tokenize input
    tokens = args.split()

    # process tokens
    for token in tokens:
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val1 - val2
            stack.append(result)
            return stack[0]

def main():
    while True:
        result = caclulate(input('rpn cacl> '))
        print(result)

if __name__ == '__main__':
    main()

