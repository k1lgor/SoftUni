from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.book_available = {}
        self.rented_books = {}
