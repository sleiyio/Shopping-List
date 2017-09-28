import unittest
from app.shopping_list import shoppingList
 
class TddShoppingList(unittest.TestCase):

    def setUp(self):
        self.myshoppingList = shoppingList()
 
    def test_shoppingList_addItem_correct_result(self):
           
        self.myshoppingList.addItem("Orange", 5)
        self.myshoppingList.addItem("Pear", 10)
        result = self.myshoppingList.no_OfItems()
        self.assertEqual(2, result)
    
    def test_shoppingList_removeItem_correct_result(self): 
              
        self.myshoppingList.addItem("Orange", 5)
        self.myshoppingList.addItem("Pear", 10)
        self.myshoppingList.addItem("Mango", 2)
        self.myshoppingList.removeItem("Pear")
        result = self.myshoppingList.no_OfItems()
        self.assertEqual(2, result)
        
    def test_shoppingList_edit_Item_correctly(self):        
        self.myshoppingList.addItem("Mango", 5)
        self.myshoppingList.editItem("Mango", 10)        
        result = self.myshoppingList.quantityOfItems("Mango")
        self.assertEqual(10, result)

if __name__ == '__main__':
    unittest.main()
