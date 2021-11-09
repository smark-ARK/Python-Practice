class vehical:
    cname = 'SMARK'

    def __init__(self, Name, Milage, topSpeed):
        self.Name = Name
        self.Milage = Milage
        self.topSpeed = topSpeed

    def vinfo(self):
        print('Vehical Name: ', self.Name, 'Milage: ',
              self.Milage, 'topSpeed: ', self.topSpeed)
