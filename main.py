from notebook import Notebook

def display_menu():
    print("\nNote Taking Menu:")
    print("1. Add a Note")
    print("2. Remove a Note")
    print("3. Display All Notes")
    print("4. Exit")

def run():
    my_notebook = Notebook()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter the note title: ")
            content = input("Enter the note content: ")
            my_notebook.add_notes(title, content)
        elif choice == "2":
            title_to_remove = input("Enter the title of the note to remove: ")
            my_notebook.remove_note(title_to_remove)
        elif choice == "3":
            my_notebook.display_all_notes()
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

run()



