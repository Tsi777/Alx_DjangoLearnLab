# Delete Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verify deletion
remaining_books = Book.objects.all()
print(f"Remaining books: {list(remaining_books)}")