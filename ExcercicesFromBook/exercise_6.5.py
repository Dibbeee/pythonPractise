
# Built upon that if 'r' is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r), and thus, 
# our base case that we can use is gcd(a, 0) = a.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(140,25))