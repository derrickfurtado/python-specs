my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_book_list = [
    {
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "year": 2008,
        "rating": 4.32,
        "pages": 374
    },
    {
        "title": "Catching Fire",
        "author": "Suzanne Collins",
        "year": 2009,
        "rating": 4.3,
        "pages": 391
    },
    {
        "title": "Mockingjay",
        "author": "Suzanne Collins",
        "year": 2010,
        "rating": 4.06,
        "pages": 398
    }
]

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_parser(book_dictionary):

    book_string = f"This book's name is {book_dictionary['title']}, and was written by {book_dictionary['author']}. It was published in the year {book_dictionary['year']} and currently holds a rating of {book_dictionary['rating']}. The length of the book is {book_dictionary['pages']} pages."

    return book_string

print(book_parser(my_book))


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def get_book_title(book_dictionary):
    book_title = book_dictionary["title"]
    return book_title

def get_book_author(book_dictionary):
    book_author = book_dictionary["author"]
    return book_author

def get_book_year(book_dictionary):
    book_year = book_dictionary["year"]
    return book_year

def get_book_rating(book_dictionary):
    book_rating = book_dictionary["rating"]
    return book_rating

def get_book_pages(book_dictionary):
    book_pages = book_dictionary["pages"]
    return book_pages

print(get_book_title(my_book))
print(get_book_author(my_book))
print(get_book_year(my_book))
print(get_book_rating(my_book))
print(get_book_year(my_book))


# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def book_parser_from_list(book_dictionary_list):
    for book_dictionary in book_dictionary_list:
        print(book_parser(book_dictionary))


def get_set_of_authors(book_dictionary_list):
    author_set = set()

    for book_dictionary in book_dictionary_list:
        author_set.add(book_dictionary["author"])

    return author_set

def get_total_pages(book_dictionary_list):
    total_pages = 0

    for book_dictionary in book_dictionary_list:
        total_pages += book_dictionary["pages"]

    return total_pages

book_parser_from_list(my_book_list)
print(get_set_of_authors(my_book_list))
print(get_total_pages(my_book_list))