# importing the requests library
import requests, time, random

'''
http://localhost:7876/nxt?
  requestType=sendMoney&
  secretPhrase=IWontTellYou&
  recipient=NXT-4VNQ-RWZC-4WWQ-GVM8S&
  amountNQT=100000000&
  feeNQT=100000000&
  deadline=60
'''

ACCOUNTS = [['TAEL-VXVQ-APCC-UHDD-7A3ZX','password1'],
        ['TAEL-PGDQ-XR6X-2EAS-9H2KM','password2'],
          ['TAEL-D6PA-3TCG-AXGA-BVHW4','password3'],
          ['TAEL-Y4LF-K6UK-AT74-CT6JS','password4'],
          ['TAEL-J4YD-K25L-6AAS-E6Y9C','password5'],
          ['TAEL-D8XY-HTU7-QWM5-2YHMZ','password6'],
          ['TAEL-PQMA-6CS2-XU9J-AWZY7','password7'],
          ['TAEL-N7LT-FNZN-A9QJ-GPXMA','password8'],
          ['TAEL-KXHS-8A7R-5FF5-5PFS6','password9'],
          ['TAEL-DLMP-5UTD-LDQQ-8929X','password10']]

def getLatestBlock():
    '''
    http://localhost:7876/nxt?
  requestType=getBlockchainStatus
    :return:
    '''

    URL = 'http://localhost:43250/nxt?' +\
  'requestType=getBlockchainStatus'

    r = requests.post(url=URL)
    data = r.json()
    blockId = data['lastBlock']
    print 'Latest Block:', blockId

    URL = 'http://localhost:43250/nxt?' + \
          'requestType=getBlock&block=' + blockId

    r = requests.post(url=URL)
    data = r.json()
    height = data['height']
    print 'Height:', height



def getTxInfo(txId):
    #now check if tx went through
    '''
    http: // localhost:7876 / nxt?
    requestType = getTransaction &
    transaction = 15200507403046301754
    '''

    try:
        URL = 'http://localhost:48250/nxt?' +\
      'requestType=getTransaction&' +\
      'transaction=' + txId

        r = requests.post(url=URL)
        data = r.json()

        return data['block'], data['blockTimestamp'],data['height']
    except Exception,e:
        print str(e)
        return None, None, None

def getAccountBalance(account):

    URL = 'http://localhost:43250/nxt?' +\
    'requestType=getAccount&' +\
    'account=' + account

    r = requests.post(url=URL)
    data = r.json()

    return data['unconfirmedBalanceNQT']

def sendMoney(recipient, amount, password):
    URL = "http://localhost:43250/nxt?" +\
      'requestType=sendMoney&' +\
      'secretPhrase=' + password +'&'+\
      'recipient=' + recipient + '&' +\
      'amountNQT=' + amount + '&' +\
      'feeNQT=10000&' +\
      'deadline=60'

    r = requests.post(url=URL)

    data = r.json()

    # for each in data:
    #     print each

def sendTx(recipient, sender):
    balance = getAccountBalance(ACCOUNTS[sender][0])
    print ACCOUNTS[sender][0], 'unconf balance:', balance

    amountToSend = int(random.random() * float(balance))
    if amountToSend < 1:
        amountToSend = 1
    sendMoney(ACCOUNTS[recipient][0], str(amountToSend), ACCOUNTS[sender][1])

    print ACCOUNTS[sender][0], 'sent', amountToSend, 'to', ACCOUNTS[recipient][0], '.'

def startForging(acct):
    URL = "http://localhost:43250/nxt?" +\
      'requestType=startForging&' +\
      'secretPhrase=' + ACCOUNTS[acct][1]

    r = requests.post(url=URL)
    data = r.json()

    print ACCOUNTS[acct][0], 'started forging.'

def stopForging(acct):
    URL = "http://localhost:43250/nxt?" +\
      'requestType=stopForging&' +\
      'secretPhrase=' + ACCOUNTS[acct][1]

    r = requests.post(url=URL)
    data = r.json()

    print ACCOUNTS[acct][0], 'stopped forging.'

def getForging(password):
    URL = "http://localhost:43250/nxt?" + \
          'requestType=getForging&' + \
          'secretPhrase=' + password

    r = requests.post(url=URL)
    data = r.json()

    return data

def getForgers():
    for account in ACCOUNTS:
        data = getForging(account[1])

        try:
            data['hitTime']
            print account[0], 'is forging.'
        except:
            print account[0], 'is NOT forging.'



def main():
    # accts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    forgingAccts = []
    nonForgingAccts = [0,1,2] # change for each node

    while (True):
        try:
            print
            action = random.randint(0,2) #inclusive 0 and 2

            if (action == 0): # start forging
                if len(nonForgingAccts)==0: continue
                acctNum = random.choice(nonForgingAccts)
                startForging(acctNum)
                forgingAccts.append(acctNum)
                nonForgingAccts.remove(acctNum)

            elif (action == 1): # stop forging
                if len(forgingAccts)==0: continue
                acctNum = random.choice(forgingAccts)
                stopForging(acctNum)
                nonForgingAccts.append(acctNum)
                forgingAccts.remove(acctNum)

            elif (action == 2): # send Money
                sender = random.randint(0, 9)
                recipient = random.randint(0, 9)
                while (sender == recipient):
                    recipient = random.randint(0, 9)

                sendTx(recipient=recipient, sender=sender)

            print 'Forging', forgingAccts
            print 'Non-forging', nonForgingAccts

        except Exception as e:
            print e
            continue




if __name__ == '__main__':
    main()
