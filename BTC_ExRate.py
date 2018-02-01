import urllib
import json
import time
import sys
import datetime
from RPLCD.gpio import CharLCD

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
        lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data[21, 22, 23, 24],
        numbering_mode=GPIO.BOARD)
        lcd.write_string("Ahoj")
    time.sleep(60)
else:
    print str(getBTCExRate()) + " $"

input()
