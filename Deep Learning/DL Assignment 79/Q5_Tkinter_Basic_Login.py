"""
Question 5:
5: Basic Login Form
Develop a Tkinter application that accepts a username and password using Entry widgets. Provide a Login
button to validate the entered credentials against predefined values and display an appropriate success or failure
message.
"""

import tkinter as tk

root = tk.Tk()

root.title("Marvellous Login Form")
root.geometry("400x300")

tk.Label(
    root,
    text="Marvellous Infosystems",
    font=("Arial", 18, "bold")
).pack(pady=10)

tk.Label(
    root,
    text="Enter Username"
).pack()

entryUsername = tk.Entry(root)
entryUsername.pack()

tk.Label(
    root,
    text="Enter Password"
).pack()

entryPassword = tk.Entry(root, show="*")
entryPassword.pack()


def Login():
    username = entryUsername.get()
    password = entryPassword.get()

    predefinedUsername = "admin"
    predefinedPassword = "admin123"

    if username == predefinedUsername and password == predefinedPassword:
        labelResult.config(
            text="Login Successful!"
        )
    else:
        labelResult.config(
            text="Invalid Username or Password!"
        )


tk.Button(
    root,
    text="Login",
    command=Login
).pack(pady=15)

labelResult = tk.Label(
    root,
    text="",
    font=("Arial", 14)
)
labelResult.pack()

root.mainloop()