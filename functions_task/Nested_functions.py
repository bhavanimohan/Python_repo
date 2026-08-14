print("Start")
def outer():
    print("This is the outer function")
    def inner():
        print("This is the inner function")
    print("end-of outer function")
    
    return inner

inner_function= outer()   
inner_function()     
print("End")