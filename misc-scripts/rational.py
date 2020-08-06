class rational:
	"""
    	A rational number class.
    
    	Fractions are automatically reduced.

    	All basic numeric operators are overloaded, and work 
    	when the other operand is an integer.
    
    	Note that this class can't make division with both 
    	operands integers return a rational, so be careful!

    	Hashing is also supported, and the hash of n/1 will 
    	always be the same as hash of n, so rationals can be 
    	used safely as a keys in dicts.

    	str() and repr() work properly.
    	"""
    	def __init__(self, num, den = 1l):
        	assert isinstance(num, (int, long))
        	assert isinstance(den, (int, long))
        	if den == 0:
            		raise ZeroDivisionError
        	if den < 0:
            		num, den = -num, -den
        	n, d = abs(num), abs(den)
        	p, q = max(n, d), min(n, d)
        	while q != 0:
            		p, q = q, p % q
        	self.num, self.den = num / p, den / p

    	def __neg__(self):
        	return rational(-self.num, self.den)

    	def __str__(self):
        	if self.den == 1:
            		return str(self.num)
        	return str(self.num) + '/' + str(self.den)

    	def __repr__(self):
        	return 'rational(' + str(self.num) + ',' + str(self.den) + ')'

    	def __add__(self, other):
        	if isinstance(other, (int, long)):
            		return rational(self.num + other * self.den, self.den)
        	return rational(self.num * other.den + other.num * self.den,
            		self.den * other.den)

    	__radd__ = __add__

    	def __sub__(self, other):
        	return self + (-other)

    	def __rsub__(self, other):
        	assert isinstance(other, (int, long))
        	return other + (-self)

    	def __mul__(self, other):
        	if isinstance(other, (int, long)):
            		return rational(self.num * other, self.den)
        	return rational(self.num * other.num, self.den * other.den)

    	__rmul__ = __mul__

    	def __div__(self, other):
        	if isinstance(other, (int, long)):
            		return rational(self.num, self.den * other)
        	return rational(self.num * other.den, self.den * other.num)

    	__truediv__ = __div__

    	def __rdiv__(self, other):
        	assert isinstance(other, (int, long))
        	return rational(other * self.den, self.num)

    	__rtruediv__ = __rdiv__

    	def __cmp__(self, other):
        	if isinstance(other, (int, long)):
            		return cmp(self.num, other * self.den)
        	return cmp(self.num * other.den, other.num * self.den)

    	def __eq__(self, other):
        	if isinstance(other, (int, long)):
            		return self.den == 1 and self.num == other
        	return self.num == other.num and self.den == other.den

    	def __hash__(self):
        	return hash(self.num * self.den + self.den - 1)

def test_rational():
	rs = [rational(2, 2), rational(1, 2), rational(0, 2),
        	rational(-1, 2), rational(2, -2)]
    	for i in xrange(len(rs)):
        	for j in xrange(i):
            		assert rs[j] > rs[i]
    	assert rational(0) == rational(0, 2)
    	assert rational(-1, 1) == rational(2, -2)
    	assert rational(6, 9) == rational(-2, -3)
    	assert hash(rational(0, 2)) == hash(0)
    	assert hash(rational(1, 1)) == hash(1)
    	assert hash(rational(-1, 1)) == hash(-1)
    	assert -rs[2] == rs[2]
    	assert -rs[0] == rs[4]
    	assert --rs[0] == rs[0]
    	assert rs[0] == 1
    	assert rs[1] != 1
    	assert rs[0] < 2
    	assert rs[0] > 0
    	assert rs[1] < 1
    	assert rs[1] > 0
    	assert rs[1] - 1 == rs[3]
    	assert 1 - rs[1] == rs[1]
    	assert rs[1] + rs[3] == 0
    	assert rs[1] * 2 == 1
    	assert rs[1] * rs[3] == rational(1, -4)
    	assert rs[1] / rs[3] == -1
    	assert 2 / rs[1] == 4
    	assert rs[1] / 2 == rational(1, 4)
