##Function to get the appropriate max and mins for the scale of the graph
##Use round_to to create padding for the graph, ie if the graph goes up by 5,
##set round_to to 5 to keep the graph neat
def get_scale(data_set, round_to=0) :
    x = 0
    neg_x = 0
    y = 0
    neg_y = 0
    #get the maximum x, -x, y, -y that need to be mapped
    for i in data_set:
        if i['x'] > x : x = i['x']
        if i['x'] < neg_x : neg_x = i['x']
        if i['y'] > y : y = i['y']
        if i['y'] < neg_y : neg_y = i['y']
    #add to scale to keep it a multiple of round_to
    if (round_to > 0): 
        x = x + (round_to - x%round_to)
        neg_x = -(abs(neg_x) + (round_to - abs(neg_x)%round_to))
        y = y + (round_to - y%round_to)
        neg_y = -(abs(neg_y) + (round_to - abs(neg_y)%round_to))
        
    return [x,neg_x,y,neg_y]

print get_scale(coords)
