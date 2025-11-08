"""
Sample queries demonstrating Django ORM relationships
"""

def get_books_by_author(author_name):
    """
    Query all books by a specific author
    """
    from .models import Author, Book
    
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # Using related_name 'books'
        return books
    except Author.DoesNotExist:
        return f"Author '{author_name}' not found"

def get_books_in_library(library_name):
    """
    List all books in a specific library
    """
    from .models import Library
    
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Using ManyToMany relationship
        return books
    except Library.DoesNotExist:
        return f"Library '{library_name}' not found"

def get_librarian_for_library(library_name):
    """
    Retrieve the librarian for a specific library
    """
    from .models import Library
    
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Using OneToOne relationship
        return librarian
    except Library.DoesNotExist:
        return f"Library '{library_name}' not found"
    except AttributeError:
        return f"No librarian assigned to '{library_name}'"

# Example usage and test data creation
def create_sample_data():
    """
    Create sample data to test the relationships
    """
    from .models import Author, Book, Library, Librarian
    
    # Create authors
    author1 = Author.objects.create(name="Chinua Achebe")
    author2 = Author.objects.create(name="Ngũgĩ wa Thiong'o")
    
    # Create books
    book1 = Book.objects.create(title="Things Fall Apart", author=author1)
    book2 = Book.objects.create(title="Arrow of God", author=author1)
    book3 = Book.objects.create(title="A Grain of Wheat", author=author2)
    
    # Create library
    library = Library.objects.create(name="African Literature Library")
    
    # Add books to library
    library.books.add(book1, book2, book3)
    
    # Create librarian
    librarian = Librarian.objects.create(name="Amina Juma", library=library)
    
    return author1, author2, library, librarian

if __name__ == "__main__":
    # Create sample data
    author1, author2, library, librarian = create_sample_data()
    
    # Test the queries
    print("=== Testing Relationship Queries ===")
    
    # Query 1: All books by a specific author
    print("\n1. Books by Chinua Achebe:")
    books_by_author = get_books_by_author("Chinua Achebe")
    for book in books_by_author:
        print(f"   - {book.title}")
    
    # Query 2: All books in a library
    print("\n2. Books in African Literature Library:")
    books_in_library = get_books_in_library("African Literature Library")
    for book in books_in_library:
        print(f"   - {book.title} by {book.author.name}")
    
    # Query 3: Librarian for a library
    print("\n3. Librarian for African Literature Library:")
    library_librarian = get_librarian_for_library("African Literature Library")
    print(f"   - {library_librarian.name}")