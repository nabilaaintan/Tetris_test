import pygame
from colors import Colors
class Grid:
    def __init__(self):
        self.num_rows =20
        self.num_cols = 10
        self.cell_size =20
        self.grid = [[0 for j in range(self.num_cols)] for i in range (self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
          for row in range(self.num_rows):
                for column in range(self.num_cols):
                    print (self.grid[row][column], end =" ")
                print()

    def is_inside(self, row, column):
          if row >= 0 and row < self.num_rows and column >= 0  and column <self.num_cols:
                return True
          return False 
    
    def is_empty(self,row, column):
         if self.grid[row][column] == 0:
              return True
         return False
    
    def is_row_full(self, row):
         for column in range(self.num_cols):
               if self.grid[row] [column] == 0:
                 return False
         return True
    
    def clear_row(self, row):
         for column in range(self.num_cols):
              self.grid[row][column] = 0


    def move_row_down(self, start_row, num_rows):
         for row in range(start_row,-1,-1):
          for column in range(self.num_cols):
              self.grid[row+num_rows][column] = self.grid[row][column]
              self.grid[row][column] = 0


    def clear_full_rows(self):
         completed = 0
         for row in range(self.num_rows-1, -1, -1):
            if self.is_row_full(row):
                   self.clear_row(row)
                   completed += 1
            elif completed > 0 :
                   self.move_row_down(row, completed)

         return completed
    
    def reset(self):
         for row in range(self.num_rows):
              for column in range(self.num_cols):
                   self.grid[row][column] = 0
         
    
    def draw(self, screen, x_offset=10, y_offset=60):
     #     x_offset = 10
     #     y_offset = 10
         for row in range(self.num_rows):
              for column in range(self.num_cols):
                   cell_value = self.grid[row][column]
                   cell_rect  = pygame.Rect( column*self.cell_size + x_offset, row*self.cell_size + y_offset, self.cell_size -1, self.cell_size -1)
                   pygame.draw.rect(screen, self.colors[cell_value], cell_rect)