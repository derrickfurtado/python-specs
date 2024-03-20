# Let's assign variables to represent a book you enjoy.

# Step 2 - Strings
# Let's start with Python strings. Replace the "None" with the name of a book, and below the name of the author of your book.

book_name = "Never Split The Difference"
author = "Chris Voss"


type(author)

print("book name is: ", book_name)
print("book name type is: ", type(book_name))
print("author is: ", author)
print("author type is: ", type(author))
# book_name = "Dune"
# author = "Frank Herbert"

print("===============================")

# Step 3 - Concatenation and f-strings
# Use concatenation and f-strings to make a sentence about your author and book name.

sentence1 = f"{book_name} is written by {author}."


print("sentence 1 is: ", sentence1)
print("sentence 1 type is: ", type(sentence1))
print("===============================")

# sentence1 = book_name + " is written by " + author + "."
sentence2 = f"Author, {author}, wrote the book {book_name}"
type(sentence2)
print("sentence 2 is: ", sentence2)
print("sentence 2 type is: ", type(sentence2))
# sentence2 = f"Author, {author}, wrote the book {book_name}."
print("===============================")


# Step 4 - Integers
# Now let's practice Integers. Replace the "None" below with the publication date of your book.
publication_year = 2016
type(publication_year)
print("publication year is: ", publication_year)
print("publication year type is: ", type(publication_year))
# publication_year = 1965
print("===============================")


# Step 5 - Floats
# Now estimate what the retail value of your book would be at a store and replace the "None" below with a float value of the price. (Doesn't have to be accurate.)
book_price = 19.99
type(book_price)
print("book price is: ", book_price)
print("book price type is: ", type(book_price))
# book_price = 17.99
print("===============================")


# Step 6 - Booleans
# Now we will practice with booleans. Replace the "is_awesome" variable with a boolean. True if your book is awesome, False if your book is not awesome.
is_awesome = True
type(is_awesome)
print("boolean is: ", is_awesome)
print("boolean type is: ", type(is_awesome))
# is_awesome = True
print("===============================")


# Step 7 - print and type functions
# Follow the instructions, and below this line, code all of the suggested print statements and the type statements.
# Code below

print(f"{book_name} was written by {author} and published in {publication_year}. It sold at an MSRP of ${book_price}.")
print("===============================")
