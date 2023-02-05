'''

week2 Q4
Make a box plot of total visits to rides in the Kiddie Rides category.

Note: For this question, display the box plot in the notebook and print the number of visits to each ride as a list (ex: [3, 4, 5, 6, ...])

'''



import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt

dbName = 'D:\python_test\dinofunworld.db'
con = sql.connect(dbName)
cur = con.cursor()

# 分别从attraction和checkin表格取出所有数据
cur.execute("SELECT * FROM attraction")
attraction_table = cur.fetchall()

cur.execute("SELECT * FROM checkin")
checkin = cur.fetchall()

# 在attraction——table表格category列中找出名字为Thrill Rides所对应的attraction ID和name
# 
attID_name = dict()  # 字典attID_name保存attractionID和name的对应
KiddieRides = dict()  # 字典Thrill Rides保存 相应的attractionID和后续记录游客访问频次
for attraction in attraction_table:
    attID_name[attraction[1]] = attraction[2]
    if attraction[4] == 'Kiddie Rides\r':
        KiddieRides[attraction[1]] = []

print(KiddieRides)

# 在checkin表格中，统计进入ThrillRides的游客ID
for onerecord in checkin:
    visitorID = onerecord[1]
    attID = onerecord[3]
    if attID in KiddieRides.keys():
        
        KiddieRides[attID].append(visitorID)

print(KiddieRides)


# 统计各个thrillridesID下的游客数量，保存到ThrillRides_count字典中
KiddieRides_count = dict()

for attID in KiddieRides.keys():
    count = len(KiddieRides[attID])
    KiddieRides_count[attID] = count
   

print(KiddieRides_count)


KiddieRides_count_name = []
for k1 in attID_name.keys():
    for k2 in KiddieRides_count.keys():
        if k1 == k2:
            KiddieRides_count_name.append(attID_name[k1])

print(KiddieRides_count_name)

# 提取ThrillRides_count中的values，合并，形成一个新的字典，最终得到attraction name与访问次数对应的字典
KiddieRides_count_values = list(KiddieRides_count.values())
print(KiddieRides_count_values)
#KiddieRides_name_values = dict(zip(KiddieRides_count_name,KiddieRides_count_values))
#print(KiddieRides_name_values)

#pairs = KiddieRides_name_values.items() 
#print(pairs)

plt.boxplot(KiddieRides_count_values)
plt.xlabel('Kiddie Rides')
plt.show()