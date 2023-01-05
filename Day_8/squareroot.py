# find square root of a number

def root(n):
    i = 1
    while True:
        if  i * i > n:
            return i - 1
        
        i += 1


print(root(17))
