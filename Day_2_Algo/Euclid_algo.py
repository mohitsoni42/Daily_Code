# algo to find HCF or GCD of 2 numbers

def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

print(GCD(3234,2355))