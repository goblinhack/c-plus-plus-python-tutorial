class Point():
    ''' Point class to represent a 2d co-ordinate system '''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def x(self):
        return self.x

    def y(self):
        return self.y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def add(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def sub(self, dx, dy):
        self.x = self.x - dx
        self.y = self.y - dy

    def div(self, dx, dy):
        self.x = self.x / dx
        self.y = self.y / dy

    def mul(self, dx, dy):
        self.x = self.x * dx
        self.y = self.y * dy

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

    def length(self, other):
        return math.sqrt(self.x**2 + self.y**2)
