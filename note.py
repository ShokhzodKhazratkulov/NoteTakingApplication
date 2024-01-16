# class Note:
#
#     def __init__(self, title, content, creation_date):
#         self.title = title
#         self.content = content
#         self.creation_date = creation_date
#
#     def display_content(self):
#         """Display Method: Formats and displays the note's information."""
#         print(f"Title: {self.title}\n\n{self.content}\nCreated on: {self.creation_date}")

class Note:
    def __init__(self, title, content, creation_date):
        self.title = title
        self.content = content
        self.creation_date = creation_date

    def display_content(self):
        """Display Method: Formats and displays the note's information."""
        print(f"Title: {self.title}\n{self.content}\nCreated on: {self.creation_date}")
