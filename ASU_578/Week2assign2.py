import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
dbName = 'D:\python_test\dinofunworld.db'
conn = sql.connect(dbName)
c = conn.cursor()
c.execute("SELECT * FROM attraction")
att_table = c.fetchall()

records = {}
attIDNameMap = {}

for oneLine in att_table : 
    type = oneLine[5]
    attID = oneLine[1]
    if 'Fast Food' in type :
        records[attID] = 0
        attIDNameMap[attID] = oneLine[2]

c.execute("SELECT * FROM checkin")
checkin_table = c.fetchall()

for oneLine in checkin_table:
    attID = oneLine[3]
    if attID in records :
        records[attID] += 1

results = []
Visit = 0

for attID in records.keys():
    attName = attIDNameMap[attID]
    Visit = records[attID]
    results.append([str(attName), Visit])

print(results)

x= attIDNameMap.values()
y = records.values()

fig, ax = plt.subplots()
autotexts = ax.bar(x, y)
plt.setp(autotexts)
fig.show()