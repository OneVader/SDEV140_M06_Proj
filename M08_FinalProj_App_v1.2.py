"""
M08 Final Project - GUI App
Author: Nelson Marte
completed 10-12-2024
Assignment:
GUI App.
REQUIRED EXTERNAL libraries (install via PIP); PIL (for image processing),
tkinterweb (loading webpages), re (form validation)
GIF credits - https://dribbble.com/madebyradio, https://dribbble.com/shots/2130577-Petsvoyage,
https://dribbble.com/shots/3821639-Day-17-18-Corgi
"""

# Import tkinter namespace as "tk" for brevity
import tkinter as tk
# Import the tkinter themed gui widgets
from tkinter import ttk
# Import the rest of the tkinter modules
from tkinter import *
# Import PIL library to handle images (EXTERNAL)
from PIL import Image, ImageTk
# Load tkinterweb (EXTERNAL)
import tkinterweb
# Import OS module to set the cwd() to file location // Current IDE set to a different directory
import os
# Identify cwd of the script and assign it to a variable
script_dir = os.path.dirname(os.path.abspath(__file__))
# Use OS method to change the cwd to the script directory // Needed for loading images
os.chdir(script_dir)
# module form validation
import re

'''3 POP-UP window classes'''
# About Us Window
class About_Us(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # Define the size of the window
        self.geometry('800x600')
        # Label the window
        self.title("About Us")
        # Set background color for window
        self.configure(bg="#f7c394")
        # Add a button to close the window
        ttk.Button(self,
                text='Close',
                command = self.destroy).pack(expand=False)
        # Open the Logo gif image
        image = Image.open('corgy_anim-ezgif.com-250x250crop.gif')
        # List to hold frames
        frames = []
        try:
            while True:
                frames.append(ImageTk.PhotoImage(image))
                image.seek(image.tell() + 1)
        except EOFError:
            pass
        # Create a label to display the gif
        label = tk.Label(self, borderwidth=0,highlightthickness=0)
        # Attach the GIF variable to the object
        label.pack()
        # Function updates the Label with the next frame
        def update(index):
            frame = frames[index]
            index = (index +1) % len(frames)
            label.configure(image=frame)
            self.after(25, update, index)
        # Starts Logo GIF animation
        update(0)
        # About Us Text
        text = Label(self,
                    text = "1) We select the best shipment route and approve it with you\n2) We choose comfortable container for your pet's shipment\n3) We arrange for all veterinary procedures required for the travel\n4) We obtain the required paperwork for the shipment\n5) We air ship your pet\n6) You pick up a happy pet on arrival",
                    font = ('Forte', 14,'bold'),bg='#f7c394'
                    ).pack()


# Contact window "Start Inquiry"
class StartInq(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # Define the size of the window
        self.geometry('800x600')
        # Label the window
        self.title("Contact Form")
        # Set background color for window
        self.configure(bg="#fed12c")
        # Add a button to close the window
        ttk.Button(self,
                text='Close',
                command = self.destroy).pack(expand=False)

        # Open the Logo gif image
        image = Image.open('shape_shift_vehicles_anim-ezgif.com-250x250crop.gif')
        # List to hold frames
        frames = []
        try:
            while True:
                frames.append(ImageTk.PhotoImage(image))
                image.seek(image.tell() + 1)
        except EOFError:
            pass
        # Create a label to display the gif
        label = tk.Label(self, borderwidth=0,highlightthickness=0)
        # Attach the GIF variable to the object
        label.pack()
        # Function updates the Label with the next frame
        def update(index):
            frame = frames[index]
            index = (index +1) % len(frames)
            label.configure(image=frame)
            self.after(32, update, index)
        # Starts Logo GIF animation
        update(0)

        '''CONTACT FORM FUNCTIONS'''
        # CREDIT - https://www.geeksforgeeks.org/validating-entry-widget-in-python-tkinter/
        # Function to validate email
        def validate_email(email):
            """Validates email format."""
            pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            return bool(re.match(pattern, email))
        # function to check valid name (string)
        def validate_name(name):
            if name.isalpha():
                return True
            return False
        # Clicking 'submit' button function
        def send_email():
            # First pulls entry field information
            name = name_entry.get()
            email = email_entry.get()
            message = message_entry.get("1.0", tk.END)
            # Checks data fields are empty
            if not name or not email or not message:
                error_label.config(text="Please fill all fields.")
            # Checks name entry field data is only alphabetical
            elif not validate_name(name):
                error_label.config(text="Invalid name.", fg="red")
            # Checks email in valid format
            elif not validate_email(email):
                error_label.config(text="Invalid email format.", fg="red")
            else:
                # Implement your email sending logic here
                # You can use smtplib or other libraries
                print("Email sent successfully!")
                error_label.config(text="Email sent successfully!", fg="green", bg="#fed12c")
        # Entry Fields
        name_label = tk.Label(self, text="Name:")
        name_label.pack()

        name_entry = tk.Entry(self)
        name_entry.insert(0, "First Name Only")
        name_entry.pack()

        email_label = tk.Label(self, text="Email:")
        email_label.pack()

        email_entry = tk.Entry(self)
        email_entry.pack()

        message_label = tk.Label(self, text="Message:")
        message_label.pack()

        message_entry = tk.Text(self, height=5)
        message_entry.pack()

        send_button = tk.Button(self, text="Send", command=send_email)
        send_button.pack()

        error_label = tk.Label(self, text="", fg="red", bg="#fed12c")
        error_label.pack()

# External Site Resource - APHIS USDA.gov
class WebPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('800x600')
        # Label the window
        self.title("Start Inquiry")
        # Set background color for window
        self.configure(bg="#fdfacf")
        # Add a button to close the window
        ttk.Button(self,
                text='Close',
                command = self.destroy).pack(expand=False)
        # Create the browser interface with 'frame' object
        # CREDIT = https://www.youtube.com/watch?v=1L5zPhhUVic
        # skipped 'root = Tk()' function and the mainloop() portions
        frame = tkinterweb.HtmlFrame(self)
        # loads page with URL
        frame.load_website("https://www.aphis.usda.gov/pet-travel")
        # attach web-interface widget to window via pack() [standard top to bottom approach]
        frame.pack()

''' MAIN Program Window '''
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Set window parameters
        self.geometry('800x600')
        # Set background color for this window
        self.configure(bg='#fdfacf')

        ''' ANIMATED LOGO SECTION '''
        # CREDIT - stackoverflow (scoured so many I lost the original post, apologies)
        # Open the Logo gif image
        image = Image.open('PetsVoyage_anim_250x250crop.gif')
        # List to hold frames
        frames = []
        try:
            while True:
                frames.append(ImageTk.PhotoImage(image))
                image.seek(image.tell() + 1)
        except EOFError:
            pass
        # Create a label to display the gif
        label = tk.Label(self, borderwidth=0,highlightthickness=0)
        # Attach the GIF variable to the object
        label.pack()
        # Function updates the Label with the next frame
        def update(index):
            frame = frames[index]
            index = (index +1) % len(frames)
            label.configure(image=frame)
            self.after(100, update, index)
        # Starts Logo GIF animation
        update(0)

        ''' BUTTONS '''
        # Add navigation button to the main window app
        ttk.Button(self,
                text = "About Us",
                command = self.aboutUs_win).pack(expand=True)
        ttk.Button(self,
                text = "Contact Us",
                command = self.startInq_win).pack(expand=True)
        ttk.Button(self,
                text = "Start Here - APHIS",
                command = self.webPage_win).pack(expand=True)
        # CREDIT - https://youtu.be/YXPyB4XeYLA?list=PLutzsjJxwIZKUHSDUFMNuc1NqjePOB7HE&t=4878
        ttk.Button(self,
                text = "EXIT",
                command = self.quit).pack(expand=True)

    # Function to open designated window
    def aboutUs_win(self):
        aboutUs = About_Us(self)
        # grab_set function allows a Toplevel window to take complete control over the keyword and mouse events
        aboutUs.grab_set()
    
    def startInq_win(self):
        startQuery = StartInq(self)
        startQuery.grab_set()
    
    def webPage_win(self):
        aphisSite = WebPage(self)
        aphisSite.grab_set()
    
# RUN main program
if __name__ == "__main__":
    app = App()
    # Label to name the Program
    app.title("Welcome to Petsvoyage")
    # Create a variable for the window icon/logo/img
    icon = tk.PhotoImage(file='PetsVoyage_anim-ezgif.com-icon.gif')
    # iconphoto() method sets the titlebar icon
    app.iconphoto(True, icon)
    # Execute app
    app.mainloop()