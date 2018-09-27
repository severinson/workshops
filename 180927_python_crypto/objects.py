class Circle(object):

    def __init__(self, x, y, radius):
        print('this runs')
        self.x = x
        self.y = y
        self.radius = radius

    def __repr__(self):
        return f'Circle(x={self.x}, y={self.y}, r={self.radius})'


# l = list()
# for x in range(0, 10):
#     l.append(Circle(x, 0, 1))

# x = [0, 1, ...]
# y = [0, 0, ...]
# r = [1, 1, ...]


circle = Circle(0, 0, 1)
print('x in circle', circle.x)
# print(circle)
