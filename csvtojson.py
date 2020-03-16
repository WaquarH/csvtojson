import csv, json
csvFilePath ="demographic.csv"
jsonFilePath = "happy.json"

data = {}
with open(csvFilePath) as csvFile:
	csvReader = csv.DictReader(csvFile)
	for csvRow in csvReader:
		hmid = csvRow["wid"]
		data[hmid] = csvRow
root ={}
root["happy"] = data

# print(data)
with open(jsonFilePath, "w")as jsonFile:
	jsonFile.write(json.dumps(root , indent=4))
