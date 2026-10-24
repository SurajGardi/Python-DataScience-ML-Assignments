"""
4: Voting Eligibility Checker
Develop a Tkinter application that accepts a person's name and age. Provide a Check Eligibility button to
determine whether the person is eligible to vote based on the minimum age of 18 years.
"""

import tkinter as tk

root = tk.Tk()

root.title("Marvellous Voting Eligibility Checker")
root.geometry("400x300")

tk.Label(
    root,
    text="Marvellous Infosystems",
    font=("Arial", 18, "bold")
).pack(pady=10)

tk.Label(
    root,
    text="Enter Your Name"
).pack()

entryName = tk.Entry(root)
entryName.pack()

tk.Label(
    root,
    text="Enter Your Age"
).pack()

entryAge = tk.Entry(root)
entryAge.pack()


def CheckEligibility():
    name = entryName.get()
    age = int(entryAge.get())

    if age >= 18:
        labelResult.config(
            text=name + " is eligible to vote."
        )
    else:
        labelResult.config(
            text=name + " is not eligible to vote."
        )


tk.Button(
    root,
    text="Check Eligibility",
    command=CheckEligibility
).pack(pady=15)

labelResult = tk.Label(
    root,
    text="",
    font=("Arial", 14)
)
labelResult.pack()

root.mainloop()