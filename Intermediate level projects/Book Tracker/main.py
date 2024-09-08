# Project Title: Book Tracker

import pandas as pd

data = {
    'Book': [
        'To Kill a Mockingbird', '1984', 'The Great Gatsby', 'The Catcher in the Rye', 'Moby Dick',
        'Pride and Prejudice', 'War and Peace', 'The Hobbit', 'Brave New World', 'The Kite Runner',
        'Harry Potter and the Sorcerer\'s Stone', 'The Lord of the Rings', 'The Book Thief', 'Fahrenheit 451',
        'Jane Eyre', 'The Alchemist', 'Animal Farm', 'The Chronicles of Narnia', 'Gone with the Wind',
        'The Hunger Games', 'The Da Vinci Code', 'The Handmaid\'s Tale', 'The Fault in Our Stars',
        'The Road', 'A Game of Thrones', 'Memoirs of a Geisha', 'The Girl on the Train', 'The Help', 
        'The Picture of Dorian Gray', 'The Shining'
    ],
    'Genre': [
        'Fiction', 'Dystopian', 'Classic', 'Classic', 'Adventure',
        'Romance', 'Historical', 'Fantasy', 'Dystopian', 'Drama',
        'Fantasy', 'Fantasy', 'Historical', 'Dystopian', 'Classic',
        'Adventure', 'Satire', 'Fantasy', 'Historical', 'Dystopian',
        'Thriller', 'Dystopian', 'Drama', 'Post-apocalyptic', 'Fantasy',
        'Historical', 'Thriller', 'Drama', 'Classic', 'Horror'
    ],
    'Status': [
        'Read', 'Read', 'To-Read', 'To-Read', 'To-Read',
        'Read', 'Read', 'To-Read', 'Read', 'Read',
        'To-Read', 'Read', 'Read', 'To-Read', 'Read',
        'To-Read', 'Read', 'Read', 'Read', 'To-Read',
        'To-Read', 'Read', 'To-Read', 'Read', 'To-Read',
        'To-Read', 'Read', 'To-Read', 'To-Read', 'Read'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Book Tracker:")
print(df)

# Function to update the status of a book (mark as 'Read')
def mark_as_read(book_name):
    if book_name in df['Book'].values:
        df.loc[df['Book'] == book_name, 'Status'] = 'Read'
        print(f"\nStatus updated: '{book_name}' marked as 'Read'.")
    else:
        print(f"\n'{book_name}' is not in the list.")

# Function to view the list of books to read
def view_books_to_read():
    to_read_books = df[df['Status'] == 'To-Read']
    return to_read_books

# Function to view the list of books already read
def view_books_read():
    read_books = df[df['Status'] == 'Read']
    return read_books

# Example Usage
print("\nBooks to Read:")
print(view_books_to_read())

print("\nBooks Already Read:")
print(view_books_read())

# Mark a book as read
book_to_mark = 'The Great Gatsby'
mark_as_read(book_to_mark)

# Show updated list
print("\nUpdated Book Tracker:")
print(df)
