import datetime
import random
import time

SL =   {'SKB': 1000000,
        'FRT': 1000000,
        'AMG': 1000000,
        'DFT': 1000000,
        'MOG': 100000,
        'MEW': 100000,
        'LMX': 100000,
        'OHO': 100000,
        'EDG': 10000,
        'GNG': 10000,
        'GYT': 10000,
        'SGA': 10000,
        'CNT': 1000,
        'LGR': 1000,
        'FNM': 1000,
        'RIZ': 1000,
        'DDN': 1000}

wallet = 1000

def randomprice():
    now = datetime.datetime.now()
    sec = int(now.strftime("%S"))
    num = random.randint(1, 101)
    roundednum = sec*num
    roundednum = roundednum/100
    roundednum = round(roundednum)

def purchase():
    buyscreen = 0
    while buyscreen == 0:
        stockamount = 0
        ListSL = []
        a = input("Please enter desired stocks and amount to purchase:")
        words = a.split()
        
        if len(words) == 2:
            requestint = (words[1])
            requeststr = (words[0])

            if requestint.isdigit():
                requestint = int(words[1])
                requeststr = str(words[0])
                    
                if requeststr in SL:
                    stockamount = SL[requeststr]
                    
                    if stockamount >= requestint:
                        
                        if stockamount >= requestint:
                            stockamount = stockamount - requestint
                            SL[requeststr] = SL[requeststr] - requestint
                            buyscreen = buyscreen + 1
                            time.sleep(2)
                            
                        else:
                            print("Request Invalid")

                    else:
                        print("Request Invalid")

                else:
                    print("Request Invalid")

            else:
                print("Request Invalid")

        else:
            print("Request Invalid")

while True:
    print("Current Balance:" + str(wallet))
    print("""Choose an action:
1 . Purchase Shares
2 . ---
3 . ---""")
    choice = input(':')
    if choice in ['1', 'Purchase Shares', 'purchase shares', 'Purchase shares']:
        purchase()
    
    else:
        print("Request Invalid")
 




