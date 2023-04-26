from project.bookstore import Bookstore
import unittest



class TestBookstore(unittest.TestCase):

    def test_books_limit(self):
        bookstore = Bookstore(5)
        self.assertEqual(bookstore.books_limit, 5)

        with self.assertRaises(ValueError):
            bookstore.books_limit = -1

    def test_total_sold_books(self):
        bookstore = Bookstore(5)
        self.assertEqual(bookstore.total_sold_books, 0)

    def test_receive_book(self):
        bookstore = Bookstore(5)
        msg = bookstore.receive_book("Book A", 3)
        self.assertEqual(msg, "3 copies of Book A are available in the bookstore.")
        self.assertEqual(len(bookstore), 3)

        msg = bookstore.receive_book("Book B", 2)
        self.assertEqual(msg, "2 copies of Book B are available in the bookstore.")
        self.assertEqual(len(bookstore), 5)

        with self.assertRaises(Exception):
            bookstore.receive_book("Book C", 1)

    def test_sell_book(self):
        bookstore = Bookstore(5)
        bookstore.receive_book("Book A", 3)

        with self.assertRaises(Exception):
            bookstore.sell_book("Book B", 1)

        with self.assertRaises(Exception):
            bookstore.sell_book("Book A", 4)

        msg = bookstore.sell_book("Book A", 2)
        self.assertEqual(msg, "Sold 2 copies of Book A")
        self.assertEqual(bookstore.total_sold_books, 2)
        self.assertEqual(bookstore.availability_in_store_by_book_titles["Book A"], 1)

    def test_str_representation(self):
        bookstore = Bookstore(5)
        bookstore.receive_book("Book A", 3)
        bookstore.receive_book("Book B", 2)

        expected_output = (
            "Total sold books: 0\n"
            "Current availability: 5\n"
            " - Book A: 3 copies\n"
            " - Book B: 2 copies"
        )
        self.assertEqual(str(bookstore), expected_output)

        bookstore.sell_book("Book A", 2)

        expected_output_after_sell = (
            "Total sold books: 2\n"
            "Current availability: 3\n"
            " - Book A: 1 copies\n"
            " - Book B: 2 copies"
        )
        self.assertEqual(str(bookstore), expected_output_after_sell)


if __name__ == '__main__':
    unittest.main()
