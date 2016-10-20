from Tkinter import *
from Pie import *


class PieChart:

        def __init__(self, data=None):
                self.data = clean_data(data) if data is not None else None
                
                
                self.master = Tk()
                self.master.resizable(0,0)
                self.master.title("PieGraph")  #eventually set by user

                self.pie = get_pie(self.master)
                self.canvas_size = int(self.pie.cget("height"))
                self.current_angle = 0                  #will go around the pie, making slices


        def getSlice(self, angle, filler='white'):
                self.pie.create_arc(self.canvas_size/4, self.canvas_size/4,
                                    self.canvas_size*3/4, self.canvas_size*3/4,
                                    outline='black', 
                                    start=self.current_angle,
                                    extent=angle,
                                    style=PIESLICE)
                self.current_angle += angle






if __name__ == '__main__':
        PieChart = PieChart()
        PieChart.getSlice(90)
        PieChart.getSlice(45)
        mainloop()
