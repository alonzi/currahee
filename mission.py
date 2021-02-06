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

class cl_mission:

    def showFriendlies(self,squads):
        board = chess.Board("8/8/8/8/4N3/8/8/8 w - - 0 1")
        squares = board.attacks(chess.E4)
        tmp = chess.svg.board(board, squares=squares, size=350)
        with open("tmp.svg", "w") as text_file:
            print("{}".format(tmp), file=text_file)
        drawing = svg2rlg("tmp.svg")
        renderPDF.drawToFile(drawing, "tmp.pdf")
        renderPM.drawToFile(drawing, "tmp.png", fmt="PNG")
        img = mpimg.imread("tmp.png")
        plt.imshow(img)
        plt.show()
        return True

    def showFoes(self):
        return True

    def __init__(self,company,type="assault"):
        self.type = str(type)    # instance variable unique to each instance
        print("\n----> Your mission is to {}.".format(self.type))
        company.setOrders(type)

        # mission briefing from Battalion CO
        # create enemy squads
        self.enemy_squads = []

    def __del__(self):
        # debrief from Battalion CO
        print("\n----> {} MISSION ACCOMPLISHED.".format(self.type))
        


"""


# https://python-chess.readthedocs.io/en/latest/
# https://python-chess.readthedocs.io/en/latest/svg.html

"""