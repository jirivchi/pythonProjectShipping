# Package class --------------------------------------------------------------

from transportclass import Transport

class Package():
    width = 0
    height = 0
    length = 0
    volume = 0
    weight = 0
    type = ''
    strweight = ' '

    def filloutpack (self):
        print(f'*--------------------\u001b[33m Package \u001b[0m---------------------------*')
        self.length = int ( input ('Package length in cm: '))
        self.width = int ( input ('Package width in cm: '))
        self.height = int ( input ('Package height in cm: '))
        self.weight = float (input('Weight of the package in Kg: '))
        self.volume = self.height * self.width * self.length

        if self.volume < 8000:
            self.type = 'small'
        elif self.volume < 125000:
            self.type = 'medium'
        else:
            self.type = 'large'

        if self.weight <= 2.000:
            self.strweight = 'light'
        elif self.weight <= 5.000:
            self.strweight = 'semi'
        else:
            self.strweight = 'heavy'


        print (f'\u001b[93mThe {Transport.destiny} shipping will be of a {self.type} size and {self.strweight}-weighted package via {Transport.way} at {Transport.distance} Km\u001b[0m')



