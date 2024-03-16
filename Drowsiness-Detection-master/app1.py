from flask import Flask,redirect, url_for,render_template,request
import os
from index import d_dtcn
from tkinter import *  # Importing tkinter library for GUI
from PIL import ImageTk
secret_key = str(os.urandom(24))

app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = secret_key
app.config['DEBUG'] = True

 # Importing ImageTk module from PIL library for image handling

# Function to navigate to signup page
def signup_page():
    login_window.destroy()  # Destroying current window
    signin_page()  # Opening signup page

# Function to navigate to signin page
def login_page():
    signin_window.destroy()  # Destroying current window
    signup_page()  # Opening signin page

# Function to hide password
def hide():
    openeye.config(file='closeye.png')  # Change image to closed eye
    passwordEntry.config(show='*')  # Show password as asterisks
    eyeButton.config(command=show)  # Change button command to show password

# Function to show password
def show():
    openeye.config(file='openeye.png')  # Change image to open eye
    passwordEntry.config(show='')  # Show password as plain text
    eyeButton.config(command=hide)  # Change button command to hide password

# Function to handle username entry focus
def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)  # Clear default username text when focused

# Function to handle password entry focus
def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)  # Clear default password text when focused

# Function to display signin page
def signin_page():
    global signin_window  # Declare signin_window as global variable
    signin_window = Tk()  # Creating a new Tkinter window
    signin_window.title('Signin Page')  # Setting window title
    signin_window.resizable(False, False)  # Making window non-resizable
    background = ImageTk.PhotoImage(file='bg.jpg')  # Loading background image

    bgLabel = Label(signin_window, image=background)  # Creating label for background image
    bgLabel.grid()  # Placing background label

    frame = Frame(signin_window, bg='white')  # Creating frame for content
    frame.place(x=560, y=100)  # Placing frame

    heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 19, 'bold'),
                    bg='white', fg='firebrick1')  # Creating heading label
    heading.grid(row=0, column=0, padx=2, pady=2)  # Placing heading label

    # Rest of your GUI components for signin page...

    signin_window.mainloop()  # Running main loop for signin window

# GUI part for login page
login_window = Tk()  # Creating Tkinter window
login_window.geometry('990x660+50+50')  # Setting window geometry
login_window.resizable(0, 0)  # Making window non-resizable
login_window.title('Login Page')  # Setting window title
bgImage = ImageTk.PhotoImage(file='bg.jpg')  # Loading background image

bgLabel = Label(login_window, image=bgImage)  # Creating label for background image
bgLabel.place(x=0, y=0)  # Placing background label

heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'),
                bg='white', fg='firebrick1')  # Creating heading label
heading.place(x=605, y=120)  # Placing heading label

# Rest of your GUI components for login page...
# Rest of GUI components for login page...

usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
                      bd=0, fg='firebrick1')  # Creating entry widget for username
usernameEntry.place(x=580, y=200)  # Placing entry widget for username
usernameEntry.insert(0, 'Username')  # Inserting default text in username entry

usernameEntry.bind('<FocusIn>', user_enter)  # Binding focus event to username entry

frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')  # Creating frame for underline effect
frame1.place(x=580, y=222)  # Placing frame for underline effect

passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
                      bd=0, fg='firebrick1')  # Creating entry widget for password
passwordEntry.place(x=580, y=260)  # Placing entry widget for password
passwordEntry.insert(0, 'Password')  # Inserting default text in password entry

passwordEntry.bind('<FocusIn>', password_enter)  # Binding focus event to password entry

frame2 = Frame(login_window, width=250, height=2, bg='firebrick1')  # Creating frame for underline effect
frame2.place(x=580, y=282)  # Placing frame for underline effect

openeye = PhotoImage(file='openeye.png')  # Loading open eye image
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white',
                   cursor='hand2', command=hide)  # Creating button for hiding/showing password
eyeButton.place(x=800, y=250)  # Placing button for hiding/showing password

forgetButton = Button(login_window, text='Forgot Password', bd=0, bg='white', activebackground='white',
                      cursor='hand2', font=('Microsoft Yahei UI Light', 9, 'bold'),
                      fg='firebrick1', activeforeground='firebrick1')  # Creating forget password button
forgetButton.place(x=715, y=295)  # Placing forget password button

loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'),
                     fg='white', bg='firebrick1', activeforeground='white',
                     activebackground='firebrick1', cursor='hand2', bd=0, width=19)  # Creating login button
loginButton.place(x=578, y=350)  # Placing login button

orLabel = Label(login_window, text='----------------OR------------------', font=('Open Sans', 16),
                fg='firebrick1', bg='white')  # Creating label for divider
orLabel.place(x=568, y=395)  # Placing label for divider

facebook_logo = PhotoImage(file='facebook.png')  # Loading Facebook logo image
fbLabel = Label(login_window, image=facebook_logo, bg='white')  # Creating label for Facebook logo
fbLabel.place(x=640, y=440)  # Placing label for Facebook logo

google_logo = PhotoImage(file='google.png')  # Loading Google logo image
googleLabel = Label(login_window, image=google_logo, bg='white')  # Creating label for Google logo
googleLabel.place(x=690, y=440)  # Placing label for Google logo

twitter_logo = PhotoImage(file='twitter.png')  # Loading Twitter logo image
twitterLabel = Label(login_window, image=twitter_logo, bg='white')  # Creating label for Twitter logo
twitterLabel.place(x=740, y=440)  # Placing label for Twitter logo

signupLabel = Label(login_window, text='Dont have an account?', font=('Open Sans', 9, 'bold'),
                    fg='firebrick1', bg='white')  # Creating label for signup prompt
signupLabel.place(x=590, y=500)  # Placing label for signup prompt

newaccountButton = Button(login_window, text='Create new one', font=('Open Sans', 9, 'bold underline'),
                          fg='blue', bg='white', activeforeground='blue',
                          activebackground='white', cursor='hand2', bd=0, command=signup_page)  # Creating signup button
newaccountButton.place(x=727, y=500)  # Placing signup button


if __name__ == "__main__":
    login_window.mainloop()  # Running main loop for login window


# Defining the home page of our site
@app.route("/",methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Continue') == 'Continue':
           return render_template("test1.html")
    else:
        # pass # unknown
        return render_template("index.html")


# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     print(request.method)
#     if request.method == "POST":
#         if request.form.get("Login") == "Login":
#             return render_template("signup.py")
#     else:
#         return render_template("signin.py")


@app.route("/start", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            # pass
            d_dtcn()
            return render_template("index.html")
    else:
        # pass # unknown
        return render_template("index.html")

@app.route('/contact', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('contact.html')

if __name__ == "__main__":
    app.run()
    
