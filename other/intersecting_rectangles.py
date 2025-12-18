# (ex. Intersecting rectangles - Dodona)

def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    coordinates1 = []   # exclude border points of rectangle 1
    coordinates2 = []   # include border points of rectangle 2

    for y in range(y1 + 1, y1 + h1):
        for x in range(x1 + 1, x1 + w1):
            coordinate = (x,y)
            coordinates1.append(coordinate)

    for y in range(y2, y2 + h2 + 1):
        for x in range(x2, x2 + w2 + 1):
            coordinate = (x,y)
            coordinates2.append(coordinate)

    # check for the same coordinates, if they exist: return True for intersect, else return False
    for i in coordinates1:
        if i in coordinates2:
            return True
    return False
