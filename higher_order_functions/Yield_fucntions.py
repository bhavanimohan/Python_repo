def funct_even():
    for char in range(1,5001):
        if char % 2 == 0:
            
            yield char
            
       
            
res = funct_even()   

print(next(res))
print(next(res))
print(next(res))