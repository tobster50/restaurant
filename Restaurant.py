from Order import *

class Restaurant:
    def __init__(self, restaurantName):
        self.restaurantName = restaurantName
        self.allOrders = {}
        self.orderNumber = 0

    def userInterface (self):
        print(f"Welcome to {self.restaurantName}!")
        order = Order()
        self.allOrders[self.orderNumber] = order
        self.orderNumber = self.orderNumber + 1
        order.newOrder()

