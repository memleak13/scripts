"""
	create slot 2 interface config on asw17shr
	10.07.14
"""

def run():
	line1 = "interface GigabitEthernet3/"
	line2 = "switchport trunk native vlan 62"
 	line3 = "switchport mode trunk"
 	line4 = "ip access-group Net in"
 	line5 = "mac access-group l2 in"
 	line6 = "ip dhcp snooping limit rate 100"
 	line7 = ("ip dhcp snooping vlan 64 information option format-type " 
 			 "circuit-id override string GigabitEthernet3/")
 	line8 = ("ip dhcp snooping vlan 63 information option format-type "
 			 "circuit-id override string GigabitEthernet3/")
 	print "conf t\n"
	for interface in range(1,81):
		print line1 + str(interface)
		print line2
 		print line3
 		print line4
 		print line5
 		print line6
 	 	print line7 + str(interface)
 		print line8 + str(interface) + "\n"
 	print ("end")

if __name__ == "__main__": 
    run()