from tkinter import Button, Label
import random
import variables
import sys
import ctypes

class Cell:
    all = []
    cell_count_label_object = None
    cell_count = variables.CELLCOUNT
    def __init__(self, x, y, is_mine = False, is_open = False):
        self.is_mine = is_mine
        self.is_open = is_open
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=""
        )
        btn.bind('<Button-1>', self.left_click)
        btn.bind('<Button-3>', self.right_click)
        self.cell_btn_object = btn                  # Assigning a button object to each button
    
    @staticmethod
    def create_cell_countobject(location):
        lbl =  Label(
            location,
            font=("", 24),
            bg="black",
            fg="white",
            text=f"Cells Left: {Cell.cell_count}"
        )
        Cell.cell_count_label_object = lbl
        return lbl

    def left_click(self, event):
        if self.is_mine:
            self.cell_btn_object.configure(bg='red')
            sys.exit()
        else:
            if self.surrounding_mines_length == 0:
                for tile in self.surrounding_titles:
                    tile.show_cell
            self.show_cell

        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')
            
    def right_click(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg="yellow"
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg="SystemButtonFace"
            )
            self.is_mine_candidate = False

    def getcell(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
        return None
            
    @property
    def show_cell(self):
        if not self.is_open:
            self.cell_btn_object.configure(
                text=self.surrounding_mines_length,
                bg="white"
            )
            Cell.cell_count -= 1
            if Cell.cell_count == variables.MINESCOUNT:
                print("You Won!!")
                sys.exit()

            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}"
                )
        # Mark the cell opened as true
        self.is_open = True
        
    @property
    def surrounding_titles(self):
        tiles_seleceted = []
        for i in range(-1,2):
            for j in range(-1,2):
                x = self.x + i
                y = self.y + j
                if x < 0 or y < 0 or x > variables.GRIDSIZE - 1 or y > variables.GRIDSIZE - 1:
                    continue
                if self.x == x and self.y == y:
                    continue
                cell = self.getcell(x, y)
                tiles_seleceted.append(cell)
        
        return tiles_seleceted
    
    @property
    def surrounding_mines_length(self):
        tiles = self.surrounding_titles
        count = 0
        for tile in tiles:
            if tile.is_mine:
                count +=1
        return count
        
    @staticmethod
    def randomizemines():
        picked_titles = random.sample(Cell.all, 9)
        for picked_title in picked_titles:
            picked_title.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
    
