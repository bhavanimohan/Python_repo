# print("Start")
# def outer():
#     print("This is the outer function")
#     def inner():
#         print("This is the inner function")
#     print("end-of outer function")
    
#     return inner

# inner_function= outer()   
# inner_function()     
# print("End")


# a = 10
# b = 20
# def fruits():
#     print(a)
#     print(b)
#     print(30)
#     print(40)
# fruits()

# print(a)
# print(b)

# print("START")

# a = 10
# def outer():
#     b = 20
#     def inner():
#         c = 30
#         print(a,b,c)
#     inner()
# outer()
# print(a)

# print("END")


# a = 10 #---> global scope --------------------------|
# def outer():                                       #| ----------->enclosing scope 
#     b = 20  #---> non-local scope ------------------|
    
    
#     def inner():
#         c = 30 #---> local scope 
#         print(a,b,c)
#     inner()
# outer()
# print(a)

# print("END")

# a = 10
# def outer():
#     global a
#     a = 20
#     def inner():
        
#         print(a)
#     inner()
# outer()
# print(a)

# print("END")


# def outer():
#     a = 10

#     def inner():
#         nonlocal a
#         a = 40
#         print(a)
#     inner()
# outer()
# print(a)

# print("END")

# x = 10
# def show():
#     print(x)
# show()

# x = 10
# def show():
#     x = 20
#     print(x)
# show()
# print(x)

# x = 10
# def change():
#     global x
#     x = 20
# change()
# print(x)

# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#     inner()
#     inner()
# outer()

# def outer():
#     msg = "hello"
#     def inner():
#         print(msg)
#     inner()
# outer()

# def outer():
#     x = "outer"
#     def middle():
#         nonlocal x
#         x = "middle"
#         def inner():
#             print(x)
#         inner()
#     middle()
#     print(x)
# outer()

# x = "global"
# def outer():
#     def inner():
#         global x
#         x = "changed"
#     inner()
#     print(x)
# outer()
# print(x)

# x = "global"
# def outer():
#     x = "outer"
#     def inner():
#         nonlocal x
#         x = "inner"
#     def change_global():
#         global x
#         x = "global-changed"
#     inner()
#     change_global()
#     print(x)
# outer()
# print(x)

# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter
# c1 = make_counter()
# print(c1())
# print(c1())
# print(c1())


# def make_counter(start):
#     count = start
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter
# c1 = make_counter(0)
# c2 = make_counter(100)
# print(c1())
# print(c2())
# print(c1())
# print(c2())

# def total_marks(student, *scores): 
#     print("Student:", student) 
#     print("Scores:", scores) 
#     print("Total:", sum(scores))

# marks = (85, 90, 78) 
# total_marks("Ravi", *marks) 
# total_marks("Meena", 60, 70)

# def add_item(item, cart=[]): 
#     cart.append(item) 
#     print(cart)

# add_item("apple") 
# add_item("banana")
# add_item("mango", [])


# def book_ticket(name, *, seat="Any", meal=None): 
#     print("Passenger:", name)
#     print("Seat:", seat)
#     print("Meal:", meal)

# book_ticket("Arjun", seat="12A") 
# book_ticket("Divya", meal="Veg", seat="4C")

# def calc_price(item, price, discount=10, tax=5): 
#     final = price - (price * discount / 100)
#     final = final + (final * tax / 100) 
#     print(f"{item}: {final}")

# calc_price("Book", 200)
# calc_price("Pen", 100, discount=0)
# calc_price("Bag", 500, 20, 0)

# def build_profile(*tags, **info):
#     print("Tags:", tags)
#     for key, value in info.items():
#         print(f"{key} -> {value}") 
#     return len(tags) + len(info)

# result = build_profile("admin", "verified", name="Zara", age=25) 
# print("Total fields:", result)


# count=int(input("Enter the number : "))

# for char in range(1,11):
#     print(f"{count} * {char} = {char*count}")
    