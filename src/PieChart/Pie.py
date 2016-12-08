from Tkinter import *

#this class will be responsible for building graphical objects and sending
#them to PieChart


def get_pie(window, screenfill):
        canvas_size = 500   #canvas should probably be square
        
        canvas = Canvas(window, width=canvas_size, height=canvas_size)
        canvas.pack()
        top = canvas_size*screenfill
        bottom = canvas_size* (1-screenfill)

        canvas.create_oval(top, top,
                           bottom, bottom,
                             fill='white', outline='black',
                                   width=1)
        return canvas

