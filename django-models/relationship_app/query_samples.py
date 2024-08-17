from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    """
    try:
        # Instead of using get(), we retrieve all authors and then filter by name within Python
        authors = Author.objects.all()
        author = next((author for author in authors if author.name == author_name), None)
        if author:
            books = author.books.all()  # Using the related_name 'books' to access related books
            print(f"Books by {author_name}:")
            for book in books:
                print(f"- {book.title}")
        else:
            print(f"No author found with name {author_name}")
    except StopIteration:
        print(f"No author found with name {author_name}")

def list_books_in_library(library_name):
    """
    List all books in a library.
    """
    try:
        # Instead of using get(), we retrieve all libraries and then filter by name within Python
        libraries = Library.objects.all()
        library = next((lib for lib in libraries if lib.name == library_name), None)
        if library:
            books = library.books.all()  # Using the related_name 'books' to access related books
            print(f"Books in {library_name} library:")
            for book in books:
                print(f"- {book.title}")
        else:
            print(f"No library found with name {library_name}")
    except StopIteration:
        print(f"No library found with name {library_name}")

def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    """
    try:
        # Instead of using get(), we retrieve all libraries and then filter by name within Python
        libraries = Library.objects.all()
        library = next((lib for lib in libraries if lib.name == library_name), None)
        if library:
            librarian = getattr(library, 'librarian', None)
            if librarian:
                print(f"Librarian for {library_name} library: {librarian.name}")
            else:
                print(f"No librarian found for the {library_name} library")
        else:
            print(f"No library found with name {library_name}")
    except StopIteration:
        print(f"No library found with name {library_name}")

if __name__ == "__main__":
    # Example usage
    query_books_by_author('Author Name')
    list_books_in_library('Library Name')
    retrieve_librarian_for_library('Library Name')