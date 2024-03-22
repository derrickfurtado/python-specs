### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
def capture_book():
    bookName = input("What is the book's title?")
    return bookName

def capture_author():
    author = input("Who is the book's author?")
    return author

# def capture_year():
#     year = input("when was the book published?")
#     return year

# def capture_rating():
#     rating = input("What is the book's rating")
#     return rating

# def capture_pages():
#     pages = input("How many pages does the book have?")
#     return pages



### Step 2 - Type conversion

## Now convert the proper data-types from strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

def capture_year():
    year = input("When was the book published? ")
    return int(year)

def capture_rating():
    rating = input("What is the book's rating ")
    return float(rating)

def capture_pages():
    pages = input("How many pages does the book have? ")
    return int(pages)


print("year type is: ", type(capture_year()))
print("rating type is: ", type(capture_rating()))
print("pages type is: ", type(capture_pages()))

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

