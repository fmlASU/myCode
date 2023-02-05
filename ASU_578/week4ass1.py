

import sqlite3 as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dbName = 'D:\python_test\dinofunworld.db'
con = sql.connect(dbName)
cur = con.cursor()

# 分别从attraction和checkin表格取出所有数据
#cur.execute("SELECT * FROM attraction")
#attraction_table = cur.fetchall()

cur.execute("SELECT * FROM sequences")
sequences = cur.fetchall()

# print(sequences)

TargetAttID = '8'  # 目标attractionID

TimeSlotIDList = []
CountList = []
TotalTimeSlot = 576

count = dict()
for TimeSlotID in range(TotalTimeSlot ):
    count[TimeSlotID] = 0
    TimeSlotIDList.append(TimeSlotID)


for oneline in sequences:
    Timeseq = oneline[2].split(sep = '-')
    for TimeSlotID in range(len(Timeseq)):
        if Timeseq[TimeSlotID] == TargetAttID:
            count[TimeSlotID] += 1
#print(count)

for TimeSlotID in count.keys():
    CountList.append(count[TimeSlotID])

print('Attendance at Atmosfear Rides = ', CountList)

# FinalCount = {'TimeSlotID': TimeSlotIDList, 'Attendance': CountList}

#FinalCount_df = pd.DataFrame.from_dict(FinalCount)
Mean = np.mean(CountList)
std = np.nanstd(CountList)

print('Average Attendance = ', Mean)
print('Standard deviation = ', std)
#print(FinalCount_df)
#TimeSlotID = TimeSlotIDList
#Attendance = CountList

Positive2std = Mean + 2*std  
Positive1std = Mean + std 
Nagative2std = Mean - 2*std 
Nagative1std = Mean - std 

#plt.plot(TimeSlotID, Attendance, label = 'Attendance for three days', color = 'b')

plt.plot(TimeSlotIDList, CountList, label = 'Attendance for three days', color = 'b')
plt.axhline(y = Mean, label = 'mean attendance', color = 'orange')
plt.axhline(y = Positive2std, label = 'two standard deviation bands', color = 'g')
plt.axhline(y = Nagative2std, color = 'g')
plt.axhline(y = Positive1std, label = 'one standard deviation bands',color = 'r')
plt.axhline(y = Nagative1std, color = 'r')
plt.title('Attendance, mean, one and two standard deviation bands at Atmosfear Rides', fontsize = 16)
plt.xlabel('TimeSlotID', fontsize = 14)
plt.ylabel('Attendance', fontsize = 14)
plt.xlim((0, 600))
#plt.ylim((-25, 350))
plt.legend()
plt.show()

pass

