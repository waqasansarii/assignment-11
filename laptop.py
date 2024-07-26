#Problem 3:

# extend the above application
# There are extra attributes in laptop i.e gpu, port_count and also it has 30% discount

# application folder structure
#1. items.py
#2. laptop.py
#3. data/items.csv


from main import Item

class Laptop(Item):
    discount = 0.3
    def __init__(self, name, price, quantity,gpu,port_count):
        super().__init__(name, price, quantity)
        self.gpu = gpu
        self.port_count = port_count
        self.items.append({"name":name,"price":price,"quantity":quantity,"gpu":gpu,"port_count":port_count})
    
    def apply_discount(self):
            discount_price = self.price * Laptop.discount 
            self.set_price(self.price - discount_price)
            
            
laptop = Laptop('laptop',54000,4,4.5,11)
print(Laptop.items) 
# laptop.apply_discount()  
print(laptop.price) 
        