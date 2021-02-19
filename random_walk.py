from random import choice

class RandomWalk: # creates class
    """A class to generate random walks"""

    def __init__(self, num_points=5000): # initialise class
        """initialise the attributes of a walk"""
        self.num_points = num_points # initialises number of points in a walk with default at 5000

        # all walks start at 0,0
        self.x_values = [0] # list for x values
        self.y_values = [0] # list for y values

    def fill_walk(self):
        """calculate all the points in the walk"""

        #keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points: # while the length of the x values is smaller than num_points

            # decide which direction to go and how far to go in that direction
            x_direction = choice([1, -1]) # choose whether to go right or left
            x_distance = choice([0, 1, 2, 3, 4]) # choose how far to go in that direction
            x_step = x_direction * x_distance # one step is a direction and a distance

            y_direction = choice([1, -1]) # choose whether to go up or down
            y_distance = choice([0, 1, 2, 3, 4]) # choose how far to go
            y_step = y_direction * y_distance # on step and how far up or down

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0: # if both x and y equal 0 then ignore it
                continue

            #calculate the new position
            x = self.x_values[-1] + x_step # x position after move
            y = self.y_values[-1] + y_step # y position after move

            self.x_values.append(x) # add new x to the x_values list
            self.y_values.append(y) # add new y to the y_values list