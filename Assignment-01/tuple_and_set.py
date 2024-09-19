books = (
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("1984", "George Orwell", 1949),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
)

tags = {"classic", "dystopian", "novel", "literature"}

# a
print(books[1][1])  # Output: George Orwell
print()

# b
new_book = ("Brave New World", "Aldous Huxley", 1932)
books = books + (new_book,)
print(books)
print()

# c
title, author, year = books[2]
print(f"Title: {title}, Author: {author}, Year: {year}")
print()

# d
for book in books:
    print(book[0])
    print()

# e
tags.add("sci-fi")
print(tags)
print()

# f
tags.remove("novel")
print(tags)