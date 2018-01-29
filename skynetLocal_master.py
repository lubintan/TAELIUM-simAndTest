import os, time, random, sys, subprocess
import login_forge, login_unforge, login_sendTx
# Acct ID, password, forging

Accounts = [['VXVQ-APCC-UHDD-7A3ZX','password1', False,'Local'],
        ['PGDQ-XR6X-2EAS-9H2KM','password2', False,'Local'],
          ['D6PA-3TCG-AXGA-BVHW4','password3', False,'Local'],
          ['Y4LF-K6UK-AT74-CT6JS','password4', False,'Local'],
          ['J4YD-K25L-6AAS-E6Y9C','password5', False,'Local'],
          ['D8XY-HTU7-QWM5-2YHMZ','password6', False,'Local'],
          ['PQMA-6CS2-XU9J-AWZY7','password7', False,'Local'],
          ['N7LT-FNZN-A9QJ-GPXMA','password8', False,'Local'],
          ['KXHS-8A7R-5FF5-5PFS6','password9', False,'Local'],
          ['DLMP-5UTD-LDQQ-8929X','password10', False,'Local']]

Nodes = {'Local': 'http://localhost:43250/'}



def forge(account):
    try:
        # os.system("python login_forge.py")
        # os.system(node)
        # os.system(account[1])


        inputString = Nodes[account[3]] + ',' + account[1]

        os.system(('echo "%s" | python login_forge.py') %(inputString))

        account[2] = True
    finally:
        pass



def unforge(account):
    try:
        # os.system("python login_unforge.py")
        # os.system(node)
        # os.system(account[1])

        inputString = Nodes[account[3]] + ',' + account[1]
        os.system(('echo "%s" | python login_unforge.py') % (inputString))

        account[2] = False
    finally:
        pass

def sendTx(account, recipient):
    try:
        # os.system("python login_sendTx.py")
        # os.system(node)
        # os.system(account[1])
        # os.system(recipient[0])
        inputString = Nodes[account[3]] + ',' + account[1] + ',' + recipient[0]

        os.system(('echo "%s" | python login_sendTx.py') % (inputString))

    finally:
        pass




if __name__ == '__main__':


    time.sleep(2) #for everything to load
    # forever forgers
    # forge(Accounts[9])
    # forge(Accounts[8])

    # setup
    forge(Accounts[0])
    forge(Accounts[1])
    forge(Accounts[2])
    forge(Accounts[3])
    forge(Accounts[4])
    forge(Accounts[5])
    forge(Accounts[6])
    forge(Accounts[7])
    forge(Accounts[8])
    forge(Accounts[9])

    while(True):
        time.sleep(5)
        action = random.randint(0,10)

        if action <= 3:
            acctNum = random.randint(0, 9)
            forge(Accounts[acctNum])
            print 'Account ', Accounts[acctNum][0], 'started forging on Node ', Accounts[acctNum][3]

        elif ((action ==4) or (action ==5)) :
            acctNum = random.randint(0, 9)
            unforge(Accounts[acctNum])
            print 'Account ', Accounts[acctNum][0], 'stopped forging on Node ', Accounts[acctNum][3]

        elif ((action >=6) and (action <=8)):
            acctNum = random.randint(0, 9)
            recipient = random.randint(0, 9)
            while (acctNum == recipient):
                recipient = random.randint(0, 9)

            sendTx(Accounts[acctNum], Accounts[recipient])

            print 'Account ', Accounts[acctNum][0], 'sending to account ', Accounts[recipient][0], 'on node ', Accounts[acctNum][3]

        else:
            print "Chilling..."



