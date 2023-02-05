import sqlite3 as sql
dbName = 'D:\python_test\dinofunworld.db'
con = sql.connect(dbName)
cur = con.cursor()

cur.execute("SELECT * FROM attraction")
attration_table = cur.fetchall()

attractionIDNameMap = dict()
records = dict()

for oneEntry in attration_table:
    attractionIDNameMap[oneEntry[1]] = oneEntry[2]
    records[oneEntry[1]] = set()

cur.execute("SELECT * FROM checkin")
checkin = cur.fetchall()

for onecheckin in checkin:

    attractionID = onecheckin[3]
    visitorID = str(onecheckin[1])
    records[attractionID].add(visitorID)

final_result = dict()

for ID in records.keys() : 
    final_result[ID] = len(records[ID])

max = 0
maxID = 0
for ID in final_result.keys():
    if max < final_result[ID]:
        max = final_result[ID]
        maxID = ID

print(attractionIDNameMap[maxID])
