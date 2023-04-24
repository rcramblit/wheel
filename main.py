import random
import time
from tkinter import *
from tkinter.ttk import *


WIDTH = HEIGHT = 1000
RADIUS = (WIDTH * .9)/2
# Points defining the corners of a rectangle containing a circle, from which the circular arcs are sliced
# https://tkinter-docs.readthedocs.io/en/latest/widgets/canvas.html#Canvas.create_arc
X0 = Y1 = (1/9) * RADIUS
X1 = Y0 = (19/9) * RADIUS


# Number of degrees to rotate each step
STEP = .5
SLEEP = 1/120

def color_spectrum(start_color, end_color, steps):
    """Takes two hex color values and returns a range of colors between them."""
    r_start, g_start, b_start = [int(start_color.replace("#", "")[i:i+2], 16) for i in (0, 2, 4)]
    r_end, g_end, b_end = [int(end_color.replace("#", "")[i:i+2], 16) for i in (0, 2, 4)]

    for step in range(steps + 1):
        r = int(r_start + (r_end - r_start) * step / steps)
        g = int(g_start + (g_end - g_start) * step / steps)
        b = int(b_start + (b_end - b_start) * step / steps)
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        yield hex_color

start_color = "#21C310"
end_color = "#B210C3"
NUM_WEDGES = 200
colors = [color for color in color_spectrum(start_color, end_color, int(NUM_WEDGES/2))]
colors.extend(reversed(colors))
random.shuffle(colors)

# Proportion of full circle each wedge takes
EXTENT = 360 / NUM_WEDGES

root = Tk()
root.title("Random Wheel")
root.geometry(f"{WIDTH}x{HEIGHT}")



canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.delete("all")

def draw_wedge(canvas, start, color):
    canvas.create_arc(X0, Y0, X1, Y1, extent=EXTENT, start=start, fill=color)

def main():
    offset = 0
    rotations = 0
    canvas.create_text(X0, Y1, text = rotations, fill = "black")
    while True:
        print(offset, rotations)
        canvas.delete("all")
        if offset == 360:
            offset = 0
            rotations += 1
        rotations_decimal = str(offset/360).lstrip("0.")[0:2]
        canvas.create_text(X0, Y1, text = f"{rotations}.{rotations_decimal}", fill = "black")
        canvas.pack()
        offset += STEP
        wedge_start = offset
        for i in range(0, len(colors)):
            color = colors[i]
            draw_wedge(canvas, wedge_start, color)
            wedge_start += EXTENT
        canvas.update()
        time.sleep(SLEEP)
    
    
    

canvas.pack()


root.after(0, main)
root.mainloop()