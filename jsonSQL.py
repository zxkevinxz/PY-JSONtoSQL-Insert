import json

inputFile = input("please enter file path: ")
fileName = inputFile[inputFile.rfind("/")+1:inputFile.rfind(".")]


fileIn = open(inputFile, 'r')
fileOut = open('./Insert-{}.sql'.format(fileName), 'a')

testIn = fileIn.read()

test = json.loads(testIn)

sqlScript = ""

for ob in test:
    sql = "INSERT INTO {}(".format(fileName)
    values = " VALUES("
    for key in ob:
        sql = sql + " " + key + ","
        values = values + '{}'.format(ob[key]) + ", "
    sql = sql[0:len(sql)-1] + " )\n"
    values = values[0:len(values)-2] + " );\n"
    sqlScript = sqlScript + sql + values

fileOut.write(sqlScript)
fileIn.close()
fileOut.close()
