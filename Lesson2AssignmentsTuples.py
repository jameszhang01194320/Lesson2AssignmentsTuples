# Lesson 2: Assignments | Tuples
# Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!
# Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!
# ________________________________________
# 1. Tuple Mastery in Python
# Objective: The aim of this assignment is to deepen your understanding of tuples in Python, along with their interaction with lists, dictionaries, and basic Python functionalities like functions, input handling, and string formatting. By completing this assignment, you will enhance your skills in data structuring, manipulation, and application of tuples in practical scenarios.
# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should loop through the list of itineraries and print a formatted string for each. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be:
# "Itinerary 1: Alice - From New York to London"
#  "Itinerary 2: Bob - From Tokyo to San Francisco"
def d():
    print("="*75)

d()
def print_itineraries(itineraries):
    for i, itinerary in enumerate(itineraries, start=1):
        traveler_name, origin, destination = itinerary
        print(f"Itinerary {i}: {traveler_name} - From {origin} to {destination}")

# sample
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

# call function
print_itineraries(itineraries)



# 2. Python Data Structure Challenges in Real-World Scenarios
# Objective: This assignment is designed to enhance your understanding and application of Python's core data structures - tuples, lists, and dictionaries - in real-world contexts. By engaging with these tasks, you will practice manipulating these data structures, applying built-in Python methods, and implementing error handling in practical situations.
# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.
# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.
# Existing Library Data:
# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# •	Add functionality to insert new books into library.
# •	Ensure that adding a duplicate book is handled appropriately (hint: do a membership check to see if the new book is already in the library).
d()
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def insert_book(library, title, author):
    new_book = (title, author)
    if new_book not in library:
        library.append(new_book)
        print(f"Book '{title}' by {author} has been added to the library.")
    else:
        print(f"Book '{title}' by {author} is already in the library.")

insert_book(library, "2024", "James Char")
print(library)
d()