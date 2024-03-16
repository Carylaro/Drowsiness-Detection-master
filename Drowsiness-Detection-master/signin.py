# from tkinter import *
# from PIL import ImageTk
# from signup import create_signup_window
#
#
# def login_page():
#     signin_window.destroy()
#     create_signup_window()
#
# def create_signin_window():
#     signin_window = Tk()
#     signin_window.title('Signin Page')
#     signin_window.resizable(False, False)
#     background = ImageTk.PhotoImage(file='bg.jpg')
#
#     bgLabel = Label(signin_window, image=background)
#     bgLabel.grid()
#
#     frame = Frame(signin_window, bg='white')
#     frame.place(x=560, y=100)
#
#     heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 19, 'bold')
#                     , bg='white', fg='firebrick1')
#     heading.grid(row=0, column=0, padx=2, pady=2)
#
#     emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 10, 'bold')
#                        , bg='white', fg='firebrick1')
#     emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))
#
#     emailEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold')
#                        , fg='white', bg='firebrick1')
#     emailEntry.grid(row=2, column=0, sticky='w', padx=25)
#
#     usernameLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light', 10, 'bold')
#                           , bg='white', fg='firebrick1')
#     usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))
#
#     usernameEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold')
#                           , fg='white', bg='firebrick1')
#     usernameEntry.grid(row=4, column=0, sticky='w', padx=25)
#
#     passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light', 10, 'bold')
#                           , bg='white', fg='firebrick1')
#     passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))
#
#     passwordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold')
#                           , fg='white', bg='firebrick1')
#     passwordEntry.grid(row=6, column=0, sticky='w', padx=25)
#
#     confirmLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 10, 'bold')
#                          , bg='white', fg='firebrick1')
#     confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))
#
#     confirmEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold')
#                          , fg='white', bg='firebrick1')
#     confirmEntry.grid(row=8, column=0, sticky='w', padx=25)
#
#     vechileLabel = Label(frame, text='Vechicle Number', font=('Microsoft Yahei UI Light', 10, 'bold')
#                          , bg='white', fg='firebrick1')
#     vechileLabel.grid(row=9, column=0, sticky='w', padx=25, pady=(10, 0))
#
#     vechileEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold')
#                          , fg='white', bg='firebrick1')
#     vechileEntry.grid(row=10, column=0, sticky='w', padx=25)
#
#     termsandconditions = Checkbutton(frame, text='I agree to the Terms & Conditions',
#                                      font=('Microsoft Yahei UI Light', 9, 'bold'),
#                                      fg='firebrick1', bg='white', activebackground='white',
#                                      activeforeground='firebrick1'
#                                      , cursor='hand2')
#     termsandconditions.grid(row=11, column=0, pady=2, padx=2)
#
#     signinButton = Button(frame, text='Signin', font=('Open Sans', 13, 'bold'), bd=0,
#                           bg='firebrick1', fg='white', activebackground='firebrick1',
#                           activeforeground='white', width=17)
#     signinButton.grid(row=12, column=0, pady=10)
#
#     alreadyaccount = Label(frame, text="Don't have an account?", font=('Open Sans', '9', 'bold'),
#                            bg='white', fg='firebrick1')
#     alreadyaccount.grid(row=13, column=0, sticky='w', padx=25, pady=2)
#
#     loginButton = Button(frame, text='Log in', font=('Open Sans', 9, 'bold underline')
#                          , bg='white', fg='blue', bd=0, cursor='hand2', activebackground='white',
#                          activeforeground='blue', command=login_page)
#     loginButton.place(x=174, y=412)
#     signin_window.mainloop()
#
#
#
# if __name__ == "__main__":
#     create_signin_window



from tkinter import *
from PIL import ImageTk
from signup import create_signup_window

def login_page():
    global signin_window
    signin_window.destroy()
    create_signup_window()

def create_signin_window():
    global signin_window
    signin_window = Tk()
    signin_window.title('Signin Page')
    signin_window.resizable(False, False)
    background = ImageTk.PhotoImage(file='bg.jpg')

    bgLabel = Label(signin_window, image=background)
    bgLabel.grid()

    frame = Frame(signin_window, bg='white')
    frame.place(x=560, y=100)

    heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 19, 'bold')
                    , bg='white', fg='firebrick1')
    heading.grid(row=0, column=0, padx=2, pady=2)

    emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 10, 'bold')
                       , bg='white', fg='firebrick1')
    emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))

    emailEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold')
                       , fg='white', bg='firebrick1')
    emailEntry.grid(row=2, column=0, sticky='w', padx=25)

    usernameLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light', 10, 'bold')
                          , bg='white', fg='firebrick1')
    usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))

    usernameEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold')
                          , fg='white', bg='firebrick1')
    usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

    passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light', 10, 'bold')
                          , bg='white', fg='firebrick1')
    passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))

    passwordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold')
                          , fg='white', bg='firebrick1')
    passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

    confirmLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 10, 'bold')
                         , bg='white', fg='firebrick1')
    confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))

    confirmEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold')
                         , fg='white', bg='firebrick1')
    confirmEntry.grid(row=8, column=0, sticky='w', padx=25)

    vechileLabel = Label(frame, text='Vechicle Number', font=('Microsoft Yahei UI Light', 10, 'bold')
                         , bg='white', fg='firebrick1')
    vechileLabel.grid(row=9, column=0, sticky='w', padx=25, pady=(10, 0))

    vechileEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold')
                         , fg='white', bg='firebrick1')
    vechileEntry.grid(row=10, column=0, sticky='w', padx=25)

    termsandconditions = Checkbutton(frame, text='I agree to the Terms & Conditions',
                                     font=('Microsoft Yahei UI Light', 9, 'bold'),
                                     fg='firebrick1', bg='white', activebackground='white',
                                     activeforeground='firebrick1'
                                     , cursor='hand2')
    termsandconditions.grid(row=11, column=0, pady=2, padx=2)

    signinButton = Button(frame, text='Signin', font=('Open Sans', 13, 'bold'), bd=0,
                          bg='firebrick1', fg='white', activebackground='firebrick1',
                          activeforeground='white', width=17)
    signinButton.grid(row=12, column=0, pady=10)

    alreadyaccount = Label(frame, text="Don't have an account?", font=('Open Sans', '9', 'bold'),
                           bg='white', fg='firebrick1')
    alreadyaccount.grid(row=13, column=0, sticky='w', padx=25, pady=2)

    loginButton = Button(frame, text='Log in', font=('Open Sans', 9, 'bold underline')
                         , bg='white', fg='blue', bd=0, cursor='hand2', activebackground='white',
                         activeforeground='blue', command=login_page)
    loginButton.place(x=174, y=412)
    # signin_window.mainloop()
    return signin_window

if __name__ == "__main__":
    create_signin_window()
