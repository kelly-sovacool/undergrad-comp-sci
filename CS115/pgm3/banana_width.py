from graphics import *
def main():
    win = GraphWin('',500,500)
    gif = Image(Point(250,250), 'banana.gif')
    gif.draw(win)
    width = gif.getWidth()
    textwid = Text(Point(250, 100), 'banana width = ' + str(width))
    textwid.draw(win)
    height = gif.getHeight()
    texthei = Text(Point(250,150), 'banana height = ' + str(height))
    texthei.draw(win)
    win.getMouse()
    win.close()
main()