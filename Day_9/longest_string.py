# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

#For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

x = ['ab','cd']

l1 = []

for i in x:
    ls = []   
    for j in i:
        print(j)
        ls.append(j)
    l1.append(ls)

print(l1)