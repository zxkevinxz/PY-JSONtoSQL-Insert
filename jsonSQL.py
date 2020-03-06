import json

inputFile = input("please enter file path: ")
fileName = inputFile[inputFile.rfind("/")+1:inputFile.rfind(".")]

fileIn = open(inputFile, 'r')
fileOut = open('./Insert-{}.sql'.format(fileName), 'a')

jsonString = fileIn.read()
table = json.loads(jsonString)
sqlScript = ""

for row in table:
    sql = "INSERT INTO {}(".format(fileName)
    values = " VALUES("
    for key in row:
        sql = sql + " " + key + ","
        values = values + '{}'.format(row[key]) + ", "
    sql = sql[0:len(sql)-1] + " )\n"
    values = values[0:len(values)-2] + " );\n"
    sqlScript = sqlScript + sql + values

fileOut.write(sqlScript)
fileIn.close()
fileOut.close()
