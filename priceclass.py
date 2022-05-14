
# Price class --------------------------------------------------**

from transportclass import Transport

class Price():

    basicprice = 5
    dicttipo = {"International": 1.5, "Local" : 1}
    dictmethod = {"flight": 2, "surface": 1}
    dictweight = {"light" : 1, "semi" : 1.5, "heavy": 2}
    dictsize = {"small": 1, "medium": 1.5, "large": 2}
    totalprice = 0
    speedname = ''

    # The calculation is made from a minimum base -5- multiplied by 1, 1.5 or 2 depending on the type of shipment, the distance,
    # the transport used, and the size and weight of the package. In the case of distance, the Km are divided by 1100 and multiplied by 1.5

    def CalcPrice (self, trip, dist, method, vol, weight):

        self.totalprice = round ( self.basicprice * self.dicttipo [trip] * (dist * 1.5 / 1100) * self.dictmethod [method] * self.dictsize [vol] * self.dictweight[weight], 2 )

        if Transport.collection == 'Y':
            print('\u001b[93mCollection at home -15€-\u001b[93m')
            self.totalprice += 15
        else:
            self.totalprice = self.totalprice

        if trip == 'International':
            print ('International shipping: Please select the shipping speed for your order.')
            speed = input('Type \n \u001b[33m1 \u001b[0m : Priority worldwide (2-3 days) \n \u001b[33m2 \u001b[0m : Express International (4-7 days) \n \u001b[33m3 \u001b[0m : Standard shipping (7-10 days) \n ')
            if speed == '1':
                self.speedname = 'Priority worldwide (2-3 days)'
            if speed == '2':
                self.speedname = 'Express International (4-7 days)'
            else:
                self.speedname = 'Standard shipping (7-10 days)'
        else:
            print('Local shipping: Please select the shipping speed for your order.')
            speed = input('Type \n \u001b[33m1 \u001b[0m : Priority (24 hours) \n \u001b[33m2 \u001b[0m : Express national (24-48 hours) \n \u001b[33m3 \u001b[0m : Standard shipping (72 hours) \n ')
            if speed == '1':
                self.speedname = 'Priority (24 hours)'
            if speed == '2':
                self.speedname = 'Express national (24-48 hours)'
            else:
                self.speedname = 'Standard shipping (72 hours)'
        # Final price (priority doubles prize, and express * 1.5)
        if speed == '1':
            self.totalprice *= 2
        if speed == '2':
            self.totalprice *= 1.5

        print(f'\u001b[93mTotal price for your shipping: {self.totalprice:.2f} €\u001b[0m')

