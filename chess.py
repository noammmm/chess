import pygame as pg
import sys, copy
from helpers import *
from piece import *
from player import *
from board import *

size = wwidth, wheight=  480, 480
pad = 40
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
    board = Board(initialize_positions(), size)

    # board.pprint()
    # print(board.board_)
    # for i in board.board_:
    #     print(i, "\n")

    # pprint(board.pos)
    
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
                board.piece_hit(pg.mouse.get_pos())
        
        pg.display.update()