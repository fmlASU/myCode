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
timeRecords = dict()
timeRecords_2 = dict()
visitRecords = dict()
result = []

for oneEntry in attration_table:    
    if "Rides" in oneEntry[4] :
        attractionIDNameMap[oneEntry[1]] = oneEntry[2]
        timeRecords[oneEntry[1]] = 0.0
        timeRecords_2[oneEntry[1]] = 0
        visitRecords[oneEntry[1]] = set()

cur.execute("SELECT * FROM checkin")
checkin = cur.fetchall()

for onecheckin in checkin:

    attractionID = onecheckin[3]
    if attractionID in attractionIDNameMap and onecheckin[4] is not None:

        duration = datetime.strptime(onecheckin[4], '%H:%M:%S') - baseLine
        duration = duration.total_seconds()
        timeRecords[attractionID] += duration
        timeRecords_2[attractionID] += 1

        visitorID = str(onecheckin[1])
        visitRecords[attractionID].add(visitorID)
    else:
        continue

for attractionID in visitRecords.keys() :
    visitRecords[attractionID] = len(visitRecords[attractionID])

for attractionID in timeRecords.keys():
    timeRecords[attractionID] = timeRecords[attractionID] / timeRecords_2[attractionID]

for attractionIDI in timeRecords.keys():
    isItBad = False
    visitRecordI = visitRecords[attractionIDI]
    timeRecordI = timeRecords[attractionIDI]
    for attractionIDJ in timeRecords.keys():
        if(attractionIDI != attractionIDJ):
            visitRecordJ = visitRecords[attractionIDJ]
            timeRecordJ = timeRecords[attractionIDJ]
            if(timeRecordI > timeRecordJ and visitRecordI < visitRecordJ):
                isItBad = True
                break
            else:
                continue
        else:
            continue    
    if(isItBad == False):
        result.append(attractionIDNameMap[attractionIDI])
    else:
        continue    
new_result = [result[0], result[3], result[4]]
print(new_result)
