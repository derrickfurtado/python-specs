### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

bookName = input("What is the book's title? ")



author = input("Who is the book's author? ")



#year = input("when was the book published? ")



#rating = input("What is the book's rating ")



#pages = input("How many pages does the book have? ")




### Step 2 - Type conversion

## Now convert the proper data-types from strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here


year = int(input("When was the book published? "))



rating = float(input("What is the book's rating "))



pages = int(input("How many pages does the book have? "))




### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

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


    new_book_dic = {
        "title": bookName,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return new_book_dic

print(create_book())

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

def main_menu():
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

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

trigger = True

while trigger:
    trigger = main_menu(trigger)