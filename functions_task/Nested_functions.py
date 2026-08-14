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


a = 10
b = 20
def fruits():
    print(a)
    print(b)
    print(30)
    print(40)
fruits()

print(a)
print(b)

print("START")

a = 10
def outer():
    b = 20
    def inner():
        c = 30
        print(a,b,c)
    inner()
outer()
print(a)

print("END")


a = 10 #---> global scope --------------------------|
def outer():                                       #| ----------->enclosing scope 
    b = 20  #---> non-local scope ------------------|
    
    
    def inner():
        c = 30 #---> local scope 
        print(a,b,c)
    inner()
outer()
print(a)

print("END")

a = 10
def outer():
    global a
    a = 20
    def inner():
        
        print(a)
    inner()
outer()
print(a)

print("END")


def outer():
    a = 10

    def inner():
        nonlocal a
        a = 40
        print(a)
    inner()
outer()
print(a)

print("END")