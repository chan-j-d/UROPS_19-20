import math

def SR(x, y):
    t = x % y
    if t == x + y or (t != x and 2 * abs(t) <= abs(y)):
        return t
    else:
        return t - y

def sign(x):
    if x >= 0:
        return 1
    else:
        return -1

def member_of(tup, lst):
    for pair in lst:
        if tup[0] == pair[0] and abs(tup[1]) == abs(pair[1]):
            #print(tup, pair)
            return True
    return False

def rel_num(s, r, M):
    
    if abs(s / r) >= 4 or math.gcd(s, r) != 1 or s % r == 0:
        return True
    xi = r
    yi = (r - SR(r, s)) // s
    pair_tracker = [(xi, yi)]
    if yi == 0:
        return True
    
    for i in range(M):
        x_ = SR(xi, s * yi)
        y_ = SR(r * yi, x_)
        x_ = x_ * r
        d = math.gcd(x_, y_)
        sigma = sign(x_)
        if d != 1:
            xi = x_ * sigma // d
            yi = y_ * sigma // d
        else:
            xi = x_ * sigma
            yi = y_ * sigma
        if xi * yi * (xi - 1) == 0 or member_of((xi, yi), pair_tracker):
            pair_tracker.append((xi, yi))
            return True
        pair_tracker.append((xi, yi))

    return False

def min3(a, b, c):
    if a * b * c == 0 or a < 0 or c < 0:
        return
    if a % b == 0:
        return (-b / a, 1, c)
    y_bound = min(a - 2, c + abs(c - abs(a - abs(b))))
    xr = 1
    yr = 1
    min_val = abs(a + b + c)
    for y in range(-y_bound, y_bound + 1):
        if y == 0:
            continue
        t = - (c / y + b) / a
        x = int(t)
        if x == 0 or (x != - 1 and (t - x) > 0.5): x += 1
        min_temp = abs((a * x + b) * y + c)
        if min_temp < min_val:
            xr = x
            yr = y
            min_val = min_temp
    return (xr, yr, (a * xr + b) * yr + c)

def rel_num_min(s, r, M):
    
    if abs(s / r) >= 4 or math.gcd(s, r) != 1 or s % r == 0:
        return True
    xi = SR(r, s)
    yi = (r - SR(r, s)) // s
    if yi == 0:
        return True
    sigma = sign(xi)
    xi = sigma * xi
    yi = sigma * yi
    pair_tracker = [(xi, yi)]
    print(xi, yi)
    for i in range(M):
        u, v, x_ = min3(s * xi, s * r * yi, r * xi)
        y_ = r * yi + u * xi
        d = math.gcd(x_, y_)
        sigma = sign(x_)
        print(u, v, x_, y_, d)
        if d != 1:
            xi = x_ * sigma // d
            yi = y_ * sigma // d
        else:
            xi = x_ * sigma
            yi = y_ * sigma
        if xi * yi * (xi - 1) == 0 or member_of((xi, yi), pair_tracker):
            pair_tracker.append((xi, yi))
            print(pair_tracker)
            return True
        pair_tracker.append((xi, yi))
    return False


            
def matrix_mul(m1, m2):
    new_mat = []
    for i in range(len(m1)):
        new_row = []
        for j in range(len(m2)):
            ij_value = 0
            for k in range(len(m2)):
                ij_value += m1[i][k] * m2[k][j]
            new_row.append(ij_value)
        new_mat.append(new_row)
    return new_mat

s = 3
r = 2
m1 = [[1, 0], [1, 1]]
m1_ = [[1, 0], [-1, 1]]
m2 = [[r, s], [0, r]]
m2_ = [[r, -s], [0, r]]


def matrix_power(m1, n):
    if n == 1:
        return m1
    return matrix_mul(m1, matrix_power(m1, n - 1))

def test1():
    excep = []
    for r in range(2, 11):
        for s in range(2, 4 * r):
            if not rel_num(s, r, 5000):
                excep.append((s, r))
    print(excep)

def test2():
    excep = []
    for s in range(2, 31):
        for r in range(2, 10 * s + 1):
            if math.gcd(s, r) == 1 and not rel_num(s, r, 5000):
                excep.append((s, r))
    print(excep)
