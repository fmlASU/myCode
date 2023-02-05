import sqlite3 as sql
from datetime import datetime
from datetime import timedelta

baseLine = datetime.strptime('00:00:00', '%H:%M:%S')

dbName = 'D:\python_test\dinofunworld.db'
con = sql.connect(dbName)
cur = con.cursor()

cur.execute("SELECT * FROM attraction")
attration_table = cur.fetchall()

attractionIDNameMap = dict()
records = dict()
records2 = dict()

for oneEntry in attration_table:    
    if "Rides" in oneEntry[4] :
        attractionIDNameMap[oneEntry[1]] = oneEntry[2]
        records[oneEntry[1]] = 0.0
        records2[oneEntry[1]] = 0

cur.execute("SELECT * FROM checkin")
checkin = cur.fetchall()

for onecheckin in checkin:

    attractionID = onecheckin[3]
    if attractionID in attractionIDNameMap and onecheckin[4] is not None:
        duration = datetime.strptime(onecheckin[4], '%H:%M:%S') - baseLine
        duration = duration.total_seconds()
    else:
        continue
    records[attractionID] += duration
    records2[attractionID] += 1

for attractionID in records.keys():
    records[attractionID] = records[attractionID] / records2[attractionID]

maxT = 0.0
maxID = 0
for ID in records.keys():
    if maxT < records[ID]:
        maxT = records[ID]
        maxID = ID
del records[maxID]
maxT = 0.0
maxID = 0
for ID in records.keys():
    if maxT < records[ID]:
        maxT = records[ID]
        maxID = ID
#print("ID=", minID)
#print("Name = ", attractionIDNameMap[minID])
print(attractionIDNameMap[maxID])
