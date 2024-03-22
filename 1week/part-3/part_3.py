my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_book_shelf = [
    {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year": 1960,
    "rating": 4.27,
    "pages": 324
},{
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "rating": 4.17,
    "pages": 328
},{
    "title": "Harry Potter and the Sorcerer's Stone",
    "author": "J.K. Rowling",
    "year": 1997,
    "rating": 4.47,
    "pages": 309
},{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "rating": 3.91,
    "pages": 180
},{
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "year": 1813,
    "rating": 4.25,
    "pages": 279
}
]


# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def describe_book(book):
    title = book["title"]
    author = book["author"]
    year = book["year"]
    rating = book["rating"]
    pages = book["pages"]

    script = f"This book is called {title} written by {author} and published in the year {year}. With an average rating of {rating}, this book has a total length of {pages} pages."

    return script

print(describe_book(my_book))



# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def show_authors(book):
    author = book["author"]
    return author

def list_publish_date(book):
    year = book["year"]
    return year

def show_title(book):
    title = book["title"]
    return title

def show_rating(book):
    rating = book["rating"]
    return rating

def show_page_count(book):
    pages = book["pages"]
    return pages






# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def show_longest_book(shelf):
    largestBook = 0
    bookTitle = ""
    for book in shelf:
        title = show_title(book)
        pages = show_page_count(book)
        if pages > largestBook:
            largestBook = pages
            bookTitle = title
        else: continue
    return print(f"{bookTitle} is the largest book with {largestBook} pages.")
        
def show_oldest_book(shelf):
    oldestBook = 2300
    bookTitle = ""
    for book in shelf:
        title = show_title(book)
        year = list_publish_date(book)
        if year < oldestBook:
            oldestBook = year
            bookTitle = title
        else: continue
    return print(f"{bookTitle} is the oldest book published in the year {oldestBook}.")

def top_rated_book(shelf):
    topRating = 0
    bookTitle = ""
    for book in shelf:
        title = show_title(book)
        rating = show_rating(book)
        if rating > topRating:
            topRating = rating
            bookTitle = title
    return print(f"{bookTitle} is the top rated book at a rating of {topRating}.")
        

def describe_all_books(shelf):
    printer = []
    for book in shelf:
        printer.append(describe_book(book))
        print(describe_book(book))
    return print(printer)





