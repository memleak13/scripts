"""
torrusEventIndex:       1.3.6.1.4.1.14697.1.1.1.1
torrusEventType:        1.3.6.1.4.1.14697.1.1.1.4
torrusMonitorDesc       1.3.6.1.4.1.14697.1.1.1.9
torrusMonitorEventsEntry    1.3.6.1.4.1.14697.1.1.1
torrusMonitorEventsTable    1.3.6.1.4.1.14697.1.1
torrusMonitorName       1.3.6.1.4.1.14697.1.1.1.3
torrusMonitorPComment       1.3.6.1.4.1.14697.1.1.1.10
torrusPath          1.3.6.1.4.1.14697.1.1.1.5
torrusSeverity          1.3.6.1.4.1.14697.1.1.1.8
torrusTimestamp         1.3.6.1.4.1.14697.1.1.1.6
torrusToken         1.3.6.1.4.1.14697.1.1.1.2
torrusTreeName          1.3.6.1.4.1.14697.1.1.1.7
"""


from pysnmp.entity.rfc3413.oneliner import ntforg
from pysnmp.proto import rfc1902

ntfOrg = ntforg.NotificationOriginator()
"""
ntfOrg.sendNotification(
    ntforg.CommunityData('tbsro'),
    ntforg.UdpTransportTarget(('10.10.10.207', 162)),
    'trap',
    '1.3.6.1.4.1.14697.1',
    ('1.3.6.1.4.1.14697.1.1.1.7', rfc1902.OctetString('TBS')),
    ('1.3.6.1.4.1.14697.1.1.1.8', rfc1902.OctetString('3')),
    ('1.3.6.1.4.1.14697.1.1.1.5', rfc1902.OctetString('/Network/UBR01SHR/Docsis_Upstream/Cable6_1_9_upstream0/SNR')),
    ('1.3.6.1.4.1.14697.1.1.1.3', rfc1902.OctetString('yet_docsis-fecuncor-3')),
    ('1.3.6.1.4.1.14697.1.1.1.9', rfc1902.OctetString('This is a Test Trap')),
    ('1.3.6.1.4.1.14697.1.1.1.10', rfc1902.OctetString('Kili INT, US B'))
)
"""
"""
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
"""
"""
ntfOrg.sendNotification(
    ntforg.CommunityData('tbsro'),
    ntforg.UdpTransportTarget(('10.10.10.207', 162)),
    'trap',
    '1.3.6.1.4.1.14697.1',
    ('1.3.6.1.4.1.14697.1.1.1.1', rfc1902.OctetString('1')),
    ('1.3.6.1.4.1.14697.1.1.1.2', rfc1902.OctetString('T12601')),
    ('1.3.6.1.4.1.14697.1.1.1.3', rfc1902.OctetString('docsis-snr-2')),
    ('1.3.6.1.4.1.14697.1.1.1.4', rfc1902.OctetString('3')),
    ('1.3.6.1.4.1.14697.1.1.1.5', rfc1902.OctetString('/Network/UBR01SHR/Docsis_Upstream/Cable6_2_4_upstream0/SNR')),
    ('1.3.6.1.4.1.14697.1.1.1.6', rfc1902.OctetString('2014-03-15T17:05:00.000-01:00')),
    ('1.3.6.1.4.1.14697.1.1.1.7', rfc1902.OctetString('YETNET')),
    ('1.3.6.1.4.1.14697.1.1.1.8', rfc1902.OctetString('4')),
    ('1.3.6.1.4.1.14697.1.1.1.9', rfc1902.OctetString('Signal/Noise-Ratio lower than 19dB')),
    ('1.3.6.1.4.1.14697.1.1.1.10', rfc1902.OctetString('Graenichen Ost INT, US A'))
)
"""
"""
#sending BGP Notification
ntfOrg.sendNotification(
    ntforg.CommunityData('tbsro'),
    ntforg.UdpTransportTarget(('10.10.10.202', 162)),
    'trap',
    '1.3.6.1.4.1.9.9.41.2.0.1',
    ('1.3.6.1.4.1.9.9.41.1.2.3.1.5', rfc1902.OctetString('This BGP neighbor is Down'))
)
"""
#sending Link Down
#1.3.6.1.6.3.1.1.5.3: linkDown
#1.3.6.1.2.1.2.2.1.2: ifDescr
ntfOrg.sendNotification(
    ntforg.CommunityData('tbsro'),
    ntforg.UdpTransportTarget(('10.10.10.202', 162)),
    'trap',
    '1.3.6.1.6.3.1.1.5.3',
    ('.1.3.6.1.2.1.2.2.1.2', rfc1902.OctetString('Gigabit'))
)