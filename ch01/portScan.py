import sys
from scapy.all import sr, IP, TCP

if len(sys.argv) < 2:
    print sys.argv[0] + "<host> <spoofed_source_ip>"
    sys.exit(1)
if len(sys.argv) == 3:
    packet = IP(dst=sys.argv[1], src=sys.argv[2])
else:
    packet = IP(dst=sys.argv[1])
packet /= TCP(dport=range(1,1025), flags="S")

answered, unanswered = sr(packet, timeout=1)
res ={}
for packet in unanswered:
    res[packet.dport] = "filtered"
for (send, recv) in answered:
    if recv.getlayer("ICMP"):
        type = recv.getlayer("ICMP").type
        code = recv.getlayer("ICMP").code
        if code == 3 and type==3:
            res[send.packet.dport] = "closed"
        else:
            res[send.packet.dport] = "Got ICMP with type " + \
                                    str(type) + \
                                    " and code " + \
                                    str(code)
    else:
        flags = recv.getlayer("TCP").sprintf("%flags%")
        if flags == "SA":
            res[send.dport] = "open"
        elif flags=="R" or flags =="RA":
            res[send.dport] = "closed"
        else:
            res[send.dport] = "Got packet with flags " + str(flags)

ports = res.keys()
ports.sort()
for port in ports:
    if res[port] != "closed":
        if res[port] != "filtered":
            print str(port) + ": " + res[port]

