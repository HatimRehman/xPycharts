import numpy as np
 
 
def LagrangeInterp(data, x):
    #Number of data points
    n=len(data)
    #Number of x points
    nx = len(x)
 
    #Parse x, y data points

 
    #Allocate space for L(x)
    L = [0.0]*(nx)
 
    def b(j,xi):
        """Calculate b_j(x_xi)"""
        v = 1.0
        for k in xrange(n):
            if k != j:
                v *= (xi-dx[k]) / (dx[j]-dx[k])
        return v
 
    #Construct L(x)
    for i,xi in enumerate(x):
        #Construct each element of L(x)
        for j in xrange(n):
            L[i] += dy[j]*b(j,xi)
           
    return L


def Lagrange(x):
	
	dx = [d['x'] for d in data]
    dy = [d['y'] for d in data]
    
	def b(x):
		v = 1.0
		for k in range(1,x):
			if k != x:
				try:
					v *= (x-dx[k]) / (dx[j]-dx[k])
				except:
					pass
		return v

    #Construct L(x)
    fx = 0 
    for coord in coords:
    		x, y = coord['x'], coord['y']
            fx += y*b(x)


if '__main__' in __name__:
    import matplotlib as mpl
    mpl.use("TKAgg")
    import matplotlib.pylab as plt
    plt.ion()
    x = lambda n: np.linspace(-1,1,n)
    f = lambda x: np.cos(np.sin(np.pi*x))
    plt.plot(x(300),f(x(300)),'k')
    n=5
    LX=x(250)
    data=zip(x(n),f(x(n)))
    LY = LagrangeInterp(data, LX)
    print LY
    plt.plot(LX,LY,'r')

# returns a dictionary to be used in the API
# def coord(x,y):
# 	return {'x': x, 'y': y}
# 
# if __name__ == '__main__':
# 
# 	Graph = Graph(6)
# 
# 	Graph.plot_point( coord(2,2) )
# 	Graph.plot_function( sin )
# 
# 	mainloop() # runs window indefinitely
