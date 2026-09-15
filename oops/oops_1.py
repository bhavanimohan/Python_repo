class Book:
    def __init__(self,type,no_of_pages,brand,price):
        self.type = type
        self.no_of_pages = no_of_pages
        self.brand = brand
        self.price = price
    def show_details(self):
        print(f"""
                Book  Type: {self.type}, 
                No of Pages: {self.no_of_pages},
                Brand: {self.brand}, 
                Price: {self.price}
                """)
b1 = Book("Plain", 100, "Camlin", 50)
b2 = Book("Hard", 200, "Camlin", 100)
b1.show_details()
b2.show_details()
