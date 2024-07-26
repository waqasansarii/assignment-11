#Problem 1:

#create class Item
#add instance properties
 # name, price, quantity
#create method calcualte_total_price
#create method apply_discount
#create method all_items

#all items have 20% discount by default

# use these items and store it in items.csv
#"Phone", 100, 1
#"Laptop", 1000, 3
#"Cable", 10, 5
#"Mouse", 50, 5
#"Keyboard", 75, 5

# read items.csv and create objects for each item
# I should be able to print all the items

    # Problem 2:
# extend the above application
# restrict updating the price directly i.e item.price = 100

import csv 
import os

class Item:
    discount = 0.2
    items = []
    def __init__(self,name,price,quantity) -> None:
        self.name = name 
        self.__price = price 
        self.quantity = quantity  
        # self.save_items() 
        self.items.append({"name":name,"price":price,"quantity":quantity}) 
        
    # def save_items(self):
    #     if not os.path.exists('./data'):
    #         os.makedirs('./data')   
    #     with open('./data/items.csv', 'a', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow([self.name, self.price, self.quantity])
    
    def price(self):
        return self.__price
        
    def calculate_price (self):
        return self.__price * self.quantity
    
    def apply_discount(self):
        discount_price = self.__price * Item.discount 
        self.__price = self.__price - discount_price
    
    @classmethod
    def all_items(cls):
        return cls.items
    
    @classmethod
    def read_item_csv(cls):
        with open('./data/items.csv','r') as file:
            print(file.read())

item = Item('Phone',100,1)
item2 = Item('Laptop',1000,3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
# print(item.items)
item.calculate_price()
item2.apply_discount()
Item.all_items()
Item.read_item_csv()
# print(item.__price)