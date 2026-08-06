num=int(input("enter the number : "))
if num % 2==0:
    print("even")
else:
    print("odd")

num = int(input("Enter a number: "))
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
num = int(input("Enter a number: "))
 
if num <= 9:
    print("One-digit number")
elif num <= 99:
    print("Two-digit number")
elif num <= 999:
    print("Three-digit number")
else:
    print("More than three-digit number")

num = int(input("Enter a number: "))

if num == 1000:
    print("It is the smallest 4-digit number")
else:
    print("It is not the smallest 4-digit number")
ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print("Uppercase Letter")
elif 'a' <= ch <= 'z':
    print("Lowercase Letter")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Special Character")
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")

num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Maximum =", a)
elif b >= a and b >= c:
    print("Maximum =", b)
else:
    print("Maximum =", c)

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
if a + b > c:
    if c * c == a * a + b * b:
        print("Right-angled Triangle")
    elif c * c < a * a + b * b:
        print("Acute-angled Triangle")
    else:
        print("Obtuse-angled Triangle")
else:
    print("Not a valid Triangle")

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid Triangle")
    
