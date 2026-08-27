Input = ["hello", "world", "python"]
empty_list = []
for i in Input:
    reverse = ""

    for j in i:
        reverse=j+reverse
    empty_list.append(reverse)
print(empty_list)
        
    
Input = ["madam", "hello", "level", "python", "radar"]
empty_list = []
for i in Input:
    reverse = ""
    for j in i:
        reverse=j+reverse
    if i == reverse:
        empty_list.append(reverse)
print(empty_list)


Input = ["apple", "banana", "apple", "cat", "banana"]
empty_list = []
for i in Input:
    if i not in empty_list:
        empty_list.append(i)
print(empty_list)

# Input = ["cat", "dog", "apple", "bat", "mango"]
# len_3 = []
# len_5 = []
# for i in Input:
#     if len(i) == 3:
#         len_3.append(i)
#     if len(i) == 5:
#         len_5.append(i)


a =  ["apple", "banana", "mango"]
b = ["banana", "orange", "apple"]
empty_list = []
for char in a:
    if char in b:
        empty_list.append(char)
print(empty_list)

    
