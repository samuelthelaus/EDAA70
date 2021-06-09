
def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


class Frac:
    def __init__(self, numer, denom):
        divisor = gcd(numer, denom)
        self.numer = numer//divisor
        self.denom = denom//divisor

    def __str__(self):
        return f'{self.numer}/{self.denom}'
    
    def add(self, fr2):
        num = self.numer * fr2.denom + self.denom * fr2.numer
        den = self.denom * fr2.denom
        return Frac(num, den)
    
    def sub(self, fr2):
        num = self.numer * fr2.denom - self.denom * fr2.numer
        den = self.denom * fr2.denom
        return Frac(num, den)

    def mul(self, fr2):
        num = self.numer * fr2.numer
        den = self.denom * fr2.denom
        return Frac(num, den)

    def div(self, fr2):
        num = self.numer * fr2.denom
        den = self.denom * fr2.numer
        return Frac(num, den)

    def __add__(self, fr2):
        return self.add(fr2)

    def __sub__(self, fr2):
        return self.sub(fr2)

    def __mul__(self, fr2):
        return self.mul(fr2)

    def __truediv__(self, fr2):
        return self.div(fr2)


# x = Frac(1, 3)
# print(x.numer, x.denom)

# print(Frac(3, 9))

# x = Frac(1, 3)
# y = Frac(1, 6)

# z = x.add(y)

# print(x)
# print(y)
# print(z)

# print(Frac(1, 3).add(Frac(1, 3)).add(Frac(1, 6)).add(Frac(1, 6)))

# print(Frac(1, 3).add(Frac(1, 3)).add(Frac(1, 6).mul(Frac(1,6))))

# print(Frac(1, 6).mul(Frac(1, 6)).add(Frac(1, 3)).add(Frac(1, 3)))

sum = Frac(1,3) - Frac(1,6)

print(sum)