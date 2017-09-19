class shoppingList(object):
    def __init__(self, userId = 1, numberOfItems = 0, items = {}, totalCost = 0):
        self.userId = userId
        self.numberOfItems = 0
        self.items = {}
        self.totalCost = totalCost

    def addItem(self, item, quantity):
        #Add new item to shopping list
        self.items[item] = quantity
        self.numberOfItems = self.numberOfItems + 1

    def removeItem(self, item):
        #Delete an item from the shopping list
        del(self.items[item])
        self.numberOfItems = self.numberOfItems - 1

    def editItem(self, item, quantity):
        #Edit quantity of items on shopping list
        self.items[item] = quantity

    def ViewShoppingList(self):
        #View the whole shopping list
        return self.items

    def no_OfItems(self):
        return self.numberOfItems

    def quantityOfItems(self, item):
        return self.items[item]

    


    