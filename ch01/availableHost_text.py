import os

Host = '192.168.100.'
fileName = "available.log"
sFile = open(fileName,'w')
for i in range(1,255):
    status = os.system("ping -n 1 %s%s"%(Host, str(i)))
    if status == 0:
        sFile.write("%s%s"%(Host, str(i)))
        print "%s%s is available"%(Host, str(i))
sFile.close()
