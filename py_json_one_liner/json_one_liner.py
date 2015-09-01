"""
	This is just a proof of concept. No fancy coding.
	A small script which takes a huge json customer db dump - in one hell of a 
	long line -, filters out the "KundenNr" and the "Passwort" and writes this
	into a separate file.

	customer file: customers.json

	Nice tutorial regarding json: 
	http://xmodulo.com/2013/05/how-to-parse-json-string-in-python.html
"""
import json
with open("./customers.json") as file:
	data = file.readline()
	datasets = json.loads(data)
	#print (json.dumps(decoded, sort_keys=True, indent=4))
	with open("./filtered_json_no_name.txt", "w") as filtered_file:
		for dataset in datasets:
			filtered_file.write(dataset["KundenNr"] + "," +
			dataset["Passwort"]+ "\n")
			"""
			filtered_file.write(dataset["Name"] + "," + dataset["KundenNr"] + "," +
			dataset["Passwort"]+ "\n")
			"""
			#print (dataset)
			#print (dataset["Name"] + "," + dataset["KundenNr"] + "," + 
			#dataset["Passwort"])


