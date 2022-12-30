#reverse a string 

# 1. normally

def reverse_str(user_string):
    temp = ""
    for i in user_string:
        temp = i + temp
    return temp

user_string = "JuniperLife"
print(reverse_str(user_string))

# 2. better function

def reverse_2(temp_str):
    temp_str = temp_str[::-1]  
    return temp_str

temp = "Practice is best"
print(reverse_2(temp))

#3. improvise

def reverse_3(temp):
    temp = [temp[i] for i in range(len(temp) -1, -1,-1 )]
    return "".join(temp)

temp = "Best Or Nothing"
print(reverse_3(temp))