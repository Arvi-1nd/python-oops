import unittest
from library import   Book, Member, Library # adjust import based on your file n


class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        """Create a fresh library before every test."""
        self.lib = Library()
        self.lib.add_book("Python Basics", "Guido", "111", 3)
        self.lib.register_member("Alice", "M001")

    # -------------------------
    # BOOK TESTS
    # -------------------------

    def test_add_book(self):
        self.lib.add_book("Django Guide", "Adrian", "222", 2)
        self.assertIn("222", self.lib.books)
        self.assertEqual(self.lib.books["222"].total_copies, 2)

    def test_add_existing_book_updates_copies(self):
        self.lib.add_book("Python Basics", "Guido", "111", 2)
        self.assertEqual(self.lib.books["111"].total_copies, 5)
        self.assertEqual(self.lib.books["111"].available_copies, 5)

    # -------------------------
    # MEMBER TESTS
    # -------------------------

    def test_register_member(self):
        self.lib.register_member("Bob", "M002")
        self.assertIn("M002", self.lib.members)

    # -------------------------
    # ISSUE BOOK TESTS
    # -------------------------

    def test_issue_book_success(self):
        self.lib.issue_book("M001", "111")
        member = self.lib.members["M001"]
        book = self.lib.books["111"]

        self.assertIn("111", member.borrowed_books)
        self.assertEqual(book.available_copies, 2)

    def test_issue_book_no_member(self):
        # Issue to unknown member
        self.lib.issue_book("INVALID", "111")
        # Should not reduce copy count
        self.assertEqual(self.lib.books["111"].available_copies, 3)

    def test_issue_book_no_copies(self):
        # Issue 3 times (all copies)
        self.lib.issue_book("M001", "111")
        self.lib.issue_book("M001", "111")
        self.lib.issue_book("M001", "111")

        # Now no more copies
        self.lib.issue_book("M001", "111")
        self.assertEqual(self.lib.books["111"].available_copies, 0)

    # -------------------------
    # RETURN BOOK TESTS
    # -------------------------

    def test_return_book_success(self):
        self.lib.issue_book("M001", "111")
        self.lib.return_book("M001", "111")

        member = self.lib.members["M001"]
        book = self.lib.books["111"]

        self.assertNotIn("111", member.borrowed_books)
        self.assertEqual(book.available_copies, 3)

    def test_return_book_not_borrowed(self):
        # Return without issuing
        self.lib.return_book("M001", "111")
        book = self.lib.books["111"]

        # Copies should remain same
        self.assertEqual(book.available_copies, 3)

    # -------------------------
    # SEARCH TESTS
    # -------------------------

    def test_search_by_title(self):
        results = [b for b in self.lib.books.values() if "python" in b.title.lower()]
        self.assertGreater(len(results), 0)

    def test_search_by_author(self):
        results = [b for b in self.lib.books.values() if "guido" in b.author.lower()]
        self.assertGreater(len(results), 0)

    def test_search_by_isbn(self):
        self.assertIn("111", self.lib.books)


if __name__ == '__main__':
    unittest.main()
