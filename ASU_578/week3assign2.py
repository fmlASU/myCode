import sqlite3 as sql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates



dbName = 'D:\python_test\dinofunworld.db'
con = sql.connect(dbName)
cur = con.cursor()

cur.execute("SELECT * FROM attraction")
attraction_table = cur.fetchall()

cur.execute("SELECT * FROM sequences")
sequences = cur.fetchall()

rides = {}
records = {}
NameList = []
MinList = []
MaxList = []
AvgList = []

for oneLine in attraction_table:
    AttID = oneLine[1]
    AttName = oneLine[2]
    Category = oneLine[4]
    if 'Rides' in Category:
        rides[AttID] = AttName
        records[AttName] = [0] * 576
        NameList.append(AttName)

for oneLine in sequences:
    Timeseq = oneLine[2].split(sep = '-')
    for TimeSlotID in range(len(Timeseq)):
        AttID = int(Timeseq[TimeSlotID])
        if AttID in rides:
            AttName = rides[AttID]     # AttID对应的是数字，所以需要重新给AttName赋值
            records[AttName][TimeSlotID] += 1

#print(records)
result = {}

for AttName in records.keys():
    AttID_visit_InOrder = sorted(records[AttName])

    result[AttName] = {}

    for index in range(len(AttID_visit_InOrder)):
        if AttID_visit_InOrder[index] != 0:
            result[AttName]['min'] = AttID_visit_InOrder[index]
            break
    
    result[AttName]['avg'] = np.mean(AttID_visit_InOrder)
    result[AttName]['max'] = max(AttID_visit_InOrder)

#print(result)

for ID in range(len(NameList)):
    AttName = NameList[ID]
    minValue = result[AttName]['min']
    maxValue = result[AttName]['max']
    avgValue = result[AttName]['avg']
    MinList.append(minValue)
    MaxList.append(maxValue)
    AvgList.append(avgValue)

FinalResult = {'Name': NameList, 'min': MinList, 'avg': AvgList, 'max': MaxList}


result_df = pd.DataFrame.from_dict(FinalResult)

print(result_df)
parallel_coordinates(result_df, 'Name')
plt.title('Min, Avg and Max Attendance at each Rides')
plt.ylabel('Attendance')
plt.legend(bbox_to_anchor= (1.01, 1), loc = 2, borderaxespad = 0, fontsize = 8)
plt.show()
pass
