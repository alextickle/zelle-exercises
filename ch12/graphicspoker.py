# graphicspoker.py
from classDice import Dice
from classPokerApp import PokerApp
from classTextInterface import TextInterface
from classGraphicsInterface import GraphicsInterface

def main():
	inter = TextInterface()
	app = PokerApp(inter)
	app.run()

main()

