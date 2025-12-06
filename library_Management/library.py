# =========================

# Library Management System (OOP)

# =========================

class Book:
    def __init__(self,title,author,isbn,copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = copies
        self.available_copies = copies
        
    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Available: {self.available_copies}/{self.total_copies}"
    
class Member:
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.max_books = 3
        
    def __str__(self):
      return f"{self.name} (ID: {self.member_id}) | Borrowed: {len(self.borrowed_books)}"
    
class Library:
    def __init__(self):
       self.books = {}
       self.members = {}
       
    # ---------------------
    
    #  BOOK METHODS
    
    # ----------------------
    
    def add_book(self, title, author, isbn, copies):
        if isbn in self.books:
            self.books[isbn].total_copies += copies
            self.books[isbn].available_copies += copies
            print("Book copies updated successfully")
        else:
            self.books[isbn] = Book(title, author, isbn, copies)
            print("Book added successfully .")
            
    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print("Book removed.")
        else:
            print("Book not found. ")
            
    # ----------------------
    
    # MEMBER METHODS
    
    # ------------------------
     
    def register_member(self, name, member_id):
        if member_id in self.members:
            print("Member already exists. ")
        else:
            self.members[member_id] = Member(name, member_id)
            print("Member registered successfully")
            

# ------------------------------

# ISSUE / RETURN METHODS

# ------------------------------

    def issue_book(self, member_id, isbn):
        if member_id not in self.members:
            print("member not found")
            return
        
        if isbn not in self.books:
            print("Book not found.")
            return
    
        member = self.members[member_id]
        book = self.books[isbn]
        
        if len(member.borrowed_books) >= member.max_books:
            print("Borrow limit exceed")
            return
        if book.available_copies <= 0:
            print("No copies available")
            return
        
        member.borrowed_books.append(isbn)
        book.available_copies -= 1
        print(f"Book issued to {member.name}")
        
    
    def return_book(self,member_id,isbn):
        if member_id not in self.members:
            print("Member not found")
            return
        
        if isbn not in self.books:
            print("Book not found")
            return
        
        member = self.members[member_id]
        book = self.books[isbn]
        
        if isbn not in member.borrowed_books:
            print("This member did not borrow this book")
            return
        
        member.borrowed_books.remove(isbn)
        book.available_copies += 1
        print("Book returned successfully")
        
# -----------------------

# SEARCH FUNCTIONS

# ---------------------------

    def search_by_title(self,title):
        for book in self.books.values():
            if title.lower() in book.title.lower():
                print(book)
    def search_by_author(self,author):
        for book in self.books.values():
            if author.lower() in book.author.lower():
                print(book)
                
    def search_by_isbn(self, isbn):
        if isbn in self.books:
            print(self.books[isbn])
        else:
            print("Book not found.")
        
# -----------------------

# Display FUNCTIONS

#-------------------------

    def show_all_books(self):
        if not self.books:
            print("No books available")
        for b in self.books.values():
            print(b)
            
    def show_all_members(self):
        if not self.members:
            print("No members registered")
        for m in self.members.values():
            print(m)
            
# ==============================

# MAIN MENU

# ==================================

def menu():
    library = Library()
    
    while True:
        print("\n==== Library Management System ====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book by Title")
        print("6. search book by Author")
        print("7. Search book by ISBN")
        print("8. Show All Books")
        print("9. Show All Members")
        print("10. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            title = input("Book Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            copies = int(input("Copies: "))
            library.add_book(title,author,isbn,copies)
            
        elif choice == "2":
            name = input("Member Name: ")
            member_id = input("Member ID: ")
            library.register_member(name,member_id)
            
        elif choice == "3":
            member_id = input("Member ID: ")
            isbn = input("ISBN: ")
            library.issue_book(member_id, isbn)
            
        elif choice == "4":
            member_id = input("Member ID: ")
            isbn = input("ISBN: ")
            library.return_book(member_id,isbn)
            
        elif choice == "5":
            title = input("Enter title keyword: ")
            library.search_by_title(title)

        elif choice == "6":
            author = input("Enter author keyword: ")
            library.search_by_author(author)

        elif choice == "7":
            isbn = input("Enter ISBN: ")
            library.search_by_isbn(isbn)

        elif choice == "8":
            library.show_all_books()

        elif choice == "9":
            library.show_all_members()

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Invalid option!")
            
menu() # run function
            
            
            