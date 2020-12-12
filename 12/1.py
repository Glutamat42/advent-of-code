class Ship:
    def __init__(self, start_x=0, start_y=0, start_direction=90):
        """

        :param start_x:
        :param start_y:
        :param start_direction: degree from north clockwise
        """
        self.x = start_x
        self.y = start_y
        self.direction = start_direction

    def set_direction(self, angle):
        self.direction = angle % 360

    def move(self, instruction):
        cmd = instruction[0]
        val = int(instruction[1:])

        if cmd == 'N':
            self.y += val
        elif cmd == 'S':
            self.y -= val
        elif cmd == 'E':
            self.x += val
        elif cmd == 'W':
            self.x -= val
        elif cmd == 'L':
            self.set_direction(self.direction - val)
        elif cmd == 'R':
            self.set_direction(self.direction + val)
        elif cmd == 'F':
            if self.direction == 0:
                self.y += val
            elif self.direction == 180:
                self.y -= val
            elif self.direction == 90:
                self.x += val
            elif self.direction == 270:
                self.x -= val
            else:
                print('invalid direction')
        else:
            print('invalid cmd')


class ShipWaypoint:
    def __init__(self, start_x=0, start_y=0):
        """

        :param start_x: waypoint start
        :param start_y: waypoint start
        :param start_direction: degree from north clockwise
        """
        self.x = 0
        self.y = 0
        self.waypoint = (start_x, start_y)

    def move(self, instruction):
        cmd = instruction[0]
        val = int(instruction[1:])

        if cmd == 'N':
            self.waypoint = (self.waypoint[0], self.waypoint[1] + val)
        elif cmd == 'S':
            self.waypoint = (self.waypoint[0], self.waypoint[1] - val)
        elif cmd == 'E':
            self.waypoint = (self.waypoint[0] + val, self.waypoint[1])
        elif cmd == 'W':
            self.waypoint = (self.waypoint[0] - val, self.waypoint[1])
        elif cmd == 'R':
            for i in range(int(val / 90)):
                self.waypoint = (self.waypoint[1], self.waypoint[0] * -1)
        elif cmd == 'L':
            for i in range(int(val / 90)):
                self.waypoint = (self.waypoint[1] * -1, self.waypoint[0])
        elif cmd == 'F':
            self.x += self.waypoint[0] * val
            self.y += self.waypoint[1] * val
        else:
            print('invalid cmd')


with open('data') as file:
# with open('test_data') as file:
    data = file.read().splitlines()

print('PART ONE')

ship = Ship()
for instruc in data:
    ship.move(instruc)
print(f'x: {ship.x}, y: {ship.y}')
print(abs(ship.x) + abs(ship.y))

print('\n\n\nPART TWO')
ship = ShipWaypoint(start_x=10, start_y=1)
for instruc in data:
    ship.move(instruc)
print(f'x: {ship.x}, y: {ship.y}')
print(abs(ship.x) + abs(ship.y))
