import os
import tkinter as tk 
from tkinter import messagebox
import math
import random
import time



root = tk.Tk()
root.title("o")

# Window size
window_width = 220
window_height = 150
root.geometry(f"{window_width}x{window_height}")

# Screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Circular motion setup
center_x = screen_width // 2
center_y = screen_height // 2
radius = 400
angle = 0
hovering = False
delay = 2 # ms

# State
returning_to_circle = False
current_x = 0
current_y = 0

def get_window_position():
    geometry = root.geometry()  # e.g., "100x100+400+300"
    parts = geometry.split("+")
    if len(parts) >= 3:
        return int(parts[1]), int(parts[2])
    return 0, 0

def smooth_return_to_circle():
    global current_x, current_y, angle, returning_to_circle

    # Target x, y on circle
    target_x = int(center_x + radius * math.cos(math.radians(angle)) - window_width // 2)
    target_y = int(center_y + radius * math.sin(math.radians(angle)) - window_height // 2)

    dx = (target_x - current_x) / 10
    dy = (target_y - current_y) / 10

    # Move slightly closer each time
    current_x += dx
    current_y += dy

    root.geometry(f"{window_width}x{window_height}+{int(current_x)}+{int(current_y)}")

    # If close enough, stop returning
    if abs(dx) < 1 and abs(dy) < 1:
        returning_to_circle = False
    else:
        root.after(delay, smooth_return_to_circle)

def move_in_circle():
    global angle, current_x, current_y

    if not hovering and not returning_to_circle:
        x = int(center_x + radius * math.cos(math.radians(angle)) - window_width // 2)
        y = int(center_y + radius * math.sin(math.radians(angle)) - window_height // 2)
        current_x, current_y = x, y
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        angle = (angle + 2) % 360

    root.after(delay, move_in_circle)

def on_enter(event):
    global hovering
    hovering = True
    # Move to a random position
    x = random.randint(0, screen_width - window_width)
    y = random.randint(0, screen_height - window_height)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    

def on_leave(event):
    global hovering, returning_to_circle, current_x, current_y
    hovering = False
    time.sleep(0.8)

    # Get current position and start returning
    current_x, current_y = get_window_position()
    smooth_return_to_circle()


# Bind events
root.bind("<Enter>", on_enter)
root.bind("<Leave>", on_leave)

# Start motion
move_in_circle()




def regain_focus(event):
    print("Lost focus ! regaining it!")
    root.lift()
    root.focus_force()
    root.attributes("-topmost", True)
    root.after(100, lambda: root.attributes("-topmost", False))

# Bind to losing focus
root.bind("<FocusOut>", regain_focus)

# Initial focus setup
def focus_window():
    root.lift()
    root.focus_force()
    root.attributes("-topmost", True)
    root.after(100, lambda: root.attributes("-topmost", False))
space_invader = r"""

    ############
    ####################
  ##########################
#######  ####  ####  ####  #########
 ############################
  ######    ####    ######
    ##                ##
"""
root.after(100, focus_window)
# Run the app
root.configure(background="gray")
label = tk.Label(root, text=space_invader, fg="lime",bg="black")
                                                
label.pack()
root.mainloop()