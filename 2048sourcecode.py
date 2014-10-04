"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    linelist1 = list(line);
    linelist2 = sorter(linelist1);
    line = merger(linelist2);
    return line


def sorter(linelist):
    """ A function to separate all the non-zero and zero tiles"""
    for dummy_row in range(len(linelist)-1):
        for idx in range(len(linelist)):
            if linelist[idx]==0 and idx<len(linelist)-1:
                temp=linelist[idx];
                linelist[idx]=linelist[idx+1];
                linelist[idx+1]=temp;   
    return linelist;


def merger(linelist2):
    """A function to merge sorted list"""
    linelist = linelist2;
    for idx in range(len(linelist)-1):
        if linelist[idx]==linelist[idx+1]:
            linelist[idx]+=linelist[idx+1];
            linelist[idx+1]=0;
    linelistx=sorter(linelist);
    return linelistx;


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """ Getting the dimenstions of grid"""
        self.height = grid_height;
        self.width = grid_width;
        self.grid =[];
        self.grid = [[0 for dummy_row in range(self.width)] for dummy_col in range(self.height)];
        
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.grid = [[0 for dummy_row in range(self.width)] for dummy_col in range(self.height)];
       
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.grid);
    
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height;
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.width;
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add a new tile if any tiles moved."""
        
        initial = str(self.grid);
        if direction == UP:
           for idx in range(self.width):
                temp=[];
                for xii in range(self.height):
                    temp.append(self.grid[xii][idx]);
                mergedlist = merge(temp);
                for kii in range(len(mergedlist)):
                    self.grid[kii][idx]=mergedlist[kii];
        elif direction == DOWN:
            for idx in range(self.width):
                temp=[];
                for xii in range(self.height):
                    temp.append(self.grid[xii][idx]);
                reverselist = temp;
                reverselist.reverse();
                mergedlist = merge(reverselist);
                mergedlist.reverse();
                for kii in range(len(mergedlist)):
                    self.grid[kii][idx]= mergedlist[kii];
        elif direction == LEFT:
            for idx in range(self.height):
                temp=[];
                for xii in range(self.width):
                    temp.append(self.grid[idx][xii]);
                mergedlist = merge(temp);
                for kii in range(len(mergedlist)):
                    self.grid[idx][kii] = mergedlist[kii];
        elif direction == RIGHT:
            for idx in range(self.height):
                temp = [];
                for xii in range(self.width):
                    temp.append(self.grid[idx][xii]);
                reverselist = temp;
                reverselist.reverse();
                mergedlist = merge(reverselist);
                mergedlist.reverse();
                for kii in range(len(mergedlist)):
                    self.grid[idx][kii] = mergedlist[kii];
              
        final = str(self.grid);
        if initial != final:
            self.new_tile();
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        if 0 in [self.grid[idx][xii] for idx in range(self.height) for xii in range(self.width)]:
           while(1):
                row = random.randint(0,self.height-1);
                col = random.randint(0,self.width-1);
                mylist=[2,2,2,2,2,2,2,2,2,4];
                mychoice = random.choice(mylist);
                if self.grid[row][col] == 0:
                    self.grid[row][col] = mychoice;
                    break;
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """  
        self.grid[row][col] = value;

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self.grid[row][col];
 
    
poc_2048_gui.run_gui(TwentyFortyEight(4,4));
