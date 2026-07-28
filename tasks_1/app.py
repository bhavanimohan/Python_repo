a = "JavaScriptlsFun"
print(a[0:5])

a = "PythonRocks"
print(a[-3:])

a = "ProgramminglsCool"
print(a[2:10])

a = "ReverseMe"
print(a[::-1])

a = "TrimThis"
print(a[1:7])

a = "SliceMaster"
print(a[2:9])

a = "DivideAndConquer"
b = len(a)//2
print(a[0:b+1])

a = "HelloPython"
b = len(a)//2
# b = round(b)
print(a[b:])

a = "1234567890ABCDEF"
print(a[::3])

a = "OddLength"
b = len(a)//2
b = a[:b]+a[b+1:]
print(b)

a = "Backwards"
print(a[::-1])

a = "InclusiveSlicing"
print(a[2:9])

a = "PatternOddEven"
b = a.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
print(b)

a = "EvenOddPattern"
b = a[::2]
print(b)

a = "PatternOddEven"
c = len(a)
b = a[1:c:2]
print(b)

a = "NegativeIndexing"
print(a[-7:-2])

a = "ILovePythonProgramming"
print(a[5:11])

a = "SlicingReverse"
b = a[2:8]
print(b[::-1])

a = "RemoveLastFour"
print(a[:10])

a = "AlternateFromEnd"
print(a[::-2])

a = input("Enter your name: ")
b = input("Enter your age: ")
c = input("Enter your city: ")
print(f"Hello This is {a} and I am {b} years old and I live in {c}.")


a = input("Enter a first_name: ")
b = input("Enter a last_name: ")
print(a+" "+b)

a = input("Enter your name: ")
b = input("Enter your college: ")
c = input("Enter your course: ")
d = input("Enter your favorite_programming_language: ")
print(f"Hello, my name is {a}. I study at {b} and I am completed my studies in  {c}. My favorite programming language is {d}.")

a = input("Hello!!! I'm Nani. What is your name? ")
print("Hi Nani !!! My name is " + a + ".")
b = input("What is your favorite hobby? ")
print("My favorite hobby is " + b + ".")

a = input("Enter your first_name: ")
b= input("Enter your last_name: ")
print(a + b+"@gmail.com")