"""
github.com/alonzi (datascientist@virginia.edu)
class definition for the mission
2021-02-03
github.com/alonzi/currahee
this class is generator of a mission
"""

import chess
import chess.svg
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import squad as sq
import orders as ord

import numpy as np

class cl_mission:

    def addTerrain(self):
        for j in range(3):
            for i in range (np.random.randint(1,6)):
                sq = np.random.randint(64)
                self.board.set_piece_at(square=sq,piece=chess.Piece(piece_type=chess.ROOK,color=chess.BLACK))

    def showFriendlies(self,squads):
        for squad in squads:
            sq = squad.location[1]*8+squad.location[0]
            self.board.set_piece_at(square=sq , piece=chess.Piece(piece_type=chess.PAWN,color=chess.BLACK))
        tmp = chess.svg.board(self.board,size=350)
        with open("tmp.svg", "w") as text_file:
            print("{}".format(tmp), file=text_file)
        drawing = svg2rlg("tmp.svg")
        renderPDF.drawToFile(drawing, "tmp.pdf")
        renderPM.drawToFile(drawing, "tmp.png", fmt="PNG")
        img = mpimg.imread("tmp.png")
        plt.imshow(img)
        plt.show()
        return True

    def showFoes(self,squads):
        for squad in squads:
            sq = squad.location[1]*8+squad.location[0]
            self.board.set_piece_at(square=sq , piece=chess.Piece(piece_type=chess.PAWN,color=chess.WHITE))
        tmp = chess.svg.board(self.board,size=350)
        with open("tmp.svg", "w") as text_file:
            print("{}".format(tmp), file=text_file)
        drawing = svg2rlg("tmp.svg")
        renderPDF.drawToFile(drawing, "tmp.pdf")
        renderPM.drawToFile(drawing, "tmp.png", fmt="PNG")
        img = mpimg.imread("tmp.png")
        plt.imshow(img)
        plt.show()
        return True

    def __init__(self,company,type="assault"):
        self.type = str(type)    # instance variable unique to each instance
        print("\n----> Your mission is to {}.".format(self.type))
        company.setOrders(ord.cl_orders())

        # mission briefing from Battalion CO
        # create enemy squads
        self.enemy_squads = []
        self.enemy_squads.append(sq.cl_squad(PVT=4))
        for squad in self.enemy_squads:
            squad.setLocation(6,6)

        # create empty battlefield
        self.board = chess.Board(fen=None)

        # add terrain
        self.addTerrain()



    def __del__(self):
        # debrief from Battalion CO
        print("\n----> {} MISSION ACCOMPLISHED.".format(self.type))
        


"""


# https://python-chess.readthedocs.io/en/latest/
# https://python-chess.readthedocs.io/en/latest/svg.html

"""