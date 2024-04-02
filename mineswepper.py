from tkinter import *;
import variables
import util
from cell import Cell

# Make the game dynamic in sense add difficulty levels and grid size
# Add mines_count formula => (grid_size ** 2) // 4
# Add flask to make a website out of this game
# Try and add database
# Deploy the whole thing somewhere so that everybody can access this  

root = Tk()

root.configure(bg="black")
root.title("mineswpper")
root.geometry(f'{variables.WIDTH}x{variables.HEIGHT}')
root.resizable(False, False)   

top_frame = Frame(
    root,
    bg = 'black',
    width = util.width_per(100),
    height = util.height_per(25)
)

left_frame = Frame(
    root,
    bg = 'black',
    width = util.width_per(25),
    height = util.height_per(75)
)

center_frame = Frame(
    root,
    bg = 'black',
    width = util.width_per(75),
    height = util.height_per(75)
)

top_frame.place(
    x = util.width_per(0),
    y = util.height_per(0)
)

left_frame.place(
    x = util.width_per(0),
    y = util.height_per(25)
)

center_frame.place(
    x = util.width_per(25),
    y = util.height_per(25)
)

game_label = Label(
    top_frame,
    bg="black",
    fg="white",
    font=("", 48),
    text="MineSweeper"
)

game_label.place(
    x = util.width_per(35),
    y = util.height_per(5)
)

for i in range(variables.GRIDSIZE):              # Make the grid size dynamic afterwards
    for j in range(variables.GRIDSIZE):
        c = Cell(i, j)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            row = i,
            column = j
        )

Cell.randomizemines()                           # Make the difficulty dynamic as well

cellLeft = Cell.create_cell_countobject(left_frame)

cellLeft.place(
    x = util.width_per(5),
    y = util.height_per(30)
)

root.mainloop()