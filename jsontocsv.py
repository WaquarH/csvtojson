import json, csv

csvFilePath ="demo.csv"
jsonFilePath = "happy.json"

with open(jsonFilePath) as file:
	data = json.load(file)
with open(csvFilePath , "w") as file:
	csv_file = csv.writer(file)
	csv_file.writerow(["wid","age","country","gender","marital","parenthood"])
	for i in data["happy"]:	
		csv_file.writerow([data['happy'][i]['wid'],data['happy'][i]['age'],data['happy'][i]['country'],data['happy'][i]['gender'],data['happy'][i]['marital'],data['happy'][i]['parenthood']])
