class point:
    def __init__(self, id, x, y, z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z


class finger:
    def __init__(self):
        self.point = [point(0, 0, 0, 0)] * 5

    # def __init__(self):
    #     self.point = [point()] * 6

    def setPoints(pointNum, point):
        point[pointNum] = point

# point + x
# x = 1
# point1

# point1 = point(id, x, y, z)

# thumb = finger(point1, point2, point3, point4)
