"""
2: Find the Largest Number
Develop a Tkinter application that accepts three numbers from the user. Provide a Find Maximum button to
determine and display the largest number.
"""

import tkinter as tk

root = tk.Tk()

root.title("Marvellous Largest Number")
root.geometry("400x350")

tk.Label(
    root,
    text="Marvellous Infosystems",
    font=("Arial", 18, "bold")
).pack(pady=10)

tk.Label(root, text="Enter First Number").pack()

entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()

entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Enter Third Number").pack()

entry3 = tk.Entry(root)
entry3.pack()


def FindMaximum():
    no1 = int(entry1.get())
    no2 = int(entry2.get())
    no3 = int(entry3.get())

    maximum = max(no1, no2, no3)

    labelResult.config(
        text="Largest Number is : " + str(maximum)
    )


tk.Button(
    root,
    text="Find Maximum",
    command=FindMaximum
).pack(pady=15)

labelResult = tk.Label(
    root,
    text="",
    font=("Arial", 14)
)
labelResult.pack()

root.mainloop()