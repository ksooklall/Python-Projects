"""
This script is a simple calculator that runs on the command line
The script uses Argparse to make command line commands
"""

# ArgparseL An argument parser
import argparse
import numpy as np
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type = float, default=1.0,
                        help = 'What is the first number?')
    parser.add_argument('--y', type = float, default=1.0,
                        help = 'What is your second number?')
    parser.add_argument('--operation', type = str, default='add',
                        help = 'What operation? (add,sub,div,mul,mod,exp,sqrt,nlog,pow2)')
    args= parser.parse_args()
    # print to the console
    sys.stdout.write(str(calc(args)))

def calc(args):
    operation = args.operation
    if args.operation =='add':
        return args.x+args.y
    elif args.operation =='sub':
        return args.x-args.y
    elif args.operation == 'div':
        return float(args.x/args.y)
    elif args.operation == 'mul':
        return args.x*args.y
    elif args.operation == 'mod':
        return args.x%args.y
    elif args.operation == 'exp':
        return np.exp(args.x),np.exp(args.y)
    elif args.operation == 'sqrt':
        # Numpy return error for invalid values
        return np.sqrt(args.x),np.sqrt(args.y)
    elif args.operation == 'nlog':
        # Numpy return error for invalid values
        return np.log(args.x),np.log(args.y)
    elif args.operation == 'pow2':
        return args.x**2, args.y**2

if __name__ == '__main__': main()
