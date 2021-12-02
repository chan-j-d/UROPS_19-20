import sys
path = 'C:/Users/raido/Desktop/NUS/NUS Year 1 Sem 2/UROPS/v2'
if path not in sys.path:
    sys.path.append(path)
import math

def create_q(p, q):
    return Rational_Number(p, q)
    
def create_q_tup(tup):
    return Rational_Number_tup(p, q)
    
def sign(x):
    if x == 0: return 0
    elif x > 0: return 1
    else: return -1

class Rational_Number:
    
    def __init__(self, p, q):
        
        #Gets rid of common denominators and always fixes q as the negative number
        if (q == 0):
            p = 1
        elif p == 0:
            q = 1
        else:
            gcd = math.gcd(p, q)
            sigma = sign(p)
            p = p * sigma // gcd
            q = q * sigma // gcd
            
        self.p = p
        self.q = q
        
    @staticmethod
    def create_q_tup(tup):
        return Rational_Number(tup[0], tup[1])
        
    def __repr__(self):
        return "(%d, %d)" % (self.p, self.q)
        
    def get_p(self):
        return self.p
        
    def get_q(self):
        return self.q
    
    def __add__(self, other):
        if type(other) == int:
            other = Rational_Number(other, 1)
        new_p = self.p * other.q + self.q * other.p
        new_q = self.q * other.q
        return Rational_Number(new_p, new_q)
        
    def __neg__(self):
        return Rational_Number(-self.p, self.q)
        
    def __sub__(self, other):
        if type(other) == int:
            other = Rational_Number(other, 1)
        return self + (-other)
        
    def __mul__(self, other):
        if type(other) == int:
            other = Rational_Number(other, 1)
        new_p = self.p * other.p
        new_q = self.q * other.q
        return Rational_Number(new_p, new_q)
    
    def inverse(self):
        return Rational_Number(self.q, self.p)
        
    def __truediv__(self, other):
        if type(other) == int:
            other = Rational_Number(other, 1)
        return self * other.inverse()

    def __abs__(self):
        return Rational_Number(abs(self.p), abs(self.q))
        
    def is_infinity(self):
        return self.q == 0
        
    def float_rep(self):
        return self.p / self.q
        
    def tup_rep(self):
        return (self.p, self.q)
        
    def sign(self):
        if self.p == 0: return 0
        elif self.q >= 0: return 1
        else: return -1
    
    def __lt__(self, other):
        return (self - other).sign() == -1
        
    def __eq__(self, other):
        return (self - other).sign() == 0
        
    def __le__(self, other):
        return (self - other).sign() in [-1, 0]
        
    def __gt__(self, other):
        return (self - other).sign() == 1
        
    def __ge__(self, other):
        return (self - other).sign() in [0, 1]
        
    def __ne__(self, other):
        return (self - other).sign() != 0
        
    def __hash__(self):
        return hash((self.p, self.q))
