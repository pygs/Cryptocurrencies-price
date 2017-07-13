import json
import requests
import time
import os

def print_info(name, url):
        response = requests.get(url=url)
        data = json.loads(response.text)
        print name + " Last: " + str(data["last"])
        print name + " BID: " + str(data["bid"])
        print name + " ASK: " + str(data["ask"])
        print name + " Vol: " + str(data["volume"])
print "Opcja/Option 1: PLN"
print "Opcja/Option 2: USD"
print "Opcja/Option 3: EUR"
print "Opcja/Option 4: BTC"
choice = int(raw_input("Wybierasz/You choose: "))

if choice is 1:
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
if choice is 2:
        while 1:
                try:
                        if os.name == "nt":
                                os.system("cls")
                        else:
                                os.system("clear")
                        print_info("ETH/PLN", "https://bitbay.net/API/Public/ETHUSD/ticker.json")
                        print "============================================"
                        print_info("BTC/PLN", "https://bitbay.net/API/Public/BTCUSD/ticker.json")
                        print "============================================"
                        print_info("LTC/PLN", "https://bitbay.net/API/Public/LTCUSD/ticker.json")
                        print "============================================"
                        print_info("LSK/PLN", "https://bitbay.net/API/Public/LSKUSD/ticker.json")
                        time.sleep(4)
                except:
                        print "See you later..."
                        exit()
if choice is 3:
        while 1:
                try:
                        if os.name == "nt":
                                os.system("cls")
                        else:
                                os.system("clear")
                        print_info("ETH/PLN", "https://bitbay.net/API/Public/ETHEUR/ticker.json")
                        print "============================================"
                        print_info("BTC/PLN", "https://bitbay.net/API/Public/BTCEUR/ticker.json")
                        print "============================================"
                        print_info("LTC/PLN", "https://bitbay.net/API/Public/LTCEUR/ticker.json")
                        print "============================================"
                        print_info("LSK/PLN", "https://bitbay.net/API/Public/LSKEUR/ticker.json")
                        time.sleep(4)
                except:
                        print "See you later..."
                        exit()
if choice is 4:
        while 1:
                try:
                        if os.name == "nt":
                                os.system("cls")
                        else:
                                os.system("clear")
                        print_info("ETH/PLN", "https://bitbay.net/API/Public/ETHBTC/ticker.json")
                        print "============================================"
                        print_info("LTC/PLN", "https://bitbay.net/API/Public/LTCBTC/ticker.json")
                        print "============================================"
                        print_info("LSK/PLN", "https://bitbay.net/API/Public/LSKBTC/ticker.json")
                        time.sleep(4)
                except:
                        print "See you later..."
                        exit()
