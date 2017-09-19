import unittest
from app.shopping_list_class import shoppingList
 
class TddShoppingList(unittest.TestCase):

    def setUp(self):
        self.myshoppingList = shoppingList()
 
    def test_shoppingList_addItem_correct_result(self):
        myshoppingList = shoppingList()
        myshoppingList.addItem("Orange", 5)
        myshoppingList.addItem("Pear", 10)
        result = myshoppingList.no_OfItems()
        self.assertEqual(2, result)
        
    def test_shoppingList_edit_Item_correctly(self):
        myshoppingList = shoppingList()
        myshoppingList.addItem("Mango", 5)
        myshoppingList.editItem("Mango", 10)        
        result = myshoppingList.quantityOfItems("Mango")
        self.assertEqual(10, result)




if __name__ == '__main__':
    unittest.main()
