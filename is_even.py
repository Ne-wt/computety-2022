#!/usr/bin/env python3

# Complete this python script which outputs True if n is even and False otherwise.
# To make this task tricky…
# Your solution may not use %, the modulus operator or
# any python 'tricks' not coverred by the lessons up till Tues 17th May

# Example standard input 1
#   4

# Example standard output 1
#   True

# Example standard input 2
#   5

# Example standard output 2
#   False

n = int(input())
num = n - (n // 2) * 2
# n // 2 will equal to either n / 2 in the case of even,
# or n / 2 - .5 in the case of odd
# we can multiply this calculated value by 2, which will sum to either
# n or n - 1
# n - n = 0, therefore anything that evaluates to 0 is even
# n - (n - 1) = 1, therefore anything that evaluates to 1 is odd
print(num == 0)