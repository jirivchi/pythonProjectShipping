
# Credir card class -------------------------

from datetime import date
from datetime import datetime


class CreditCard():
    holder = "John"
    monthexpiry = date.today().month
    yearexpiry = date.today().year
    CVC = 111
    number = '1111111111111111'
    cardcompany = ''
    limit = 0
    response = "test"
    response2 = "test"

    def filloutcard (self):

        print('*------------------------\u001b[33m Credit card \u001b[0m--------------------*')
        self.holder = input ('Credit card holder: ')

        while True:  # Repeat it until you write it right
            self.number = input ('Card number: ')
            if 13 < len(self.number) < 19:
                break
            else:
                print("\u001b[33m Check Card number once again. It must be between 13 and 19 digits long.\u001b[0m")

        while True: # Repeat it until you write a valid month
            self.monthexpiry = input ('Expiration month: ')
            if 0 < int(self.monthexpiry ) < 13:
                break
            else:
                print("\u001b[33m Check expiration month. It must be less than 13.\u001b[0m")
        while True: # Year must contain only 2 digits
            self.yearexpiry = input ('Expiration year: ')
            if len(self.yearexpiry) == 2:
                break
            else:
                print("\u001b[33m Check expiration year. It must contain only 2 digits.\u001b[0m")

        self.limit = int(input('Credit limit: '))
        self.CVC = input('Type the secret number: ')


    def company(self):

        if str(self.number).startswith('4'):
            self.cardcompany = 'Visa Card'
        elif str(self.number).startswith(('50', '67', '58', '63',)):
            self.cardcompany = 'Maestro Card'
        elif str(self.number).startswith('5'):
            self.cardcompany = 'Master Card'
        elif str(self.number).startswith('37'):
            self.cardcompany = 'American Express Card'
        else:
            self.cardcompany = 'Not recognized company Card'
        #print(myCard.cardcompany)

    def validate(self):
        """
        Luhn's Algorithm
        Example: 49927398716
        The digits that occupy the even positions starting from the end are multiplied by 2:
        (1×2) = 2, (8×2) = 16, (3×2) = 6, (2×2) = 4, (9×2) = 18
        The digits that occupy the odd positions are added with the digits of the obtained products:
        6 + (2) + 7 + (1 + 6) + 9 + (6) + 7 + (4) + 9 + (1 + 8) + 4 = 70.
        PS: (1+6) is for the multiplication of 8x2=16 and (1+8) is for the multiplication of 9x2=18 of the first point
        If the result of this sum is a multiple of 10, the number is correct: 70% 10 = 0
        """

        # initialize variable for addition
        sum_ = 0

        # put the number backwards to count better
        crd_no = self.number [::-1]

        # the odd ones (with remainder = 1) are actually the even ones since the list starts with 0
        for i in range(len(crd_no)):
           if i % 2 == 1:
               double_it = int(crd_no[i]) * 2
               if len(str(double_it)) == 2:
                   sum_ += sum([eval(i) for i in str(double_it)])
               else:
                   sum_ += double_it
           else:
               sum_ += int(crd_no[i])

        if sum_ % 10 == 0:
            self.response = "valid"
        else:
            self.response = '\u001b[91m not valid \u001b[0m'

        print(f'\033[92m Your {myCard.cardcompany} number {myCard.number} is {self.response}')


    def testexpiry(self):
        if len(self.monthexpiry) == 1:
            self.monthexpiry = '0' + self.monthexpiry

        date_time_str = '20' + self.yearexpiry + '-' + self.monthexpiry + '-' + '01' + ' 00:00:00'
        today = date.today()

        expdate = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

        daysleft = (expdate.date() - today).days

        if daysleft <= 0:
            print( '\u001b[91m Expired card. Type a new one. \u001b[0m')
        else:
            self.response2 = 'Card in use'
            print('\033[92m Card in use')
