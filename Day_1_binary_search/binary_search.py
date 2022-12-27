# Program to implement binary search with iterator

def  binary_search(list_num, target):
    start = 0
    end = len(list_num) -1
    mid = 0
    while (start <= end):
        mid = (start + end) // 2
        if (list_num[mid] > target):
            end = mid -1
        elif (list_num[mid] < target):
            start = mid + 1
        else:
            return mid +1
    return None

list_num = [11,23,32,45,51,67,79,82,95]
t = 32
print("Number presnt at", binary_search(list_num, t))