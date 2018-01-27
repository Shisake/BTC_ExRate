import urllib
import json
import time
import sys
import datetime

arguments = ['log', 'display']

def getBTCExRate():
    url = "https://blockchain.info/ticker"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    ExRate = data['USD']['last']
    return ExRate


while True:
    if "log" in sys.argv[1:]:
        with open("/home/pi/BTC_ExRate/BTC_ExRateLog.txt","a") as f:
            now = datetime.datetime.now()
            f.write(now.strftime("%d.%m.%y | %H:%M  ") + str(getBTCExRate()) + "\n")

    if "display" in sys.argv[1:]:

    time.sleep(60)
else:
    print str(getBTCExRate()) + " $"

input()
