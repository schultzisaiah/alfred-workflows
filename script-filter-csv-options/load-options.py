import sys
import csv
import json

csvFilePath = '/path/to/file.csv'

#Expected CSV format:
#Option Title,Option subtitle or description,agument value to be passed on through workflow

result = ''
with open(csvFilePath) as csvFile:
	csvReader = csv.reader(csvFile, delimiter=',')
	for row in csvReader:
		data = {}
		data['uid'] = row[0]
		data['title'] = row[0]
		data['subtitle'] = row[1]
		data['arg'] = row[2]
		data['autocomplete'] = row[0]
		if result:
			result += ','
		result += json.dumps(data, indent=2)

sys.stdout.write('{"items": [ ' + result + ' ]}')
