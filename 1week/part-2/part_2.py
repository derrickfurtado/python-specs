### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["Chris Voss","Sun Zhu","Tom Clancy","Kurt Vonnegut","Michael Crichton","John Steinbeck","Ernest Hemingway"]
print(my_authors)

# Now let's add a new author to the end with the .append() method. Type your code below.

my_authors.append("Mark Twain")
# Code here
# Example: my_authors.append("H.G. Wells")
print(my_authors)


# Now let's remove an element in the list

# Code here

my_authors.pop()

print(my_authors)
# Example: my_authors.remove("H.G. Wells")


# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here

print(my_authors[3])
# Example: my_authors[2]


# Now slice the list.

# Code here

print(my_authors[2:4])
# Example: my_authors[1:4]


### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here

my_author_tuple = ("Chris Voss","Sun Zhu","Tom Clancy","Kurt Vonnegut","Michael Crichton","John Steinbeck","Ernest Hemingway")
print("My tuple is: ", my_author_tuple)
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")


### Step 3 - Sets ###

# Create a set with your authors.


# Code here
my_author_set = {"Chris Voss","Sun Zhu","Tom Clancy","Kurt Vonnegut","Michael Crichton","John Steinbeck","Ernest Hemingway"}
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}


# Add a new author to your set.

# Code here
my_author_set.add("J.K. Rawlings")
# Example: my_author_set.add("J.R.R. Tolkien")


# Try adding the same author again, and be sure to print your set.

# Code here
my_author_set.add("J.K. Rawlings")

print("My set is: ", my_author_set)

# Example: my_author_set.add("J.R.R. Tolkien")



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
print("=====================")

for author in my_authors:
    print("Here is an author in the LIST: ", author)

print("=====================")

for tuples in my_author_tuple:
    print("Here is an author in my TUPLE: ",tuples)

print("=====================")

for set in my_author_set:
    print("Here is an author in my SET: ",set)

print("=====================")

# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

