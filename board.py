from pygame.locals import *
import pygame as pg
import math
from chess import screen, size, pad
from piece import *

class Board:
    def __init__(self, size):
        self.n = 8
        self.size = size
        self.squares = []
        self.sqrsize = (size[0]-2*pad)/self.n
        self.sel_piece = None 
        self.board_ = self.initialize_positions()
        self.font = pg.font.SysFont(None, 34)
        self.hit = (None, None, False)
        # init squares
        for x in range(self.n):
            for y in range(self.n):
                x_ = x*self.sqrsize + pad
                y_ = y*self.sqrsize + pad
                self.squares.append([Rect(x_, y_, self.sqrsize, self.sqrsize),x,y])
        

    def draw(self):
        self.draw_chequerboard(self.size)
        self.draw_pieces()
        
        for r in self.squares:
            if r[0].collidepoint(pg.mouse.get_pos()):
                pg.draw.circle(screen, (0, 0, 0, 20), r[0].center, self.sqrsize/2, width=2)

    def make_move(self, pos):
        cy = self.sel_piece["id"][0]
        cx = self.sel_piece["id"][1]
        sel_pos = (cx, cy)
        if pos != sel_pos:
            y = pos[0]
            x = pos[1]
            if self.board_[y][x]["piece"] is None:
                self.board_[y][x]["piece"] = self.board_[cy][cx]["piece"]
                self.sel_piece = None
                self.board_[cy][cx]["piece"] = None


    def draw_chequerboard(self, size):
        
        lttr = ["A","B","C","D","E","F","G","H"]
        sqrsize = 50 # size[0]/n 
        # pad = 40
        count = 0
        # draw board
        for x in range(self.n):
            for y in range(self.n):
                x_ = x*sqrsize
                y_ = y*sqrsize
                i = (x*8)+y
                if count%2==0:
                    col = (130, 190, 100)
                else:
                    col = (190, 130, 100)
                pg.draw.rect(screen, col, self.squares[i][0])
                count+=1
            count+=1
        # # draw side labels
        for y in range(self.n):
            # letters
            img = self.font.render(lttr[y], True, (255, 255, 255))
            screen.blit(img, (sqrsize*0.2, y*self.sqrsize + self.sqrsize*0.4 + pad))
            # numvers  
            img = self.font.render(str(y+1), True, (255, 255, 255))
            screen.blit(img, (y*self.sqrsize + self.sqrsize*0.4 + pad,self.sqrsize*0.2))

    def draw_pieces(self):
        for i in range(len(self.board_)):
            for j in range(len(self.board_)):
                idx = (i*8)+j
                if self.board_[i][j]["piece"] is not None:
                    self.board_[i][j]["piece"].draw(self.squares[idx][0].center, screen)
        
    def pprint(self):
        """ Pretty print board to prompt """
        b_ = [[0]*8 for _ in range (8)]
        for i in range(len(self.board_)):
            for j in range(len(self.board_)):
                if self.board_[i][j]["piece"] is not None:
                    b_[i][j]=self.board_[i][j]["piece"].colour[:1]+":"+self.board_[i][j]["piece"].piece_type.strip()[:1]
                else:
                    b_[i][j]='___'
            print(b_[i], "\n")

    def square_clicked(self, pos):
        for i, r in enumerate(self.squares):
            if r[0].collidepoint(pos):
                x = self.squares[i][1]
                y = self.squares[i][2]
                hitpos = (y, x)
                print("collision", y, x)
        if self.sel_piece is None:
            self.select_piece(hitpos)
            return
        self.make_move(hitpos)
                
    def select_piece(self, pos):
        y = pos[0]
        x = pos[1]            
        if self.board_[y][x]["piece"] is not None:
            # print(self.board_[y][x]["piece"].piece_type)
            # print(self.board_[y][x]["piece"].colour)
            # print("------")
            if self.sel_piece is not None:
                y_ = self.sel_piece["id"][1]
                x_ = self.sel_piece["id"][0]
                self.board_[y_][x_]["piece"].selected=False
            self.sel_piece = {
                "type": self.board_[y][x]["piece"].piece_type,
                "colour": self.board_[y][x]["piece"].colour,
                "id":(y,x)
            }
            self.board_[y][x]["piece"].selected=True
            return True
        else:
            return False


    def initialize_positions(self):
        """ Returns 2d array with either None values 
            or piece objects """
        letters = ["A","B","C","D","E","F","G","H"]
        out = []
        # for number in range(1,9):
        for i, letter in enumerate(letters):
            row = []
            # for letter in letters:
            for number in range(1,9):
                c=(i*8)+number
                p = None
                if number==2:
                    p = Pawn("White", [letter, number], self.sqrsize)
                if number==7:
                    p = Pawn("Black", [letter, number], self.sqrsize)
                # back pieces			
                if number==1:
                    # white back
                    if letter=="F" or letter =="C":
                        # make bishops
                        p = Bishop("White", [letter, number], self.sqrsize)
                    if letter=="B" or letter =="G":
                        # make knights
                        p = Knight("White", [letter, number], self.sqrsize)
                    if letter=="A" or letter =="H":
                        # make rooks
                        p = Rook("White", [letter, number], self.sqrsize)
                    if letter=="D":
                        p = Queen("White", [letter, number], self.sqrsize)
                    if letter=="E":
                        p = King("White", [letter, number], self.sqrsize)

                if number==8:
                    # black back
                    if letter=="F" or letter =="C":
                        # make bishops
                        p = Bishop("Black", [letter, number], self.sqrsize)
                    if letter=="B" or letter =="G":
                        # make knights
                        p = Knight("Black", [letter, number], self.sqrsize)
                    if letter=="A" or letter =="H":
                        # make rooks
                        p = Rook("Black", [letter, number], self.sqrsize)
                    if letter=="D":
                        p = Queen("Black", [letter, number], self.sqrsize)
                    if letter=="E":
                        p = King("Black", [letter, number], self.sqrsize)

                # row.append(p)
                s = {
                    "letter": letter,
                    "number": number,
                    "piece": p,
                    "code":c
                }
                # print(c)
                row.append(s)
                # codes.append(c)
            out.append(row)
        print(out)
        return out
