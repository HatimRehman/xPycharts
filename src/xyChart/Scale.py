##
# get_scale\n
# Author: Louis Bursey\n
# Function to get the appropriate max and mins for the scale of the graph\n
# Returns a tuple in the format [x,y]
#  @param data_set, the set of data being graphed, in a (x,y) dictionary
#  @param round_to, an optional parameter to make the scale a multiple of round_to
def get_scale(data_set, round_to=0) :
    x = 0

    y = 0

    
    for i in data_set: #get the maximum x, -x, y, -y that need to be mapped
        if abs(i['x']) > x : x = abs(i['x'])
        
        if abs(i['y']) > y : y = abs(i['y'])
        
    
    if (round_to > 0): #add to scale to keep it a multiple of round_to
        x = x + (round_to - x%round_to)
        
        y = y + (round_to - y%round_to)
        
        
    return [x,y]

