class Cuboid(object):
    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width

    def get_surface(self):
        surface = 2 * (self.length * self.width + self.width * self.height + self.height * self.length)
        return surface

    def get_volume(self):
        volume = int(self.height) * int(self.length) * int(self.width)
        return volume
    # Create a class that represents a cuboid:
    # It should take its three dimensions as constructor parameters (numbers)
    # It should have a method called `get_surface` that returns the cuboid's surface
    # It should have a method called `get_volume` that returns the cuboid's volume

box = Cuboid(10, 20, 30)
print("the surface of the box is: " + str(box.get_surface())) # should print 2200
print("the volume of the box is: " + str(box.get_volume())) # should print 6000
