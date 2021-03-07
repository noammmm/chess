import pygame as pg
import sys, copy
from piece import *
from player import *
from board import *

size = wwidth, wheight=  880, 880
pad = 40
squaresize = size[0] - (2*pad)//8
screen = pg.display.set_mode(size)


if __name__ == "__main__":
    chess_print = """ 
         _______  __   __  _______  _______  _______ 
        |       ||  | |  ||       ||       ||       |
        |       ||  |_|  ||    ___||  _____||  _____|
        |       ||       ||   |___ | |_____ | |_____ 
        |      _||       ||    ___||_____  ||_____  |
        |     |_ |   _   ||   |___  _____| | _____| |
        |_______||__| |__||_______||_______||_______|"""
    # print(chess_print, "\n")
    pg.init()

    green = (118, 150, 85)
    # print
    # Create chess board
    board = Board(size)

    # board.pprint()
    # print(board.board_)
    # for i in board.board_:
    #     print(i, "\n")

    # pprint(board.pos)
    board.pprint()
    # print(type(board.pos))
    # sys.exit()

    player1 = Player("Alice", "White", board)

    ## Main loop ## 
    while 1:
        screen.fill(green)
        board.draw()

        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                board.square_clicked(pg.mouse.get_pos())
        
        pg.display.update()