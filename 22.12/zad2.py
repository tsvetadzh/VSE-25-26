class Library:
    name = ""
    borrowed = []

    def borrow(self, book_name):
        self.borrowed.append(book_name)

    def returned(self, book_name):
        if book_name in self.borrowed:
            self.borrowed.remove(book_name)
        else:
            print("Wrong")
    
    def books(self):
        if self.borrowed:
            for book in self.borrowed:
                print(book)
        else:
            print("No")

ivan = Library()
ivan.name = "Ivan"
ivan.borrowed = []
ivan.borrow("Harry Potter")
ivan.borrow("Hamlet")
ivan.returned("Hamlet")
ivan.books()

