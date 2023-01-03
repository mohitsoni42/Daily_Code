#need to find if list contains dups

def dups(ls):
    op = set()

    for i in ls:
        if i in op:
            return True
        else:
            op.add(i)

    return False
ls = [1,2,3,4,1,2,3,4]
print(dups(ls))