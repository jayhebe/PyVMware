from pyVim.connect import SmartConnect, Disconnect
import ssl

try:
    si = SmartConnect(host = "labvcsa01.vlab.net", user = "adminjig", pwd = "Start1234")
    #print("valid certification.")
except:
    context = None
    
    if hasattr(ssl, "_create_unverified_context"):
        context = ssl._create_unverified_context()
        
    si = SmartConnect(host = "labvcsa01.vlab.net", user = "adminjig", pwd = "Start1234", sslContext = context)
    #print("Invalid or untrusted certification.")
    
datacenter = si.content.rootFolder.childEntity[0]
folder = datacenter.vmFolder.childEntity[1]
vms = folder.childEntity

for i in vms:
    print(i.name)
    
Disconnect(si)