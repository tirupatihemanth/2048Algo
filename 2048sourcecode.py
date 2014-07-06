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
    lineList1 = list(line);
    lineList2 = sorter(lineList1);
    line = merger(lineList2);
    return line


def sorter(lineList):
    """ A function to separate all the non-zero and zero tiles"""
    for x in range(len(lineList)-1):
        for idx in range(len(lineList)):
            if lineList[idx]==0 and idx<len(lineList)-1:
                temp=lineList[idx];
                lineList[idx]=lineList[idx+1];
                lineList[idx+1]=temp;    
    return lineList;


def merger(lineList2):
    """A function to merge sorted list"""
    lineList = lineList2;
    for idx in range(len(lineList)-1):
        if lineList[idx]==lineList[idx+1]:
            lineList[idx]+=lineList[idx+1];
            lineList[idx+1]=0;
    lineListx=sorter(lineList);
    return lineListx;


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """ Getting the dimenstions of grid"""
        self.height = grid_height;
        self.width = grid_width;
        self.grid =[];
        self.row=[];
        leftList = [];
        rightList = [];
        upList = [];
        downList = [];
        for idx in range(self.width):
           upList.append((0,idx));
        for idx in range(self.width):
           downList.append((self.height-1,idx));
        for idx in range(self.height):
           leftList.append((idx,0));
        for idx in range(self.height):
           rightList.append((idx,self.width-1));
        self.library = {UP:upList,
                   DOWN:downList,
                   RIGHT:rightList,
                   LEFT:leftList};
        pass
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.grid =[];
        self.row = [];
        for x in range(self.width):
            self.row.append(0);
        for idx in range(self.height):
            self.grid.append(self.row);
        pass
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(grid);
        pass

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
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        
        pass
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        row = random.randint(0,self.height-1);
        col = random.randint(0,self.width-1);
        myList=[2,2,2,2,2,2,2,2,2,4];
        myChoice = random.choice(myList);
        if self.grid[row][col] == 0:
           self.grid[row][col]=myChoice;
        pass
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """  
        self.grid[row][col]=value;
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        # replace with your code
        return self.grid[row][col];
 
    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4));
