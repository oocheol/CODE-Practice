def insertion_sort(x):
    for i in range(len(x)):
        
    
    return x


# def selection_sort(x):
#     res = []
    
#     for _ in range(len(x)):
#         a = x.index(min(x))
#         res.append(x.pop(x))
        
#     return res

# def bubble_sort(x):
#     for _ in range(len(x)):
#         for i in range(len(x)-1):
#             if x[i] >= x[i+1] :
#                 x[i], x[i+1] = x[i+1], x[i]
    
#     return x

n = int(input())
num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

insertion_sorted_list = insertion_sort(num_list)
print(" ".join(map(str, insertion_sorted_list)))

# selection_sorted_list = selection_sort(num_list)
# print(" ".join(map(str, selection_sorted_list)))

# bubble_sorted_list = bubble_sort(num_list)
# print(" ".join(map(str, bubble_sorted_list)))
