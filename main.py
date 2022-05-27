
#OPSEC panel by Glocked
# Glocked Security Suite
import json # used to print
import subprocess
import browserclearerhard
from browserclearerhard import *
import requests # IP-printing
from getmac import get_mac_address as getmacmodule # for MAC address printing
import dearpygui # for the GUIs
import dearpygui.dearpygui as dpg

# current data (used later for "print current data" option on GUI):
# so I was gonna use WMI module to get current MAC address and IP from network interfaces
# however, WMI requires win32COM, which is only available on windows, and my workstation isn't
# powered by Windows. WMI network interface would also only give me local IP.

def printcurrentIP(): # it was supposed to print IP on-GUI but oh well
    ip_address = requests.get("https://api.ipify.org?format=json")
    response_dict = json.loads(ip_address.text)
    for i in response_dict:
         print(i, response_dict[i])

def currentmacaddress():
    print(getmacmodule())


# i'm lonely, man...

# define variables

def ipchanging():
    print("Unavailable for now, sadly. Use a proxy!") # :( couldn't figure out shell to ipconfig /release etc. will fix later, probably.

def getcurrentMACbutton(sender, data):
    currentmacaddress()

def getcurrentIPbutton(sender, data):
    printcurrentIP()

def ipchangerbutton(sender, data):
    ipchanging()

def browserhardclearingbutton(sender, data):
    browserclearerhard.clearallhard()

def clearchromebutton(sender, data):
    browserclearerhard.chrome()

def clearfirefoxbutton(sender, data):
    browserclearerhard.firefox

def clearbravebutton(sender, data):
    browserclearerhard.brave_local()

def browsersoftclearingbutton(sender, data):
    softbrowserclearer()



dpg.create_context()
dpg.create_viewport(title='Glocked Security Suite', width=600, height=444)
dpg.setup_dearpygui()

with dpg.window(tag="BrowserClearing", label="Browser clearing!"):
    dpg.add_button(label="Clear all browsers?", callback=browserclearerhard.clearallhard)
    dpg.add_button(label="Clear Firefox? use clean all instead plz", callback=clearfirefoxbutton)
    dpg.add_button(label="Clear Chrome?", callback=clearchromebutton)
    dpg.add_button(label="Clear Brave?", callback=clearbravebutton)

with dpg.window(tag="CurrentDataWindow", label="current data"):
    dpg.add_text(label="hey, this window prints your current pc's data.")
    dpg.add_button(label="What's my IP?", callback=getcurrentIPbutton)
    dpg.add_button(label="Current MAC address?", callback=getcurrentMACbutton)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
