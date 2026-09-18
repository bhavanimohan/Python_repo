class Phone():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")
    def call(self, number):
        print(f"Calling {number} from {self.brand} - {self.model}...")
    def send_message(self, number, message):
        print(f"Sending message to {number} from {self.brand} - {self.model}: {message}")   
    def receive_message(self, number, message):
        print(f"Received message from {number} on {self.brand} - {self.model}: {message}")
class Smartphone(Phone):
    def __init__(self, brand, model, price, os):
        Phone.__init__(self, brand, model, price)
        self.os = os

    def display_info(self):
        Phone.display_info(self)
        print(f"Operating System: {self.os}")

    def take_photo(self):
        print(f"Taking photo with {self.brand} - {self.model}...")

    def play_music(self, song):
        print(f"Playing {song} on {self.brand} - {self.model}...")

    def play_games(self, game):
        print(f"Playing {game} on {self.brand} - {self.model}...")

    def play_video(self, video):
        print(f"Playing {video} on {self.brand} - {self.model}...")
        
res = Smartphone("Samsung", "Galaxy S21", 799, "Android")
res2 = Smartphone("Apple", "iPhone 13", 999, "iOS")
res.display_info()
res.call("123-456-7890")
res.send_message("123-456-7890", "Hello, how are you?")
res.receive_message("123-456-7890", "I'm doing great, thanks for asking!")
res.take_photo()
res.play_music("Blinding Lights")
res.play_games("Minecraft")
res.play_video("Python Tutorial")

res2.display_info()
