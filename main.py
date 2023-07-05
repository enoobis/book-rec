import pandas as pd

def book_recommendation():
    # Load the books data from the CSV file
    books_data = pd.read_csv('data.csv')

    # Ask the user for their preferences
    favorite_book = input("Enter your favorite book: ")
    favorite_genre = input("Enter your favorite genre: ")
    favorite_author = input("Enter your favorite author: ")

    # Filter the books based on user preferences
    filtered_books = books_data[
        (books_data['Book'].str.contains(favorite_book, case=False)) |
        (books_data['Genres'].str.contains(favorite_genre, case=False)) |
        (books_data['Author'].str.contains(favorite_author, case=False))
    ]

    # Display the recommended books with numbers
    if len(filtered_books) > 0:
        print("Recommended Books:")
        for index, book in filtered_books.head(10).iterrows():
            print(f"{index + 1}. {book['Book']}")
    else:
        print("No suitable books found.")

    # Prompt for reload or exit
    choice = input("Enter 'r' to reload or 'e' to exit: ")
    if choice.lower() == 'r':
        book_recommendation()
    elif choice.lower() == 'e':
        print("Exiting the program...")
    else:
        print("Invalid choice. Exiting the program...")

# Start the book recommendation program
book_recommendation()