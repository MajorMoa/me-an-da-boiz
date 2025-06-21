import os
import tkinter as tk 
from tkinter import messagebox
import math

# Screen circle parameters
RADIUS = 200  # radius of circle in pixels
CENTER_X = 700  # center X position of the circle on screen
CENTER_Y = 500  # center Y position of the circle on screen
ANGLE_STEP = 5  # degrees to move per update

class WindowMover:
    def __init__(self, root):
        self.root = root
        self.angle = 0  # degrees

        self.update_position()

    def update_position(self):
        rad = math.radians(self.angle)
        x = int(CENTER_X + RADIUS * math.cos(rad))
        y = int(CENTER_Y + RADIUS * math.sin(rad))

        # Move the window to new position
        self.root.geometry(f"+{x}+{y}")

        self.angle = (self.angle + ANGLE_STEP) % 360

        # Call this method again after 50ms
        self.root.after(20, self.update_position)

root = tk.Tk()
root.title("o")

root.geometry("100x100")  # Set initial window size

mover = WindowMover(root)


print("hello, World!")
if 1 == 1:
    print("coool")

# Start the Tkinter event loop
root.mainloop()

