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