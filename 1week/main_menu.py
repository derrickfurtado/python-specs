

def describe_book(book):
    title = book["title"]
    author = book["author"]
    year = book["year"]
    rating = book["rating"]
    pages = book["pages"]

    script = f"⭐️ {title} was written by {author} and published in the year {year}. With an average rating of {rating}, this book has a total length of {pages} pages."

    return script

def show_longest_book(db):
    largestBook = 0
    bookTitle = ""

    with open(db, "r") as f:
        read_list = f.readlines()

    for book in read_list:
        book = book.replace(" \n", "").split(", ")
        pages = int(book[4])
        if pages > largestBook:
            largestBook = pages
            bookTitle = book[0]
        else: continue
    return print(f"⭐️ {bookTitle} is the largest book with {largestBook} pages.")
        
def show_oldest_book(db):
    oldestBook = 2300
    bookTitle = ""

    with open(db, "r") as f:
        read_list = f.readlines()
        
    for book in read_list:
        book = book.replace(" \n", "").split(", ")
        book_year = int(book[2])
        if book_year < oldestBook:
            oldestBook = book_year
            bookTitle = book[0]
        else: continue
    return print(f"⭐️ {bookTitle} is the oldest book published in the year {oldestBook}.")

def top_rated_book(db):
    topRating = 0
    bookTitle = ""
    with open(db, "r") as f:
        read_list = f.readlines()

    for book in read_list:
        book = book.replace(" \n", "").split(", ")
        rating = float(book[3])
        if rating > topRating:
            topRating = rating
            bookTitle = book[0]
    return print(f"⭐️ {bookTitle} is the top rated book at a rating of {topRating} out of 5 Stars.")
        

def describe_all_books(db):

    with open(db, "r") as f:
        each_book = f.readlines()

    for book in each_book:
        book = book.replace(" \n", "").split(", ")

        book_dic = {
            'title': book[0],
            'author': book[1],
            'year': book[2],
            'rating': book[3],
            'pages':book[4]
        }
        
        print(describe_book(book_dic))




def create_book(db):
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

    with open(db, "a") as f:
        f.write(f"{bookName}, {author}, {year}, {rating}, {pages} \n")



def main_menu(db):
    trigger = True
    
    while trigger:
        x = input("Choose an option: \n A: Add Book \n B: Describe All Books \n C: Find Oldest Book \n D: Find Longest Book \n E: Find Top Rated Book \n F: End Inquiry \n \n Selection: ")
        if x.lower() == "a":
            create_book(db)
        elif x.lower() == "b":
            describe_all_books(db)
        elif x.lower() == "c":
            show_oldest_book(db)
        elif x.lower() == "d":
            show_longest_book(db)
        elif x.lower() == "e":
            top_rated_book(db)
        elif x.lower() == "f":
            trigger = False
        else:
            x = input("Invalid Entry!!! \n\n Only choose the following: \n A: Add Book \n B: Describe All Books \n C: Find Oldest Book \n D: Find Longest Book \n E: Find Top Rated Book \n F: End Inquiry \n \n Selection: ")


if __name__ == "__main__":
    main_menu("book_shelf.txt")




