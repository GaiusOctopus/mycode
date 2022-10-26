#!/usr/bin/env python3

def digit_count(x, b):
    count = 0
    while x > 0:
        count = count + 1
        x = x // b
    return count

def get_digits(x, b, init_k):
    k = digit_count(x, b)
    digits = []
    while x > 0:
        digits.append(x % b)
        x = x // b
    for i in range(k, init_k):
        digits.append(0)
    return digits

def form_number(digits, b):
    result = 0
    for i in range(0, len(digits)):
        result = result * b + digits[i]
    return result

def kaprekar_map(x, b, init_k):
    descending = form_number(sorted(get_digits(x, b, init_k), reverse=True), b)
    ascending = form_number(sorted(get_digits(x, b, init_k)), b)
    return descending - ascending

def kaprekar_cycle(x, b):
    x = int (str(x), b)
    init_k = digit_count(x, b)
    seen = []
    while x not in seen:
        seen.append(x)
        x = kaprekar_map(x, b, init_k)
    cycle = []
    while x not in cycle:
        cycle.append(x)
        x = kaprekar_map(x, b, init_k)
    return cycle
