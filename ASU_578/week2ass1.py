
'''

Q1:
Make a Pie Chart of the visits to Thrill Ride attractions.

Note: For this question, display the pie chart in the notebook and print the data used to create the pie chart as a list of lists (ex: [['Ride 1', 10], ['Ride 2', 100], ...])

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
ThrillRides = dict()  # 字典Thrill Rides保存 相应的attractionID和后续记录游客访问频次
for attraction in attraction_table:
    attID_name[attraction[1]] = attraction[2]
    if attraction[4] == 'Thrill Rides\r':
        ThrillRides[attraction[1]] = []

print(ThrillRides)

# 在checkin表格中，统计进入ThrillRides的游客ID
for onerecord in checkin:
    visitorID = onerecord[1]
    attID = onerecord[3]
    if attID in ThrillRides.keys():
        
        ThrillRides[attID].append(visitorID)

print(ThrillRides)


# 统计各个thrillridesID下的游客数量，保存到ThrillRides_count字典中
ThrillRides_count = dict()

for attID in ThrillRides.keys():
    count = len(ThrillRides[attID])
    ThrillRides_count[attID] = count
   

# print(ThrillRides_count)


# 遍历attID_name和ThrillRides_count, 把ThrillRides_count中attractionID的name对应过来，形成一个列表
ThrillRides_count_name = []
for k1 in attID_name.keys():
    for k2 in ThrillRides_count.keys():
        if k1 == k2:
            ThrillRides_count_name.append(attID_name[k1])

print(ThrillRides_count_name)

# 提取ThrillRides_count中的values，合并，形成一个新的字典，最终得到attraction name与访问次数对应的字典
ThrillRides_count_values = list(ThrillRides_count.values())
print(ThrillRides_count_values)
ThrillRides_name_values = dict(zip(ThrillRides_count_name,ThrillRides_count_values))
print(ThrillRides_name_values)

pairs = [(k, v) for (k, v) in ThrillRides_name_values.items()]
print(pairs)

'''
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        #同时显示数值和占比的饼图
        return '{p: .2f}% ({v:d})'.format(p = pct, v =val)
    return my_autopct
'''

plt.pie(ThrillRides_name_values.values(),labels = ThrillRides_name_values.keys(), shadow = False, autopct = '%.2f%%')
plt.title('visits to Thrill Ride attractions')
plt.show()




