def sq_num(num):
    res = num **2
    return res
print(sq_num(5))

sq_num = lambda num : num **2
print(sq_num(5))

sum = lambda a,b : a+b
print(sum(2,4))

length = lambda b : len(b)
print(length("bhavani mohan"))

plus_10 = lambda b : 10+b
print(plus_10(35))

print_upper =lambda b : b.upper()
print(print_upper("nani"))


even_odd = lambda num : "even" if num % 2 == 0 else "odd"
print(even_odd(6))

max_of_two = lambda a,b: max(a,b)
print(max_of_two(4,7))

