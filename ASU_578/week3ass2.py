



import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt

dbName = 'D:\python_test\dinofunworld.db'
con = sql.connect(dbName)
cur = con.cursor()

# 分别从attraction和checkin表格取出所有数据

cur.execute("SELECT * FROM attraction")
attraction_table = cur.fetchall()

cur.execute("SELECT * FROM sequences")
sequences = cur.fetchall()

attID_Name = dict()
for oneline in attraction_table:
    if 'Rides' in oneline[4]:
        attID_Name[oneline[1]] = oneline[2]

#print(attID_Name)

ColNum = 2
visit_sequences = list()

for record in sequences:
    visit_sequences.append(record[ColNum].split(sep = '-'))

total_time_slot = len(visit_sequences[0])
visitcount = dict()
for attID in attID_Name.keys():
    visitcount[attID] = 0

count = dict()
#for timeslotID in range(total_time_slot):    
#    count[timeslotID] = 0 

print(total_time_slot)


for attID in attID_Name.keys():
    count = dict()
    for visit in visit_sequences:
        for timeslotID in range(total_time_slot):
            count[timeslotID] = 0 
            if int(visit[timeslotID]) == attID:
                count[timeslotID] += 1
            else:
                continue
    visitcount[attID] = count
print(visitcount)