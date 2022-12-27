# [1,2,3,4,5] should be [120,60,40,30, 24]
import math

def prod_of_value(ls):
    result = math.prod(ls)    
    for (i,n) in enumerate(ls):
        ls[i] = result//n
    
    print(ls)
    
ls= [1,2,3,4,5]
prod_of_value(ls)