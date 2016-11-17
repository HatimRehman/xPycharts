from Tkinter import *
from Pie import *
import random


class PieChart:

        def __init__(self, data=None):
                self.data = clean_data(data) if data is not None else None
                      
                self.master = Tk()
                self.master.resizable(0,0)
                self.master.title("PieGraph")  #eventually set by user

                self.pie = get_pie(self.master)
                self.canvas_size = int(self.pie.cget("height"))
                self.current_percent = 0      #will go around the pie, making slices


        def getSlice(self, percent, color=None):
                #get a random three bit hexadecimal number.
                #n/4096 chance of printing same number, shouldn't be a problem.
                if color == None:
                        color = self.genColor()
                
                self.pie.create_arc(self.canvas_size/4, self.canvas_size/4,
                                    self.canvas_size*3/4, self.canvas_size*3/4,
                                    outline='black', 
                                    start=self.current_percent*360,
                                    extent=percent*360,
                                    style=PIESLICE,
                                    fill=color)
                self.current_percent += percent

        def genColor(self):
                color = "#%03x" % random.randint(0, 0xFFF)
                return color


if __name__ == '__main__':
        PieChart = PieChart()
        PieChart.getSlice(0.10)
        PieChart.getSlice(0.60)
        PieChart.getSlice(0.30)
        mainloop()
