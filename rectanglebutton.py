# button class example

from graphics import *


class RectangleButton:


    def __init__(self, center, width, height, text):
        w, h = width / 2.0, height / 2.0
        self.xmin, self.xmax = center.getX() - w, center.getX() + w
        self.ymin, self.ymax = center.getY() - h, center.getY() + h
        self.rect = Rectangle(Point(self.xmin, self.ymin), 
                                Point(self.xmax, self.ymax))
        self.text = Text(center, text)
        self.deactivate()


    def draw(self, window):
        self.rect.draw(window)
        self.text.draw(window)


    def get_label(self):
        return self.text.getText()


    def clicked(self, p):
        return (self.active and self.xmin <= p.getX() <= self.xmax and 
                self.ymin <= p.getY() <= self.ymax)


    def deactivate(self):
        self.text.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False


    def activate(self):
        self.text.setFill('black')
        self.rect.setWidth(2)
        self.active = True
