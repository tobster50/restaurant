import json

class Order:
    def __init__(self):
        self.orderCost = 0
        self.itemNumber = 0
        self.currentOrderFood = {}
        self.currentOrderDrink = {}

    def foodMenu(self):
        foodMenu = {
            "item1" : {
                    "1" : "Roast Duck",
                    "Price" : "£15"
            },
            "item2" : {
                    "2" : "Braised Squid",
                    "Price" : "£10"
            },
            "item3" : {
                    "3" : "Pork Confit",
                    "Price" : "£20"
            },
            "item4" : {
                    "4" : "Fillet Steak",
                    "Price" : "£40"
            },                
        }
        for itemNum, itemInfo in foodMenu.items():
            for key in itemInfo:
                print(key + ':', itemInfo[key])

        session = 0
        while session == 0:
            print("\nWhat would you like to order? (1-4)")
            choice = input("To stop ordering input 0 : ")
            choice = int(choice)
            if choice == 1:
                print("You ordered 1 Roast Duck")
                self.orderCost = self.orderCost + 15
                self.currentOrderFood[self.itemNumber] = foodMenu["item1"]["1"]
                self.currentOrderFood[self.itemNumber] = foodMenu["item1"]["Price"]
                self.itemNumber = self.itemNumber + 1
            elif choice == 2:
                print("You ordered 1 Braised Squid")
                self.orderCost = self.orderCost + 10
                self.currentOrderFood[self.itemNumber] = foodMenu["item2"]["2"]
                self.currentOrderFood[self.itemNumber] = foodMenu["item2"]["Price"]
                self.itemNumber = self.itemNumber + 1
            elif choice == 3:
                self.orderCost = self.orderCost + 20
                self.currentOrderFood[self.itemNumber] = foodMenu["item3"]["3"]
                self.currentOrderFood[self.itemNumber] = foodMenu["item3"]["Price"]
                self.itemNumber = self.itemNumber + 1
            elif choice == 4:
                print("You ordered 1 Fillet Steak")
                self.orderCost = self.orderCost + 40
                self.currentOrderFood[self.itemNumber] = foodMenu["item4"]["4"]
                self.currentOrderFood[self.itemNumber] = foodMenu["item4"]["Price"]
                self.itemNumber = self.itemNumber + 1
            elif choice == 0:
                session = 1
            else:
                print("Invalid selection. Try again")       

    def drinksMenu(self):
        drinkMenu = {
            "item1" : {
                    "1" : "Beer",
                    "Price" : "£5"
            },
            "item2" : {
                    "2" : "IPA",
                    "Price" : "£6"
            },
            "item3" : {
                    "3" : "Red Wine",
                    "Price" : "£15"
            },
            "item4" : {
                    "4" : "Coke",
                    "Price" : "£3"
            },                
        }
        for itemNum, itemInfo in drinkMenu.items():
            for key in itemInfo:
                print(key + ':', itemInfo[key])
        
        session = 0
        while session == 0:
            print("\nWhat would you like to order? (1-4)")
            choice = input("To stop ordering input 0 : ")
            choice = int(choice)
            if choice == 1:
                print("You ordered 1 Beer")
                self.orderCost = self.orderCost + 5
                self.currentOrderDrink[self.itemNumber] = drinkMenu["item1"]["1"]
                self.currentOrderDrink[self.itemNumber] = drinkMenu["item1"]["Price"]
                self.itemNumber = self.itemNumber + 1
            elif choice == 2:
                print("You ordered 1 IPA")
                self.orderCost = self.orderCost + 6
                self.currentOrderDrink[self.itemNumber] = drinkMenu["item2"]["2"]
                self.currentOrderDrink[self.itemNumber] = drinkMenu["item2"]["Price"]
                self.itemNumber = self.itemNumber + 1
            elif choice == 3:
                print("You ordered 1 Red Wine")
                self.orderCost = self.orderCost + 15
                self.currentOrderDrink[self.itemNumber] = drinkMenu["item3"]["3"]
                self.currentOrderDrink[self.itemNumber] = drinkMenu["item3"]["Price"]
                self.itemNumber = self.itemNumber + 1
            elif choice == 4:
                print("You ordered 1 Coke")
                self.orderCost = self.orderCost + 3
                self.currentOrderDrink[self.itemNumber] = drinkMenu["item4"]["4"]
                self.currentOrderDrink[self.itemNumber] = drinkMenu["item4"]["Price"]
                self.itemNumber = self.itemNumber + 1
            elif choice == 0:
                session = 1
            else:
                print("Invalid selection. Try again")

    def newOrder(self):
        session = 0
        while session == 0:
            print("\nHow can I help you today?")
            print(f"Your current total cost is: £{self.orderCost}")
            print("1. Order Food")
            print("2. Order Drink")
            print("3. Get receipt")
            choice = input("Make your choice 1-2: ")
            choice = int(choice)
            if choice == 1:
                print("Would you like to view our food menu?")
                self.foodMenu()
            elif choice == 2:
                print("Would you like to view our drinks menu?")
                self.drinksMenu()
            elif choice == 3:
                choice = input("Would you like the bill? 1-2")
                choice = int(choice)
                if choice == 1:
                    self.getReceipt()
                    self.itemNumber = 0
                else:
                    pass
            else:
                print("Please try again")

    def getReceipt(self):
        food = json.dumps(self.currentOrderFood)
        drink = json.dumps(self.currentOrderDrink)
        with open ('receipt.txt', 'w') as receipt:
            receipt.writelines(f'You have ordered the following:')
            receipt.writelines('\nFood:')
            receipt.writelines(f'\n{food}')
            receipt.writelines('\nDrink:')
            receipt.writelines(f'\n{drink}')
            receipt.writelines(f'\nTotal Order Cost comes to: £{self.orderCost}')
            receipt.writelines('\nHave a nice day!')




