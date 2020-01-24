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
          ['TAEL-DLMP-5UTD-LDQQ-8929X','password10'],
        ['TAEL-7WM6-25HQ-PWRD-6JYL5', 'password11'],
        ['TAEL-2F46-CUYL-GEQ9-HAV4S', 'password12'],
        ['TAEL-MVSV-VJT9-ZF66-BD69Q', 'password13'],
        ['TAEL-YB5W-5BC5-Y8BR-FSAHE', 'password14'],
        ['TAEL-6J4A-KQPT-WKUU-8UCVZ', 'password15'],
        ['TAEL-KXFC-KDK9-9QZZ-F62B6', 'password16'],
        ['TAEL-YPYD-HL88-3MAB-BBZ5Y', 'password17'],
        ['TAEL-PHRR-B6MS-K68F-B787N', 'password18'],
        ['TAEL-C2KW-R47L-UL46-FP4V4', 'password19'],
        ['TAEL-GG8F-KX2Y-EKJH-B5R7A', 'password20']]

RED_QUEEN = '44333'
ALPHA = '43255'
DEFAULT = '43250'
PORT = RED_QUEEN

INTERVAL = 5


def getLatestBlock():
    '''
    http://localhost:7876/nxt?
  requestType=getBlockchainStatus
    :return:
    '''

    URL = 'http://localhost:'+PORT+'/nxt?' +\
  'requestType=getBlockchainStatus'

    r = requests.post(url=URL)
    data = r.json()
    blockId = data['lastBlock']
    print 'Latest Block:', blockId

    URL = 'http://localhost:'+PORT+'/nxt?' + \
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
        URL = 'http://localhost:'+PORT+'/nxt?' +\
      'requestType=getTransaction&' +\
      'transaction=' + txId

        r = requests.post(url=URL)
        data = r.json()

        return data['block'], data['blockTimestamp'],data['height']
    except Exception,e:
        print str(e)
        return None, None, None

def getAccountBalance(account):

    URL = 'http://localhost:'+PORT+'/nxt?' +\
    'requestType=getAccount&' +\
    'account=' + account

    r = requests.post(url=URL)
    data = r.json()

    return data['unconfirmedBalanceNQT']

def sendMoney(recipient, amount, password):
    URL = 'http://localhost:'+PORT+'/nxt?' +\
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

    amountToSend = int(random.random() * int(balance))


    if amountToSend < 1:
        amountToSend = 1
    sendMoney(ACCOUNTS[recipient][0], str(amountToSend), ACCOUNTS[sender][1])

    print ACCOUNTS[sender][0], 'sent', str(amountToSend), 'to', ACCOUNTS[recipient][0], '.'

def startForging(acct):
    URL = 'http://localhost:'+PORT+'/nxt?' +\
      'requestType=startForging&' +\
      'secretPhrase=' + ACCOUNTS[acct][1]

    r = requests.post(url=URL)
    data = r.json()

    print ACCOUNTS[acct][0], 'started forging.'

def stopForging(acct):
    URL = 'http://localhost:'+PORT+'/nxt?' +\
      'requestType=stopForging&' +\
      'secretPhrase=' + ACCOUNTS[acct][1]

    r = requests.post(url=URL)
    data = r.json()

    print ACCOUNTS[acct][0], 'stopped forging.'

def getForging(password):
    URL = 'http://localhost:'+PORT+'/nxt?' + \
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
    notConnectedFlag = False
    forgingAccts = []
    nonForgingAccts = [15,16,17,18,19] # change for each node

    while (True):
        time.sleep(INTERVAL)
        try:
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
                sender = random.randint(0, len(ACCOUNTS)-1)
                recipient = random.randint(0, len(ACCOUNTS)-1)
                while (sender == recipient):
                    recipient = random.randint(0, len(ACCOUNTS)-1)

                sendTx(recipient=recipient, sender=sender)

            print 'Forging', forgingAccts
            print 'Non-forging', nonForgingAccts
            print 'Timestamp:', time.strftime("%Y-%b-%d %H:%M:%S")
            print

        except Exception as e:
            if 'Connection refused' in str(e):
                if notConnectedFlag:
                    continue
                else:
                    print e
                    print 'Timestamp:', time.strftime("%Y-%b-%d %H:%M:%S")
                    print
                    notConnectedFlag=True

            else:
                print e
                print 'Timestamp:', time.strftime("%Y-%b-%d %H:%M:%S")
                notConnectedFlag=False
                print
                continue




if __name__ == '__main__':
    main()
