"""
The purpose of this script is to list ONLY the modem mac. Not any of the other 
macs on this port. This is done by analysing the mac-address table of the device

The mac address-table has multiple entries. These need to be filtered.
Modem mac addresses start with 000f.The MTA uses the same mac address but is 
in a different vlan.
"""
with open('./mac_address-table.txt','r') as fh:
	d_filtered = {}
	for line in fh:
		#look only for modem macs
		#this should really be done using a regular expression
		if "000f." in line:
			line.rstrip()
			filtered = line.split()
			#check if the key already exists.
			#this might be the case if voice (mta) is provisioned too
			if filtered[4] not in d_filtered:
			    d_filtered[filtered[4]] = filtered[1]
			else:
				print ("key exists! - %s"% filtered[4])
	#sort all keys in dictionary and print 
	for key in sorted(d_filtered.keys()):
		print "%s  :  %s" % (key, d_filtered[key])