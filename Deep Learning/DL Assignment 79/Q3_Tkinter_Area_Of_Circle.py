"""
3: Area of Circle
Develop a Tkinter application that accepts the radius of a circle. Provide a Calculate Area button to calculate
and display the area of the circle.
"""

import tkinter as tk
import math

root = tk.Tk()

root.title("Marvellous Circle Area Calculator")
root.geometry("400x300")

tk.Label(
    root,
    text="Marvellous Infosystems",
    font=("Arial", 18, "bold")
).pack(pady=10)

tk.Label(
    root,
    text="Enter Radius"
).pack()

entryRadius = tk.Entry(root)
entryRadius.pack()


def CalculateArea():
    radius = float(entryRadius.get())

    area = math.pi * radius * radius

    labelResult.config(
        text="Area of Circle : " + str(area)
    )


tk.Button(
    root,
    text="Calculate Area",
    command=CalculateArea
).pack(pady=15)

labelResult = tk.Label(
    root,
    text="",
    font=("Arial", 14)
)
labelResult.pack()

root.mainloop()