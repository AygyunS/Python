import unittest
from project.toy_store import ToyStore


class TestToyStore(unittest.TestCase):

    def setUp(self):
        self.toy_store = ToyStore()

    def test_add_toy_success(self):
        result = self.toy_store.add_toy("A", "Car")
        self.assertEqual(result, "Toy:Car placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf["A"], "Car")

    def test_add_toy_shelf_not_exists(self):
        with self.assertRaises(Exception) as context:
            self.toy_store.add_toy("X", "Car")
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

    def test_add_toy_already_in_shelf(self):
        self.toy_store.add_toy("A", "Car")
        with self.assertRaises(Exception) as context:
            self.toy_store.add_toy("A", "Car")
        self.assertEqual(str(context.exception), "Toy is already in shelf!")

    def test_add_toy_shelf_already_taken(self):
        self.toy_store.add_toy("A", "Car")
        with self.assertRaises(Exception) as context:
            self.toy_store.add_toy("A", "Bike")
        self.assertEqual(str(context.exception), "Shelf is already taken!")

    def test_remove_toy_success(self):
        self.toy_store.add_toy("A", "Car")
        result = self.toy_store.remove_toy("A", "Car")
        self.assertEqual(result, "Remove toy:Car successfully!")
        self.assertIsNone(self.toy_store.toy_shelf["A"])

    def test_remove_toy_shelf_not_exists(self):
        with self.assertRaises(Exception) as context:
            self.toy_store.remove_toy("X", "Car")
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

    def test_remove_toy_not_in_shelf(self):
        with self.assertRaises(Exception) as context:
            self.toy_store.remove_toy("A", "Car")
        self.assertEqual(str(context.exception), "Toy in that shelf doesn't exists!")

if __name__ == "__main__":
    unittest.main()
