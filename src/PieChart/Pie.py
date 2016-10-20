from Tkinter import *

#this class will be responsible for building graphical objects and sending
#them to PieChart


def get_pie(window):
        canvas_size = 500   #canvas should probably be square
        
        canvas = Canvas(window, width=canvas_size, height=canvas_size)
        canvas.pack()

        canvas.create_oval(canvas_size/4, canvas_size/4,
                           canvas_size*3/4, canvas_size*3/4,
                             fill='white', outline='black',
                                   width=1)
        return canvas

