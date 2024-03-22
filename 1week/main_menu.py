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
def describe_book(book):
    title = book["title"]
    author = book["author"]
    year = book["year"]
    rating = book["rating"]
    pages = book["pages"]

    script = f"⭐️ {title} written by {author} and published in the year {year}. With an average rating of {rating}, this book has a total length of {pages} pages."

    return script

def show_longest_book(shelf):
    largestBook = 0
    bookTitle = ""
    for book in shelf:
        title = book["title"]
        pages = book["pages"]
        if pages > largestBook:
            largestBook = pages
            bookTitle = title
        else: continue
    return print(f"⭐️ {bookTitle} is the largest book with {largestBook} pages.")
        
def show_oldest_book(shelf):
    oldestBook = 2300
    bookTitle = ""
    for book in shelf:
        title = book["title"]
        year = book["year"]
        if year < oldestBook:
            oldestBook = year
            bookTitle = title
        else: continue
    return print(f"⭐️ {bookTitle} is the oldest book published in the year {oldestBook}.")

def top_rated_book(shelf):
    topRating = 0
    bookTitle = ""
    for book in shelf:
        title = book["title"]
        rating = book["rating"]
        if rating > topRating:
            topRating = rating
            bookTitle = title
    return print(f"⭐️ {bookTitle} is the top rated book at a rating of {topRating}.")
        

def describe_all_books(shelf):
    for book in shelf:
        print(describe_book(book))


def create_book():
    bookName = input("What is the book's title? ")
    author = input("Who is the book's author? ")
    try:
        year = int(input("When was the book published? "))
    except:
        year = int(input("A year is required in this format (ex: 1998, 2008). What year was the book published? "))
    try:
        rating = float(input("What is the book's rating "))
    except:
        rating = float(input("A rating is required in this format (ex: 3.4 or 5) What is the book's rating "))
    try:
        pages = int(input("How many pages does the book have? "))
    except:
        pages = int(input("Pages must be in number format only. How many pages does the book have? "))


    new_book_dic = {
        "title": bookName,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return new_book_dic



def main_menu(trigger):
    x = input("Choose an option: \n A: Add Book \n B: Describe All Books \n C: Find Oldest Book \n D: Find Longest Book \n E: Find Top Rated Book \n F: End Inquiry \n \n Selection: ")
    if x.lower() == "a":
        my_book_shelf.append(create_book())
    elif x.lower() == "b":
        describe_all_books(my_book_shelf)
    elif x.lower() == "c":
        show_oldest_book(my_book_shelf)
    elif x.lower() == "d":
        show_longest_book(my_book_shelf)
    elif x.lower() == "e":
        top_rated_book(my_book_shelf)
    elif x.lower() == "f":
        return False
    else:
        x = input("ERROR!!! \n Only choose the following: \n A: Add Book \n B: Describe All Books \n C: Find Oldest Book \n D: Find Longest Book \n E: Find Top Rated Book \n F: End Inquiry \n \n Selection: ")
    return trigger


trigger = True

while trigger:
    trigger = main_menu(trigger)



