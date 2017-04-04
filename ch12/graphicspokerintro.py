# graphicspoker.py
from classDice import Dice
from classPokerApp import PokerApp
from classTextInterface import TextInterface
from classGraphicsInterface import GraphicsInterface

def main():
	win = GraphWin()
	intro = Text(
	inter = TextInterface()
	app = PokerApp(inter)
	app.run()

main()

