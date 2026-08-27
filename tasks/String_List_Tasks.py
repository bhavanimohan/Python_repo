# Input = ["hello", "world", "python"]
# empty_list = []
# for i in Input:
#     for j in i:
#         empty_list=[j]+empty_list
# print(empty_list)
        
    
# Input = ["madam", "hello", "level", "python", "radar"]
# empty_list = []
# for i in Input:
#     for j in i:
#         if i[j] == i[j-i]:
#             empty_list+=[j]
# print(empty_list)


Input = ["apple", "banana", "apple", "cat", "banana"]
empty_list = []
for i in Input:
    if i not in empty_list:
        empty_list.append(i)
print(empty_list)
    
