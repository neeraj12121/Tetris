import os
import random


class Game(object):
     Game_shape=('straight','square','N','L','7')
     Game_shape_map={
         Game_shape[0]:[[1,1,1,1]],
         
         Game_shape[1]:[[1,1],
                        [1,1]],
         
         Game_shape[2]:[[0,1],
                        [1,1],
                        [1,0]],
         
         Game_shape[3]:[[1,0],
                        [1,0],
                        [1,1]],
         
         Game_shape[4]:[[0,1],
                        [0,1],
                        [1,1]]
         }

     brd=[]
     next_shape=None

     def __init__(self, brdSize):
         
         self.brdSize=brdSize
         self.Board()

     def Board(self):
         
         for i in range(self.brdSize):
             self.brd.append([])
             for j in range(self.brdSize):
                 if (j==0) or (j==self.brdSize-1) or (i==self.brdSize-1):
                     self.brd[i].append(1)
                 else:
                     self.brd[i].append(0)
                     
     def ShowBrd(self):
         for i in range(self.brdSize):
             for j in range(self.brdSize):
                 if self.brd[i][j]==1:
                     print('@',end='')
                 else:
                     print(' ',end='')
             print('')


     def RL(self):
         _next_shape=[]
         x=lambda y:list(y)
         z=zip(*self.next_shape[::-1])
         for i in  z:
              x=i
              a=list(x)
              _next_shape.append(a)
         if Game.is_valid(self.brdSize,self.left,_next_shape):
             self.next_shape=_next_shape

     def RR(self):
         _next_shape=[]
         x=lambda y:list(y)
         z=zip(*self.next_shape[::-1])
         for i in  z:
                x=i
                a=list(x)
                _next_shape.append(a)
         if Game.is_valid(self.brdSize,self.left,_next_shape):
             self.next_shape=_next_shape
     def MR(self):
        if Game.is_valid(self.brdSize, self.left + 1, self.next_shape):
            self.left +=1

     def ML(self):
         if Game.is_valid(self.brdSize, self.left - 1, self.next_shape):
             self.left -=1

     def GetNextShape(self):
         self.next_shape = self.Game_shape_map[self.Game_shape[random.randint(0,len(self.Game_shape)-1)]]
         width = Game.GetWidthOfShape(self.next_shape)
         self.left = (self.brdSize - width)//2


     def ShowNextShape(self):
         shape_length = len(self.next_shape)
         for i in range(shape_length):
             for j in range(self.left):
                 print (' ',end='')
             for k in self.next_shape[i]:
                 if k == 1:
                     print('*',end='')
                 else:
                     print(' ',end='')
             print('')



     def run(self, input_str):
         Key_actions = {'a': self.ML,'d': self.MR,'w': self.RL,'s': self.RR,'f': self.UpdateBrd}
         if input_str in Key_actions.keys():
             return Key_actions[input_str]
          
     @staticmethod
     def is_valid(brdSize, left, shape):
         width = Game.GetWidthOfShape(shape)
         if (left <= brdSize - width - 1) and (left >= 1):
             return True
         return False
     
     @staticmethod
     def GetWidthOfShape(shape):
         a=0
         for i in zip(*shape):
             if sum(i)>=1:
                 a+=1
         return a


     def GetAppropriateRow(self):
         width = Game.GetWidthOfShape(self.next_shape)
         height = len(self.next_shape)
         row_index = self.brdSize - 1
         while(row_index >= height):
             sub_board = self.brd[row_index - height:row_index]
             for i in range(len(self.next_shape)):
                 if 2 in [x + y for x, y in zip(self.next_shape[i], sub_board[i][self.left:self.left+width])]:
                     break
             else:
                 return row_index
             row_index -= 1
         return False



     def UpdateBrd(self):
         width = Game.GetWidthOfShape(self.next_shape)
         row = self.GetAppropriateRow()
         if row:
             for shape_row in self.next_shape[::-1]:
                 row -= 1
                 self.brd[row][self.left:self.left+width] = [x + y for x, y in zip(shape_row, self.brd[row][self.left:self.left+width])]
             self.ShowBrd()
             return True
         else:
             return False         
         

def Tetris():
    Game_obj=Game(12)
    _next_move=None
    is_continue=True
    while True:
        Game_obj.GetNextShape()
        while True:
            os.system('cls')
            print("\n\n#############  --------GAME OF TETRIS-----------  ############\n\n")
            Game_obj.ShowNextShape()
            print("\n\n")
            Game_obj.ShowBrd()
            print("----Instructions----")
            print("a - Move left")
            print("d - Move right")
            print("w - Rotate left")
            print("s - Rotate right")
            print("f - Fix the shape into the board")
            print("q - Quit the game in between")
            
            _next_move = input('Enter ::::------').lower()
            if _next_move=='q':
                break

            valid_move=Game_obj.run(_next_move)
            if valid_move:
                is_continue=valid_move()

            if _next_move=='f':
                break
        if _next_move=='q':
            is_quit=input('Are You Sure You Want To QUIT (y or n) ').lower()
            if is_quit=='y':
                break
        if not is_continue:
            print("Play It ON")
            break


if __name__ == '__main__':
    Tetris()
