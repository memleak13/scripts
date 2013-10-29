"""
	A small script to filter configurations for specific words.
	Writes the matching lines into a seperate file
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


if __name__ == "__main__": 
    run()