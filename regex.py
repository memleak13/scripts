"""
	A small script to filter configurations for specific words.
	Writes the matching lines into a seperate file

	http://www.pythonregex.com
"""
import re
def run():
	"""
	#RFGW
	#matches lines with interface and frequency in them
	filter = re.compile (r'.*interface.*|.*frequency.*', re.I)
	filtered = []
	with open('./rfg01SHR.txt','r') as fh_orig_config:
		filtered = [line for line in fh_orig_config if re.search(filter, line)]
	with open('./rfg01SHR_filtered.txt', 'w') as fh_filtered_config:
		for line in filtered:
			fh_filtered_config.write(line)
	"""
 	"""
	#RFGW
	#matches no qam sub interfaces ...Qam9/1, Qam12/12 ... $: End of Line
        filter = re.compile (r'Qam[0-9]{1,2}/[0-9]{1,2}$')
        filtered = []
        with open('./rfg01SHR.txt','r') as fh_orig_config:
                filtered = [line for line in fh_orig_config if re.search(filter, line)]
        with open('./rfg01SHR_filtered.txt', 'w') as fh_filtered_config:
                for line in filtered:
                        fh_filtered_config.write(line)
	"""
	"""
    #RFGW
	#matches QAM admin down interfaces, in "sh int des"
        filter1 = re.compile (r'Qa[0-9]{1,2}/[0-9]{1,2}\s')
        filter2 = re.compile (r'admin')
        filtered = []
        with open('./rfg_int','r') as fh_orig_config:
                filtered = [line for line in fh_orig_config if re.search(filter1, line)
                        and re.search(filter2, line)]
        with open('./rfg_int_f.txt', 'w') as fh_filtered_config:
                for line in filtered:
                        fh_filtered_config.write(line)
			print line
	"""
	"""
	#CMTS
	filter1 = re.compile (r'.*Ca[0-9].*')
	filter2 = re.compile (r'.*up.*')
        filtered = []
        with open('./ubr_int','r') as fh_orig_config:
                filtered = [line for line in fh_orig_config if re.search(filter1, line)
			and re.search(filter2, line)]
        with open('./ubr_filtered.txt', 'w') as fh_filtered_config:
                for line in filtered:
                        fh_filtered_config.write(line)
	"""
	"""
	#Zabbix, filter IfType for upstream Interfaces
	line = "docsCableUpstream12345"
	filter1 = re.compile (r'^docsCableUpstream($|.*)') #String can end ($) or have more chars
	if re.search(filter1, line):
		print ("true")
  	else:
  		print ("false")
  	"""
	"""
 	#Checks if a pattern (bgp) is NOT in a String
 	#http://www.regular-expressions.info/lookaround.html#lookahead
 	#^ - beginning of line
 	#$ - end of line
 	#(?!stringToExclude) - negative lookahead - do not match overall if stringToExclude matches
 	#.(?!stringToExclude) - match any character (.) provided it is not followed by the stringToExclude
 	#(.(?!stringToExclude))* - match zero or more of the above characters (*)

 	#filter1 works: if bgp is not in end of string, then true
 	#filter2 does not works: if bgp is not at the beginning of the string, then true
 	#filter3 does not work - middle of the string
	line = "bgp-test-bgp-test"
	filter1 = re.compile (r'.*(?<!bgp)$')
	filter2 = re.compile (r'^(?<!bgp).*$')
	filter3 = re.compile (r'^.*(?<!bgp).*$')
	if re.search(filter2, line):
		print ("true")
  	else:
  		print ("false")
	"""
	#Only Interfaces that starts with Gi
	line = "TenGigabitEthernet3/2"
	filter1 = re.compile (r'^Gi.*$')
	if re.search(filter1, line):
		print ("true")
	else:
		print ("false")


if __name__ == "__main__":
    run()
