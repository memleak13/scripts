"""
    Name:     tor_auto_update.py
    Version:  0.1 
    Author:   tltjmo
    Modified: 12.03.14

    This script is run by cron job. It rediscovers, compiles and builds all network devices 
    for torrus. This was done as Yetnet wishes that this happens automatically
    (inserting new lineccards, device descriptions etc ...)
    
    #Todo:
"""


import subprocess
from pysnmp.entity.rfc3413.oneliner import ntforg
from pysnmp.proto import rfc1902

def error_check(error):
        #checks if the discovery or compilations returns with an error
        #if so a snmp trap is sent to yetnet and tbs zenoss
        if error == True:
                print ("- Houston we have a problem! -")
                ntfOrg = ntforg.NotificationOriginator()
                #send notification to yetnet
                ntfOrg.sendNotification(
                        ntforg.CommunityData('tbsro'),
                        ntforg.UdpTransportTarget(('10.10.10.207', 162)),
                        'trap',
                        '1.3.6.1.4.1.14697.1',
                        ('1.3.6.1.4.1.14697.1.1.1.7', rfc1902.OctetString('YETNET')),
                        ('1.3.6.1.4.1.14697.1.1.1.8', rfc1902.OctetString('3')),
                        ('1.3.6.1.4.1.14697.1.1.1.5', rfc1902.OctetString('////tor_auto_update.py')),
                        ('1.3.6.1.4.1.14697.1.1.1.3', rfc1902.OctetString('')),
                        ('1.3.6.1.4.1.14697.1.1.1.9', rfc1902.OctetString('Houston, we have a problem!')),
                        ('1.3.6.1.4.1.14697.1.1.1.10', rfc1902.OctetString('tor_auto_update.py'))
                )
                #send notification to tbs
                ntfOrg.sendNotification(
                        ntforg.CommunityData('tbsro'),
                        ntforg.UdpTransportTarget(('10.10.10.202', 162)),
                        'trap',
                        '1.3.6.1.4.1.14697.1',
                        ('1.3.6.1.4.1.14697.1.1.1.7', rfc1902.OctetString('TBS')),
                        ('1.3.6.1.4.1.14697.1.1.1.8', rfc1902.OctetString('3')),
                        ('1.3.6.1.4.1.14697.1.1.1.5', rfc1902.OctetString('////tor_auto_update.py')),
                        ('1.3.6.1.4.1.14697.1.1.1.3', rfc1902.OctetString('')),
                        ('1.3.6.1.4.1.14697.1.1.1.9', rfc1902.OctetString('Houston, we have a problem!')),
                        ('1.3.6.1.4.1.14697.1.1.1.10', rfc1902.OctetString('tor_auto_update.py'))
                )
                print("- snmp trap has been sent -")
        else:
                print("- no error - ")

def run():
        #discover and compile all ddx files
        print('- processing torrus devdiscover --in=yetnet_ubr.ddx -')
        error = subprocess.call('torrus devdiscover --in=yetnet_ubr.ddx', shell=True)
        error_check(error)
        print('- processing torrus devdiscover --in=yetnet_network.ddx -')
        error = subprocess.call('torrus devdiscover --in=yetnet_network.ddx', shell=True)
        error_check(error)
        print('- processing torrus devdiscover --in=tbsNetwork.ddx -')
        error = subprocess.call('torrus devdiscover --in=tbsNetwork.ddx', shell=True)
        error_check(error)
        print('processing - torrus compile --all -')
        error = subprocess.call('torrus compile --all', shell=True)
        error_check(error)
        print('processing - torrus bs --global -')
        error = subprocess.call('torrus bs --global', shell=True)
        error_check(error)
        print ("- FINITO ... -")


if __name__ == "__main__":
        run()
