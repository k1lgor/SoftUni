from unittest import TestCase, main

from project.library import Library


class LibraryTests(TestCase):
    def setUp(self) -> None:
        self.library = Library('main')

    def test_init(self):
        self.assertEqual('main', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_cannot_be_empty(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ''
        self.assertEqual('Name cannot be empty string!', str(ex.exception))

    def test_add_book_if_author_not_in_books_by_author(self):
        self.library.add_book('manqka', 'lek')
        self.assertEqual({'manqka': ['lek']}, self.library.books_by_authors)

    def test_add_reader_if_not_in_readers(self):
        self.library.add_reader('pesho')
        self.assertEqual([], self.library.readers['pesho'])
        self.assertEqual({'pesho': []}, self.library.readers)

    def test_add_reader_if_reader_in_readers(self):
        self.library.add_reader('pesho')
        result = self.library.add_reader('pesho')
        self.assertEqual(f"pesho is already registered in the {self.library.name} library.", result)

    def test_rent_book_if_reader_not_in_reader(self):
        result = self.library.rent_book('pesho', 'manqk', 'lek')
        self.assertEqual(f"pesho is not registered in the {self.library.name} Library.", result)

    def test_rent_book_if_author_is_not_in_authors(self):
        self.library.readers['pesho'] = []
        result = self.library.rent_book('pesho', 'manqk', 'lek')
        self.assertEqual(f"{self.library.name} Library does not have any manqk's books.", result)

    def test_rent_book_if_book_title_not_in_authors_titles(self):
        self.library.readers['pesho'] = []
        self.library.books_by_authors['manqk'] = 'lek'
        result = self.library.rent_book('pesho', 'manqk', 'lek2')
        self.assertEqual(f"""{self.library.name} Library does not have manqk's "lek2".""", result)

    def test_rent_book(self):
        reader_name = 'reader'
        author_name = 'author'
        first_title = 'title1'
        second_title = 'title2'
        self.library.add_reader(reader_name)
        self.library.add_book(author_name, first_title)
        self.library.add_book(author_name, second_title)

        self.library.rent_book(reader_name, author_name, first_title)

        self.assertEqual([{author_name: first_title}], self.library.readers[reader_name])
        self.assertEqual(1, len(self.library.books_by_authors[author_name]))
        self.assertTrue(first_title not in self.library.books_by_authors[author_name])
        self.assertTrue(second_title in self.library.books_by_authors[author_name])


if __name__ == '__main__':
    main()
