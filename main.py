# --------------- Final Project Python -------------------------*
# --------------- Ismael Rivera & Wagner E. Schuster -------------------------*

#LIBRARIES FROM EACH CLASS
from transportclass import Transport
from packageclass import Package
from priceclass import Price
from creditcardclass import CreditCard
from userclass import User


#--------------------------------------- Code --------------------------------------------------------
print ('*-------------------------------------------------------------------------*')
print('*------------------------------ \033[1;33m RivEx \033[0m ----------------------------------*')
print('*---------------------- All shipping services ----------------------------*')
print('*-------------------------------------------------------------------------*')
print('')
print('')
sender = User() #new
receiver = User() #new
myTransport = Transport()
myPackage = Package()
myPrice = Price()
myCard = CreditCard()

while True:

    while True:
        sender.filloutuser('Sender')
        receiver.filloutuser('Receiver')
        myTransport.choosetransport()
        myTransport.calcroute()
        myPackage.filloutpack()
        myPrice.CalcPrice(myTransport.destiny, myTransport.distance, myTransport.way, myPackage.type, myPackage.strweight)

        print(f'Summary of your order: \n {myTransport.destiny} Shipping \n Distance: {myTransport.distance} km'
              f' \n Collecting at home: {myTransport.collection.upper()} \n Package: {myPackage.type} and {myPackage.strweight}'
              f' \n Speed: {myPrice.speedname}')

        ok = input('Are all the data correct? -\u001b[33mY\u001b[0m or \u001b[33mN\u001b[0m-: ')
        if ok.upper() == 'Y':
            break

    Cash_Card = input('Will you pay with \u001b[33mC\u001b[0mard or in Cas\u001b[33mH\u001b[0m: ')

    if Cash_Card.upper() == 'C':

        myCard = CreditCard()
        myCard.filloutcard()

        print(f'\u001b[33m One moment, we are checking your card\u001b[0m')

        myCard.limit -= myPrice.totalprice
        print(f'\033[92m The limit after payment will be {myCard.limit:.2f} €')

        if myCard.limit < 0:
            print('\033[91m Sorry. The price of your shipping is higher than your card limit \033[91m')
            print('Operation canceled')
            break

        myCard.company()
        myCard.validate()
        test = myCard.response
        if test != "valid" or myCard.company() == "Not recognized company":
            print('\033[91m Sorry. The card informed is not valid')
            print('Operation canceled')
            break

        myCard.testexpiry()
        test2 = myCard.response2
        if test2 != "Card in use":
            print('\033[91m Sorry. The card informed is expired')
            print('Operation canceled')
            break

        else:
            myTransport.assigntracknumber()
            print('\033[92m Everything is ok with your card, thank you very much for your order')
            print(f'Your track number is {myTransport.tracknumber}')

    else:

        print('\033[92mThank your for your order. You will pay in one of our offices.')

