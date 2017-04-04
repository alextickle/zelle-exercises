# dieview2.py
from graphics import *
class DieView:
    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
        d1 = DieView(myWin, Point(40,50), 20) 
        creates a die centered at (40,50) having sides
        of length 20"""
        
        self.win = win
        self.background = "white"
        self.foreground = "black"
        self.psize = 0.1 * size
        hsize = size / 2.0
        offset = 0.6 * hsize
        
        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)
        
        # create 7 circles for standard pip locations
        self.pips = [self.makePip(cx-offset, cy-offset),
                    self.makePip(cx-offset, cy),
                    self.makePip(cx-offset, cy+offset),
                    self.makePip(cx, cy),
                    self.makePip(cx+offset, cy-offset),
                    self.makePip(cx+offset, cy),
                    self.makePip(cx+offset, cy+offset),]
        
        # create a table for which pips are on for each value
        self.onTable = [ [], [3], [2,4], [2,3,4], [0,2,4,6], [0,2,3,4,6], [0,1,2,4,5,6]]
        self.setValue(1)
        
    def __makePip(self, x, y):
        """Draws a pip at (x,y)""""
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip
    
    def setValue(self.value):
        """Sets this die to display value"""
        # turn all the pips off
        for pip in self.pips:
            pip.setFill(self.background)
        # turn the appropriate pips back on
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)