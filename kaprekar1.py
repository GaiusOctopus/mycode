#!/usr/bin/env python3
"""" TLG NDE Python | LAncheta | Kaprekar's Constant """

def get_digits(x, b):
    digits = []
    while x > 0:
        digits.append(x % b)
        x = x // b
    return digits

def form_number(digits, b):
    result = 0
    for i in range(0, len(digits)):
        result = result * b + digits[i]
    return result

def kaprekar_map(x, b):
    descending = form_number(sorted(get_digits(x, b), reverse=True), b)
    ascending = form_number(sorted(get_digits(x, b)), b)
    return descending - ascending

def kaprekar_cycle(x, b):
    x = int (str(x), b)
    seen = []
    while x not in seen:
        seen.append(x)
        x = kaprekar_map(x, b)
    cycle = []
    while x not in cycle:
        cycle.append(x)
        x = kaprekar_map(x, b)
    return cycle
