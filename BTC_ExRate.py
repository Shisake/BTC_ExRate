import urllib
import json
import time
import sys
import datetime

def getBTCExRate():
    url = "https://blockchain.info/ticker"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    ExRate = data['USD']['last']
    return ExRate

if "log" in sys.argv[1:]
    while True:
        with open("/home/pi/BTC_ExRate/BTC_ExRateLog.txt","a") as f:
            now = datetime.datetime.now()
            f.write(now.strftime("%d.%m.%y | %H:%M  ") + str(getBTCExRate()) + "\n")
            time.sleep(60)
else:
    print str(getBTCExRate()) + " $"

input()
