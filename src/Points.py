class Points():


    def __init__(self,xval,yval):
        self.x=xval
        self.y=yval
        self.checkL=False
        self.checklen()
        self.checkT=False
        self.checktype()

        if (self.checkL==False):
            print ("There must be an equal number of x and y values")

        if (self.checkT==False):
            print ("All values for the co-ordinate pairs must be integers or floats")
        else:
            self.ndict= dict([(self.x[i],self.y[i])for i in range(len (self.x))])

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
a = Points(m,n)
