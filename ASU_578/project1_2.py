import matplotlib.pyplot as plt
from operator import itemgetter
#from matplotlib.pyplot import MultipleLocator
import matplotlib.ticker as ticker
from pandas import DataFrame

fileName = 'D:\myCode\ASU_578\\adult.data'
fileObj = open(fileName)

ageIndex = 0
workClassIndex = 1
educationIndex = 3
edu_NumIndex = 4
maritalIndex = 5
OccupationIndex = 6
relationIndex = 7
raceIndex = 8
sexIndex = 9
HoursWorkIndex = 12
nativecountryIndex = 13

LargerThan50KDataBase = {'age':{}, 'workClass':{}, 'education':{}, 'edu_num':{}, 'martial':{}, 'Occupation':{}, 'relation':{},'race':{},'sex':{},'hours':{}, 'nativecountry':{}}
LessThan50KDataBase = {'age':{}, 'workClass':{}, 'education':{}, 'edu_num':{}, 'martial':{}, 'Occupation':{}, 'relation':{},'race':{},'sex':{},'hours':{}, 'nativecountry':{}}

for oneLine in fileObj:

    if len(oneLine) < 15:
        continue

    Items = oneLine[0: len(oneLine) - 1].split(sep = ',')

    age = Items[ageIndex]
    workClass = Items[workClassIndex]
    education = Items[educationIndex]
    edu_Num = Items[edu_NumIndex]
    marital = Items[maritalIndex]
    Occupation = Items[OccupationIndex]
    relation = Items[relationIndex]
    race = Items[raceIndex]
    sex = Items[sexIndex]
    HoursWork = Items[HoursWorkIndex]
    nativecountry = Items[nativecountryIndex]

    if Items[14] == " <=50K":
        
        if not '?' in age:
            if  age in LessThan50KDataBase['age']:
                LessThan50KDataBase['age'][age] += 1
            else:
                LessThan50KDataBase['age'][age] = 1

        if not '?' in workClass:
            if workClass in LessThan50KDataBase['workClass']:
                LessThan50KDataBase['workClass'][workClass] += 1
            else:
                LessThan50KDataBase['workClass'][workClass] = 1  

        if not '?' in education:
            if  education in LessThan50KDataBase['education']:
                LessThan50KDataBase['education'][education] += 1
            else:
                LessThan50KDataBase['education'][education] = 1  

        if not '?' in edu_Num:
            if  edu_Num in LessThan50KDataBase['edu_num']:
                LessThan50KDataBase['edu_num'][edu_Num] += 1
            else:
                LessThan50KDataBase['edu_num'][edu_Num] = 1       

        if not '?' in marital:
            if marital in LessThan50KDataBase['martial']:
                LessThan50KDataBase['martial'][marital] += 1
            else:
                LessThan50KDataBase['martial'][marital] = 1    

        if not '?' in Occupation:
            if Occupation in LessThan50KDataBase['Occupation']:
                LessThan50KDataBase['Occupation'][Occupation] += 1
            else:
                LessThan50KDataBase['Occupation'][Occupation] = 1    

        if not '?' in relation:
            if relation in LessThan50KDataBase['relation']:
                LessThan50KDataBase['relation'][relation] += 1
            else:
                LessThan50KDataBase['relation'][relation] = 1    

        if not '?' in race:
            if race  in LessThan50KDataBase['race']:
                LessThan50KDataBase['race'][race] += 1
            else:
                LessThan50KDataBase['race'][race] = 1    

        if not '?' in sex:
            if sex in LessThan50KDataBase['sex']:
                LessThan50KDataBase['sex'][sex] += 1
            else:
                LessThan50KDataBase['sex'][sex] = 1    

        if not '?' in HoursWork:
            if HoursWork in LessThan50KDataBase['hours']:
                LessThan50KDataBase['hours'][HoursWork] += 1
            else:
                LessThan50KDataBase['hours'][HoursWork] = 1
        
        if not '?' in nativecountry:
            if nativecountry in LessThan50KDataBase['nativecountry']:
                LessThan50KDataBase['nativecountry'][nativecountry] += 1
            else:
                LessThan50KDataBase['nativecountry'][nativecountry] = 1


    else:
        if not '?' in age:
            if age in LargerThan50KDataBase['age']:
                LargerThan50KDataBase['age'][age] += 1
            else:
                LargerThan50KDataBase['age'][age] = 1

        if not '?' in workClass:
            if workClass in LargerThan50KDataBase['workClass']:
                LargerThan50KDataBase['workClass'][workClass] += 1
            else:
                LargerThan50KDataBase['workClass'][workClass] = 1  

        if not '?' in education:
            if education in LargerThan50KDataBase['education']:
                LargerThan50KDataBase['education'][education] += 1
            else:
                LargerThan50KDataBase['education'][education] = 1  

        if not '?' in edu_Num:
            if edu_Num in LargerThan50KDataBase['edu_num']:
                LargerThan50KDataBase['edu_num'][edu_Num] += 1
            else:
                LargerThan50KDataBase['edu_num'][edu_Num] = 1       

        if not '?' in marital:
            if marital in LargerThan50KDataBase['martial']:
                LargerThan50KDataBase['martial'][marital] += 1
            else:
                LargerThan50KDataBase['martial'][marital] = 1    

        if not '?' in Occupation:
            if Occupation in LargerThan50KDataBase['Occupation']:
                LargerThan50KDataBase['Occupation'][Occupation] += 1
            else:
                LargerThan50KDataBase['Occupation'][Occupation] = 1    

        if not '?' in relation:
            if relation in LargerThan50KDataBase['relation']:
                LargerThan50KDataBase['relation'][relation] += 1
            else:
                LargerThan50KDataBase['relation'][relation] = 1    

        if not '?' in race:
            if race in LargerThan50KDataBase['race']:
                LargerThan50KDataBase['race'][race] += 1
            else:
                LargerThan50KDataBase['race'][race] = 1    

        if not '?' in sex:
            if sex in LargerThan50KDataBase['sex']:
                LargerThan50KDataBase['sex'][sex] += 1
            else:
                LargerThan50KDataBase['sex'][sex] = 1    

        if not '?' in HoursWork:
            if HoursWork in LargerThan50KDataBase['hours']:
                LargerThan50KDataBase['hours'][HoursWork] += 1
            else:
                LargerThan50KDataBase['hours'][HoursWork] = 1

        if not '?' in nativecountry:
            if nativecountry in LargerThan50KDataBase['nativecountry']:
                LargerThan50KDataBase['nativecountry'][nativecountry] += 1
            else:
                LargerThan50KDataBase['nativecountry'][nativecountry] = 1


