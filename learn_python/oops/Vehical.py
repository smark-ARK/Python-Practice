class vehical:
    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

    def vehicalinfo(self):
        print('Name of vehical:', self.name, '\nMaximum Speed:',
              self.max_speed, '\nMilage:', self.milage)


vehical1 = vehical('Karizma ZMR', '220 kmph', '30 kmpl')
vehical1.vehicalinfo()
