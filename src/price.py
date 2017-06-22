import json
import requests
import time
import os

urlETH = "https://bitbay.net/API/Public/ETHPLN/ticker.json"
urlBTC = "https://bitbay.net/API/Public/BTCPLN/ticker.json"

def print_info(name, url):
        response = requests.get(url=url)
        data = json.loads(response.text)
        print name + " Last: " + str(data["last"])
        print name + " BID: " + str(data["bid"])
        print name + " ASK: " + str(data["ask"])
        print name + " Vol: " + str(data["volume"])

while 1:
        try:
                if os.name == "nt":
                        os.system("cls")
                else:
                        os.system("clear")

                print_info("ETH/PLN", "https://bitbay.net/API/Public/ETHPLN/ticker.json")
                print "============================================"
                print_info("BTC/PLN", "https://bitbay.net/API/Public/BTCPLN/ticker.json")
                print "============================================"
                print_info("LTC/PLN", "https://bitbay.net/API/Public/LTCPLN/ticker.json")
                print "============================================"
                print_info("LSK/PLN", "https://bitbay.net/API/Public/LSKPLN/ticker.json")
                time.sleep(4)
        except:
                print "See you later..."
                exit()