## 获取两组salary下的年龄数据(done)
'''
# 提取age参数，并排序，但是因为在LargerThan50KDataBase['age']字典中，key尽管都是年龄数字，但都是字符串。在出图时，无法对字符串限定范围，故需要先把年龄转换成整型，然后就可以限定x轴范围和设置步长
UpAgeX = sorted(LargerThan50KDataBase['age'].keys())
UpAgex = []
for upagex in UpAgeX:
    UpAgex.append(int(upagex))
UpAgeY = []
for key in UpAgeX:
    UpAgeY.append(LargerThan50KDataBase['age'][key])

DownAgeX = sorted(LessThan50KDataBase['age'].keys())
DownAgex = []
for downagex in DownAgeX:
    DownAgex.append(int(downagex))
DownAgeY = []
for key in DownAgeX:
    DownAgeY.append(LessThan50KDataBase['age'][key])



plt.figure(figsize = (12,10))
plt.figure(1)
#设置图字尺寸，上下并列布置图形。（211）表示2行1列，最后的1表示排列在上面的图，
ax1 = plt.subplot(211)

plt.plot(UpAgex,UpAgeY, label = 'Salary > 50K', color = 'y')
plt.title('Relationship between age and salary ', fontsize = 18)
plt.ylabel('Counts', fontsize = 14)

ax1.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(100))
plt.xlim((15, 90))

plt.ylim((0, 900))

plt.legend()

ax2 = plt.subplot(212)  # （212）表示2行1列，最后的2表示排列在下面的图，
plt.plot(DownAgex,DownAgeY, label = 'Salary <= 50K',color = 'r')
plt.xlabel('Age', fontsize = 14)
plt.ylabel('Counts', fontsize = 14)
#ax2 = plt.axes()
ax2.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax2.yaxis.set_major_locator(ticker.MultipleLocator(100))
plt.xlim((15, 95))
plt.ylim(0, 900)

plt.legend()
plt.show()
'''


