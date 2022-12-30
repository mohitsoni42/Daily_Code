# best time to buy and sell stock for max profit

def profit(price, day):
    mins = 100
    profit =0 
    day = 0

    for (j,i)  in  enumerate(price):
        if i < mins:
            mins = i
        
        if  i- mins > profit:
            profit = i -mins
            day = j + 1


    return (profit, day)



price = [7,1,5,9,8,4]
day = [1,2,3,4,5,6]

print(profit(price, day))