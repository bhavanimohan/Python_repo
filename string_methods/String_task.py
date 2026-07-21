# Task 2 -- STRING METHODS 


# Question No 1
text = " PyThOn PrOgRaMmInG Is AwEsOmE "
result = (
 text.strip()
 .swapcase()
 .replace("aWeSoMe", "Fantastic")
 .title()
 .split()
)

output = (
 result[0].upper()
 + "-"
 + result[1][:4].lower()
 + "-"
 + str(text.lower().count("o"))
 + "-"
 + result[-1][::-1]
)

print(output)


# Question 2
text = " JaVaScRiPt Is VeRy PoWeRfUl "
words = (
 text.strip()
 .swapcase()
 .replace("vErY", "Super")
 .title()
 .split()
)

output = (
 words[0][::-1]
 + "-"
 + words[2].upper()
 + "-"
 + str(len(text.strip()))
 + "-"
 + words[-1][:5].lower()
)
print(output)

# Question 3
text = " DaTa ScIeNcE WiTh PyThOn "
parts = (
 text.strip()
 .title()
 .replace("With", "Using")
 .split()
)
output = (
 parts[1].swapcase()
 + "-"
 + parts[2].upper()
 + "-"
 + str(text.lower().count("t"))
 + "-"
 + parts[-1][::-1]
)
print(output)

# Question 4

msg = " LeArNiNg CoDiNg Is FuN "
items = (
 msg.strip()
 .swapcase()
 .replace("fUn", "Awesome")
 .title()
 .split()
)
output = (
 items[0][:4]
 + "-"
 + items[1].lower()
 + "-"
 + str(msg.find("Co"))
 + "-"
 + items[-1].upper()
)
print(output)

# Question 5
text = " MaChInE LeArNiNg Is ThE FuTuRe "
words = (
 text.strip()
 .title()
 .replace("Future", "Tomorrow")
 .split()
)
output = (
 words[0].lower()
 + "-"
 + words[1][::2]
 + "-"
 + str(text.lower().count("e"))
 + "-"
 + words[-1].swapcase()
)
print(output)


# Q6: " pYtHoN Is AwEsOmE " -> Python_is_Awesome
# Rules: strip(), title(), replace(" ","_")

text = " pYtHoN Is AwEsOmE "
result = text.strip().title().replace(" ", "_").replace("Is", "is")
print(result)

# Q7: " javaScript programming language " -> JAVASCRIPT-PROGRAMMING-LANGUAGE
# Rules: strip(), upper(), replace(" ","-")
text = " javaScript programming language "
result = text.strip().upper().replace(' ', "-")
print(result)


# Q8: " welcome TO python FULL stack " -> Welcome to Python Full Stack
# Rules: strip(), title(), replace("To","to")

text = " welcome TO python FULL stack "
result = text.strip().title().replace("To", "to")
print(result)


# Q9: " Learn Python In 30 Days " -> days_30_in_python_learn
# Rules: strip(), lower(), split(), reverse words, join("_")

text = " Learn Python In 30 Days "
result = "_".join(text.strip().lower().split()[::-1])
print(result)

# Q10: " Data Science With Python " -> PYTHON->WITH->SCIENCE->DATA
# Rules: strip(), upper(), split(), reverse words, join("->")

text = " Data Science With Python "
result = "->".join(text.strip().upper().split()[::-1])
print(result)


# BONUS 
text = " PyThOn PrOgRaMmInG LaNgUaGe "
# Target: language_programming_python
# Use at least: strip(), swapcase(), title(), replace(), split(), lower(), slicing, join()

result = "_".join(text.strip().lower().split()[::-1])
print(result)