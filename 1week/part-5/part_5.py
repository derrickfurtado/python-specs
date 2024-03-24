### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

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

    with open("book_shelf.txt", "a") as f:
        f.write(f"{bookName}, {author}, {year}, {rating}, {pages} \n")

# create_book()

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

def describe_book(book):
    title = book["title"]
    author = book["author"]
    year = book["year"]
    rating = book["rating"]
    pages = book["pages"]

    script = f"⭐️ {title} written by {author} and published in the year {year}. With an average rating of {rating}, this book has a total length of {pages} pages."

    return script

def describe_all_books():

    with open("book_shelf.txt", "r") as f:
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

describe_all_books()

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

# 🚨🚨🚨🚨🚨🚨 SEE main_menu.py file for this 🚨🚨🚨🚨🚨🚨 

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!


# 🚨🚨🚨🚨🚨🚨 SEE main_menu.py file for this 🚨🚨🚨🚨🚨🚨 