## 获取两组salary下education数据(not done)

'''
UpEdu_num = LargerThan50KDataBase['edu_num']
UpEdu_numX = UpEdu_num.keys()
UpEdu_numx1 = []
for upedu_numx in UpEdu_numX:
    UpEdu_numx1.append(int(upedu_numx))
UpEdu_numx2 = sorted(UpEdu_numx1)
UpEdu_numY = []
for num in UpEdu_numx2:
    print(num)
    UpEdu_numY.append(UpEdu_num[' num'])

DownEdu_numX = sorted(LessThan50KDataBase['edu_num'].keys())
DownEdu_numx = []
for downedu_numx in DownEdu_numX:
    DownEdu_numx.append(int(downedu_numx))
DownEdu_numY = []
for key in DownEdu_numX:
    DownEdu_numY.append(LessThan50KDataBase['edu_num'][key])


plt.figure(figsize = (12,10))
plt.figure(1)

ax1 = plt.subplot(211)

plt.plot(UpEdu_numx,UpEdu_numY, label = 'Salary > 50K', color = 'y')
plt.title('Relationship between education and salary ', fontsize = 18)
plt.ylabel('Counts', fontsize = 14)


ax1.yaxis.set_major_locator(ticker.MultipleLocator(200))


#plt.ylim((0, 900))

plt.legend()

ax2 = plt.subplot(212)  # （212）表示2行1列，最后的2表示排列在下面的图，
plt.plot(DownEdu_numx,DownEdu_numY, label = 'Salary <= 50K',color = 'r')
plt.xlabel('Education', fontsize = 14)
plt.ylabel('Counts', fontsize = 14)
plt.legend()

plt.show()

'''


# 获取性别和工资的关系(done)

'''
Upgender = LargerThan50KDataBase['sex']
Downgender = LessThan50KDataBase['sex']

plt.figure(figsize = (12,10))  # 创建画布尺寸
fig, axes = plt.subplots(1, 2)  # 创建1行2列的矩阵

axes[0].pie(Upgender.values(), labels = Upgender.keys(), shadow = False, autopct = '%.2f%%')
#axes[0].legend(loc = 'best')
axes[0].set_title('Pie Chart of gender at salary > 50K', fontsize = 18)

axes[1].pie(Downgender.values(), labels = Downgender.keys(), shadow = False, autopct = '%.2f%%')
#axes[1].legend(loc = 'best')
axes[1].set_title('Pie Chart of gender at salary <= 50K', fontsize = 18)

plt.show()

'''

