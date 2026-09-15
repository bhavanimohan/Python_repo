# class Book:
#     def __init__(self,type,no_of_pages,brand,price):
#         self.type = type
#         self.no_of_pages = no_of_pages
#         self.brand = brand
#         self.price = price
#     def show_details(self):
#         print(f"""
#                 Book  Type: {self.type}, 
#                 No of Pages: {self.no_of_pages},
#                 Brand: {self.brand}, 
#                 Price: {self.price}
#                 """)
# b1 = Book("Plain", 100, "Camlin", 50)
# b2 = Book("Hard", 200, "Camlin", 100)
# b1.show_details()
# b2.show_details()


# class Person:
#     def __init__(self,name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def show_details(self):
#         print(f"""
#                 Name: {self.name}, 
#                 Age: {self.age},
#                 Gender: {self.gender}""")
        
# h1 = Person("John", 25, "Male")
# h1.show_details()
# print(dir(h1))

from xml.parsers.expat import model


class Phone:
    def __init__(self):
        self.brand = input("Enter brand: ")
        self.model = input("Enter model: ")
        self.price = float(input("Enter price: "))
    def show_details(self):
        print(f"""
                Brand: {self.brand}, 
                Model: {self.model},
                Price: {self.price}""")
    def call(self, number):
        print(f"Calling {number} from {self.brand} - {self.model}...")
    def send_message(self, number, message):
        print(f"Sending message to {number} from {self.brand} - {self.model} : {message}")
    def receive_message(self, number, message):
        print(f"Received message from {number} on {self.brand} - {self.model} : {message}")
    def take_photo(self):
        print(f"Taking photo with {self.brand} - {self.model}...")
    def play_music(self, song):
        print(f"Playing {song} on {self.brand} - {self.model}...")
    def play_games(self, game):
        print(f"Playing {game} on {self.brand} - {self.model}...")
    def play_video(self, video):
        print(f"Playing {video} on {self.brand} - {self.model}...")



p1 = Phone()
p2 = Phone()

p1.show_details()
p1.call("123-456-7890")
p1.send_message("123-456-7890", "Hello, how are you?")
p1.receive_message("123-456-7890", "I'm good, thanks for asking!")
p1.take_photo()
p1.play_music("Blinding Lights")
p1.play_games("Minecraft")
p1.play_video("Python Tutorial")
p2.show_details()