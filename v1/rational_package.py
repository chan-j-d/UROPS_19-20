import math

def create_q(x, y):
    if y == 0:
        return (1, 0)
    gcd = math.gcd(x, y)
    sigma = sign(x)
    x *= sigma
    y *= sigma
    if gcd != 1:
        x = x // gcd
        y = y // gcd
    return (x, y)

def create_q_tup(tup):
    return create_q(tup[0], tup[1])

def get_s(q):
    return q[0]

def get_r(q):
    return q[1]

def add_q(q1, q2):
    numerator = get_s(q1) * get_r(q2) + get_s(q2) * get_r(q1)
    denominator = get_r(q1) * get_r(q2)
    return create_q(numerator, denominator)

def minus_q(q1, q2):
    numerator = get_s(q1) * get_r(q2) - get_s(q2) * get_r(q1)
    denominator = get_r(q1) * get_r(q2)
    return create_q(numerator, denominator)

def multiply_q(q1, q2):
    return create_q(get_s(q1) * get_s(q2), get_r(q1) * get_r(q2))

def divide_q(q1, q2):
    return multiply_q(q1, inverse_q(q2))

def inverse_q(q):
    return create_q(get_r(q), get_s(q))

def abs_q(q):
    s = abs(get_s(q))
    r = abs(get_r(q))
    return create_q(s, r)

def compare_q(q1, q2):
    if equal_q(q1, q2):
        return 0
    elif get_s(q1) / get_r(q1) > get_s(q2) / get_r(q2):
        return 1
    else:
        return -1

def less_than(q1, q2):
    return compare_q(q1, q2) == -1

def less_than_or_eq(q1, q2):
    return compare_q(q1, q2) in (0, -1)

def greater_than(q1, q2):
    return compare_q(q1, q2) == 1

def greater_than_or_eq(q1, q2):
    return compare_q(q1, q2) in (0, 1)

def equal_q(q1, q2):
    s1, r1 = get_s(q1), get_r(q1)
    s2, r2 = get_s(q2), get_r(q2)
    gcd1 = math.gcd(s1, r1)
    gcd2 = math.gcd(s2, r2)
    sigma1 = sign(s1)
    sigma2 = sign(s2)
    s1, r1 = s1 * sigma1 // gcd1, r1 * sigma1 // gcd1
    s2, r2 = s2 * sigma2 // gcd2, r2 * sigma2 // gcd2
    return s1 == s2 and r1 == r2

def sign(x):
    if x >= 0:
        return 1
    else:
        return -1

def float_rep(q):
    if not is_infinity(q):
        return get_s(q) / get_r(q)
    
def is_infinity(q):
    return get_r(q) == 0
