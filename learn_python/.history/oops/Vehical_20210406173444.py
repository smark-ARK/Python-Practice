class vehical:
    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

    def vehicalinfo(self):
        print('Name of vehical:', self.name, 'Maximum Speed:',
              self.max_speed, 'Milage:', self.milage)
