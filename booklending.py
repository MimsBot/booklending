from random import choice
from datetime import datetime


class Book:

    on_shelf = []
    on_loan = []

    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    @classmethod
    def create(cls, title, author, ISBN):
        new_book = Book(title, author, ISBN)
        cls.on_shelf.append(new_book)
        return new_book

    @classmethod
    def browse(cls):
        book = choice(cls.on_shelf)
        return book

    def lent_out(self):
        return self in Book.on_loan

    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14   # two weeks expressed in seconds
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

    def borrow(self):
        if self.lent_out():
            return False
        else:
            self.due_date = Book.current_due_date()
            Book.on_shelf.remove(self)
            Book.on_loan.append(self)
            return True

    def return_to_library(self):
        if not self.lent_out():
            return False
        else:
            Book.on_loan.remove(self)
            Book.on_shelf.append(self)
            self.due_date = None
            return True

    @classmethod
    def overdue(cls):
        overdue_books = []
        for num in range(0, len(Book.on_loan)):
            current_book = Book.on_loan[num]
            if current_book.due_date < datetime.now():
                overdue_books.append(current_book)
            return overdue_books



sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
print(Book.browse().title)   # "Sister Outsider" (this value may be different for you)
print(Book.browse().title)   # "Ain't I a Woman?" (this value may be different for you)
print(len(Book.on_shelf))   # 3
print(len(Book.on_loan))   # 0
print(sister_outsider.lent_out())   # False
print(sister_outsider.borrow())   # True
print(len(Book.on_shelf))   # 2
print(len(Book.on_loan))   # 1
print(sister_outsider.lent_out())   # True
print(sister_outsider.borrow())   # False
print(sister_outsider.due_date)    # 2017-02-25 20:52:20 -0500 (this value will be different for you)
print(len(Book.overdue()))   # 0
print(sister_outsider.return_to_library())   # True
print(sister_outsider.lent_out())    # False
print(len(Book.on_shelf))   # 2
print(len(Book.on_loan))   # 0
