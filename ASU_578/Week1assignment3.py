'''
Which Fast Food offering in the park has the fewest visitors?

Note: Your output should be the name of the fast food offering.

'''


import sqlite3 as sql
dbName = 'D:\python_test\dinofunworld.db'
con = sql.connect(dbName)
cur = con.cursor()

cur.execute("SELECT * FROM attraction")
attration_table = cur.fetchall()

attractionIDNameMap = dict()
records = dict()
visitors = set()

for oneEntry in attration_table:
    attractionIDNameMap[oneEntry[1]] = oneEntry[2]
    if oneEntry[5] == 'Fast Food':
        records[oneEntry[1]] = set()

print(records)
# print(attractionIDNameMap)

cur.execute("SELECT * FROM checkin")
checkin = cur.fetchall()

for onecheckin in checkin:

    attractionID = onecheckin[3]
    visitorID = onecheckin[1]
    visitors.add(visitorID)

    if attractionID in records :
        records[attractionID].add(visitorID)
 
final_result = dict()

for ID in records.keys() : 
    final_result[ID] = len(records[ID])

min = len(visitors) + 1
minID = 0
for ID in final_result.keys():
    if min > final_result[ID]:
        min = final_result[ID]
        minID = ID

#print("ID=", minID)
#print("Name = ", attractionIDNameMap[minID])
print(attractionIDNameMap[minID])
