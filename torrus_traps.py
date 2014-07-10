 from pysnmp.entity.rfc3413.oneliner import ntforg
from pysnmp.proto import rfc1902

ntfOrg = ntforg.NotificationOriginator()

ntfOrg.sendNotification(
    ntforg.CommunityData('tbsro'),
    ntforg.UdpTransportTarget(('10.10.10.207', 162)),
    'trap',
    '1.3.6.1.4.1.14697.1',
    ('1.3.6.1.4.1.14697.1.1.1.7', rfc1902.OctetString('YETNET'))
)


"""
# I use below script to send torrus traps from torrus to zenoss
from pysnmp.entity.rfc3413.oneliner import ntforg
from pysnmp.proto import rfc1902

ntfOrg = ntforg.NotificationOriginator()
ntfOrg.sendNotification(
                        ntforg.CommunityData('tbsro'),
                        ntforg.UdpTransportTarget(('10.10.10.202', 162)),
                        'trap',
                        '1.3.6.1.4.1.14697.1',
                        ('1.3.6.1.4.1.14697.1.1.1.7', rfc1902.OctetString('TBS')),
                        ('1.3.6.1.4.1.14697.1.1.1.8', rfc1902.OctetString('3')),
                        ('1.3.6.1.4.1.14697.1.1.1.5', rfc1902.OctetString('/Network/UBR01SHR/Docsis_Upstream/Cable6_1_9_upstream0/SNR')),
                        ('1.3.6.1.4.1.14697.1.1.1.3', rfc1902.OctetString('yet_docsis-fecuncor-3')),
                        ('1.3.6.1.4.1.14697.1.1.1.9', rfc1902.OctetString('This is a Test Trap')),
                        ('1.3.6.1.4.1.14697.1.1.1.10', rfc1902.OctetString('Kilimangaro'))
                        )
"""