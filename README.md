# MineSweeper Game
## Description
This is a basic **2D game** called MineSweeper made using **Python** and for UI I have used **Tkinter** library.

### Objective
The objective of the game is to open all the tiles/cells without hitting any of the hidden mines beneath random cells/tiles in a 6x6 grid.

### Video Demo
[Link to youtube video](https://youtu.be/mkoEx5Zn8CU)
## Explanation Of Files
### minesweepper.py
This is the **main file** of the project.<br>

Here at start I have initialised the `Tk()` function and at last `mainloop()` function imported from the **tkinter library**, it creates a window for the project in which I can configure our UI and runs the window using mainloop. Whole logic of the game is written between these functions only.

Next I have assigned some properties to our window and created three frames i.e. `top_frame, left_frame(), center_frame()` in which different functionalites of my game will be shown and a `game_label` which contains the logo my game

- In **top_frame** I will be showing the logo or name of our game.
- In **left_frame** I will be showing the number of cells/tiles left which can be clicked. 
>Later on I have thought of adding some dynamic features to this game like difficulity level which would increase or decrease the number of mines accordingly and also adding a range in which the player wants it grid to be such as if he wants it to be of 5x5 or 6x6 or some other number.
- In **center_frame** we have added the tiles/cells to the which are clickable.  

All the frames and label are then placed on the window using `place()` function.

After that I written a `nested for loop` which is creating the grid of the game where eventually cells/titles will be palced which are instances of `class Cell`.
In the loop itself I have assigned the coordinates for each cell which would help in writing the further game logic.

Then I have called `randomizemines()` function which is a static method of Class Cell which assigns mines to 9 random tiles/cells.

Then to display the number of clickable tiles I have called the `create_cell_countobject()` Which is also a static method of class Cell, it helps in displaying the cells left.

Then the above created object is displayed on the left_frame.

### cell.py
In this file we have created a Class named **Cell** which contains all the logic of how the cells work.

It has three variables named **all** which is a list containg information about the whole grid or all of the cells, **cell_count_label_object** which as the name says is label object of number of cells left, and cell_count which contains the total number of cells.

`__init__(self, x, y, is_mine = False, is_open = False)` **Constructor** which initalises an instance and assigns the following values:
- `is_mine`: False(default value) whether it is a mine or not
- `is_open`: False(default value) whether the tile has been opened or not
- `is_mine_candidate`: False(default value) whether the tile is opted for possible mine or not.
- `cell_btn_object`: None
- `x` and `y` coordinates

`create_btn_object(self, location)` function as the name says it creates a button object for each tile and uses the `bind()` fucntion to bind the left and right click of mouse to the tile.

`create_cell_countobject(location)` function creates the label object for displaying the number of cells left

`left_click(self)` function has a if else condition it checks if the clicked tile is mine or not. 
- If it is a mine then that tiles color is changed to red and the player is made to exit the game.
- Else we check if none of the surrounding tiles for the current tile are mine then the code will also display the number of mines around those tiles and if this is not the case then the code will only show the number of mines around the current tile clicked.

After the above logic has been executed I have unbind the click function for the clicked tile so that there is no uncessary execution of code.

`right_click(self)` function has also a if else condition it basically checks if the clicked mine is selected probable candidate or not by the player. If the tile is not a candidate then it is made to be and the color of the tile is changed to yellow or vice versa.

`get_cell(self, x, y)` function the returns the cell whose coordinates are sent as arguments.

`show_cell(self)` function first of all checks if the seleted tile is opened or not. If not then shows the number of mines around the current tile and then checks if we have won the game for which the condition is to have equal number of clickable tiles left and count of mines. It also updates the cell count variable everytime the function is called.

`surrounding_titles(self)` function interates through the surrounding tiles of the current selected tiles and return the list of those tiles after rejecting the outside grid case and also not including the current tile which was clicked.

`surrounding_mines_length(self)` this function simply returns the count of mines from the list it got from surrounding_tiles function. 

`randomizemines()` function picks random tiles which in turn becomes mines.

### util.py
It contains helper functions

`height_per(per)` returns heigth w.r.t. percentage.

`width_per(per)` returns width w.r.t. percentage.

### variables.py
This file has all the important variables which are used globally. 

> For now GRIDSIZE and MINESCOUNT are hardcoded but I will be making them dynamic in near future. 

WIDTH = 1440
HEIGHT = 720
GRIDSIZE = 6
CELLCOUNT = GRIDSIZE **2
MINESCOUNT = CELLCOUNT // 4