# 获取workclass与salary关系(done)
'''
Upworkclass = LargerThan50KDataBase['workClass']
Downworkclass = LessThan50KDataBase['workClass']

# pie chart
plt.figure(figsize = (12,10))  # 创建画布尺寸
fig, axes = plt.subplots(1, 2)  # 创建1行2列的矩阵

axes[0].pie(Upworkclass.values(), labels = Upworkclass.keys(), shadow = False, autopct = '%.2f%%')
#axes[0].legend(loc = 'best')
axes[0].set_title('Pie Chart of workclass at salary > 50K', fontsize = 18)

axes[1].pie(Downworkclass.values(), labels = Downworkclass.keys(), shadow = False, autopct = '%.2f%%')
#axes[1].legend(loc = 'best')
axes[1].set_title('Pie Chart of workclass at salary <= 50K', fontsize = 18)

plt.show()

# bar chart

plt.figure(figsize = (12,10))
plt.figure(1)
#设置图字尺寸，上下并列布置图形。（211）表示2行1列，最后的1表示排列在上面的图，
ax1 = plt.subplot(211)

plt.bar(Upworkclass.keys(), Upworkclass.values(), label = 'Salary > 50K', color = 'y')
plt.title('Relationship between workclass and salary ', fontsize = 20)
plt.ylabel('Counts', fontsize = 14)

#plt.ylim((0, 900))
for a, b in Upworkclass.items():
    plt.text(a, b + 0.05, b, ha = 'center', va = 'bottom', fontsize = 12)
plt.legend(fontsize = 14)

ax2 = plt.subplot(212)  # （212）表示2行1列，最后的2表示排列在下面的图，
plt.bar(Downworkclass.keys(), Downworkclass.values(), label = 'Salary <= 50K',color = 'r')
plt.xlabel('Workclass', fontsize = 14)
plt.ylabel('Counts', fontsize = 14)

for a, b in Downworkclass.items():
    plt.text(a, b + 0.05, b, ha = 'center', va = 'bottom', fontsize = 12)
#ax2.yaxis.set_major_locator(ticker.MultipleLocator(100))

#plt.ylim(0, 900)

plt.legend(fontsize = 14)
plt.show()
'''

# salary VS race

Uprace = LargerThan50KDataBase['race']
Downrace = LessThan50KDataBase['race']

Race = [' White', ' Black', ' Asian-Pac-Islander', ' Other', ' Amer-Indian-Eskimo']

Upracepercent = {}
Downracepercent = {}
for ra in Race:
    Upracepercent[ra] =  '%.2f%%' % (Uprace[ra] * 100 / (Uprace[ra] + Downrace[ra]))
    Downracepercent[ra] = '%.2f%%' % (Downrace[ra] * 100 / (Uprace[ra] + Downrace[ra]))

Upracepercent_float = []
Downracepercent_float = []

for upkey in Upracepercent.keys():
    Upracepercent_float.append(Upracepercent[upkey])

for downkey in Downracepercent.keys():
    Downracepercent_float.append(Downracepercent[downkey])

df_Upracepercent = DataFrame({'Upracepercent_float': Upracepercent_float})
Upracepercent100 = df_Upracepercent['Upracepercent_float'].str.strip('%').astype(float)/100

Upracepercent100_2 = Upracepercent100.apply(lambda x: format(x, '.2%'))

'''
df = DataFrame({'p_str': ['10.33%','23.22%','56%','35.786%','99.0009%']})

p_float = df['p_str'].str.strip("%").astype(float)/100

p_str_2 = p_float.apply(lambda x: format(x, '.2%'))
'''

plt.figure(figsize = (12,10))
plt.figure(1)
#设置图字尺寸，上下并列布置图形。（211）表示2行1列，最后的1表示排列在上面的图，
ax1 = plt.subplot(211)

plt.bar(Race, Upracepercent_float, label = 'Salary > 50K', color = 'y')
plt.title('Relationship between Race and Income ', fontsize = 20)
plt.ylabel('Counts', fontsize = 14)


plt.legend(fontsize = 14)

ax2 = plt.subplot(212)  # （212）表示2行1列，最后的2表示排列在下面的图，
plt.bar(Race, Downracepercent_float, label = 'Salary <= 50K',color = 'r')
plt.xlabel('Race', fontsize = 14)
plt.ylabel('Percent', fontsize = 14)




plt.legend(fontsize = 14)
plt.show()


fileObj.close()