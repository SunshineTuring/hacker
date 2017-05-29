#!coding=utf-8
import socket
import optparse



def portScan(hostName, tgtport):
    addre = socket.gethostbyname(hostName)
    if tgtport != None:
        tgtport = tgtport.split(',')
    else:
        tgtport = range(1,1000)
    for port in tgtport:
        print ('Scanning port %s' % port)
        connScan(addre,int(port))
# print socket.gethostbyname("192.168.100.47")
# print socket.gethostbyaddr("192.168.100.47")
def connScan(addre, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((addre, port))
        print ('[+]%d/tcp open'%port)
        s.close()
    except:
        print('[+]%s/tcp closed'%port)

if __name__ == "__main__":
    parser = optparse.OptionParser('usage %prog -H <targethost> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtport', type='string',default=None, help='specify target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtport = options.tgtport
    if (tgtHost == None):
        print (parser.usage)
        exit(0)
    else:
        portScan(tgtHost,tgtport)