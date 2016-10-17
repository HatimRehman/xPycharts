class Points():


    def __init__(self,data):
        self.x=[ x[0] for x in data  ]
        self.y=[ y[1] for y in data  ]
        self.mylist=[]
        self.checkL=False
        self.checklen()
        self.checkT=False
        self.checktype()

        if (self.checkL==False):
            print ("There must be an equal number of x and y values")

        if (self.checkT==False):
            print ("All values for the co-ordinate pairs must be integers or floats")
        else:
           for i in range (len(self.x)):
               d = {"x": self.x[i], "y": self.y[i]}
               self.mylist.append(d)
            
    def checklen(self):
        if len(self.x)==len(self.y):
            self.checkL=True

    def checktype(self):
        for value in self.x:
            if type (value) != int and type (value) != float:
                return
        for value in self.y:
            if type (value) != int and type (value) != float:
                return
        self.checkT=True
        return


m= [1,2,3,4]
n= [6,7,8,9]

l = [(2,3), (3,4), (5,6) ]   
a = Points(l)
print(a.mylist)
