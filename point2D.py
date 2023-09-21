class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point at (' + str(self.x) + ', ' + str(self.y) +')'
    
    def distanceTo(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return (dx**2 + dy**2) ** 0.5


origin = Point(0,0)
p1 = Point(3,4)
p2 = Point(7,10)
print(p1.distanceTo(origin))


class Scatter:
    def __init__(self):
        self.points = []

    def addPoint(self, p):
        self.points.append(p)

    def removePoint(self, p):
        self.points.remove(p)

    def getClosestPoint(self, targetPoint):
        closestDistance = 100000000000000000000000000000
        closestPoint = Point(0,0) 
        for point in self.points:
            if targetPoint.distanceTo(point) < closestDistance:
                closestDistance = targetPoint.distanceTo(point)
                closestPoint = point

        return closestPoint

    def __str__(self):
        #########################
        # Just print the points #
        #########################

        # output = ''
        # for point in self.points:
        #     output += str(point) + '\n'
        # return output
        ######################
        # Make a fancy chart #
        ######################

        xs = [point.x for point in self.points]
        ys = [point.y for point in self.points]

        min_x = min(xs)
        min_y = min(ys)

        max_x = max(xs)
        max_y = max(ys)

        x_len = max(len(str(max_x)), len(str(min_x)))
        y_len =  max(len(str(max_y)), len(str(min_y)))

        output = ''
        for row in range(max_y, min_y -1, -1):
            
            output += str(row).rjust(x_len + 1) + '|'
            for col in range(min_x,  max_x + 1):
                pr = ' '
                for point in self.points:
                    if point.x == col and point.y == row:
                        pr = 'X'
                output += pr
            output += '\n'
        output += '-' * (x_len+1) + '+' + '-' * (max_x - min_x + 1) + '\n'
        x_strings = [str(x) for x in range(min_x, max_x+1)]
        x_strings = [x if x[0] == '-' else ' ' + x for x in x_strings]

        x_len = max([len(x) for x in x_strings])
        
        for i in range(0, x_len+1):
            output += ' ' * (x_len) + '|'
            for s in x_strings:
                if len(s) > i:
                    output += s[-i]
                else:
                    output += ' '
            output += '\n'
                
                    
        return output
    

origin = Point(0,0)
p1 = Point(-3,4)
p2 = Point(11,10)

s = Scatter()
s.addPoint(origin)
s.addPoint(p1)
s.addPoint(p2)



print(s)


t = Point(1,1)
print(s.getClosestPoint(t))

lst = [100,5,3,8,32,89,3,12]

mini = 1000000000
mini_location = 0
for i in range(len(lst)):
    if lst[ i] < mini:
        mini = lst[i]
        mini_location = i

print(mini, mini_location)