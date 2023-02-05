'''
week2  Q2
Make a bar chart of total visits to food stalls.

Note: For this question, display the bar chart in the notebook and print the data used to create the bar chart as a list of lists (ex: [['Stall 1', 10], ['Stall 2', 50], ...])

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
Food = dict()  # 字典Thrill Rides保存 相应的attractionID和后续记录游客访问频次
for attraction in attraction_table:
    attID_name[attraction[1]] = attraction[2]
    if attraction[4] == 'Food\r':
        Food[attraction[1]] = []

print(Food)

# 在checkin表格中，统计进入ThrillRides的游客ID
for onerecord in checkin:
    visitorID = onerecord[1]
    attID = onerecord[3]
    if attID in Food.keys():
        
        Food[attID].append(visitorID)

print(Food)


# 统计各个thrillridesID下的游客数量，保存到ThrillRides_count字典中
Food_count = dict()

for attID in Food.keys():
    count = len(Food[attID])
    Food_count[attID] = count
   

print(Food_count)


Food_count_name = []
for k1 in attID_name.keys():
    for k2 in Food_count.keys():
        if k1 == k2:
            Food_count_name.append(attID_name[k1])

print(Food_count_name)

# 提取ThrillRides_count中的values，合并，形成一个新的字典，最终得到attraction name与访问次数对应的字典
Food_count_values = Food_count.values()
print(Food_count_values)
Food_name_values = dict(zip(Food_count_name,Food_count_values))
print(Food_name_values)

pairs = [(k, v) for (k, v) in Food_name_values.items()]
print(pairs)

plt.figure(figsize=(10,9))


fig, ax = plt.subplots()

Food_count = list(Food_count.values())
print(Food_count)
Food_name = list(Food_name_values.keys())
print(Food_name)

ax.bar(Food_name, Food_count)


ax.set_xlabel('Food stalls name', fontsize = 16)
ax.set_ylabel('Visits count', fontsize = 16)
ax.set_title('Visits  to food stalls', fontsize = 16)
plt.tick_params(labelsize = 8)
plt.xticks(rotation = -30)
for a, b in zip(Food_name, Food_count):
    plt.text(a, b + 0.05, b, ha = 'center', va = 'bottom', fontsize = 12)

plt.show()




