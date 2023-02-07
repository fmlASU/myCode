fileName = 'C:\\temp\myCode\ASU_578\\adult.data'
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

LargerThan50KDataBase = {'age':{}, 'workClass':{}, 'education':{}, 'edu_num':{}, 'martial':{}, 'Occupation':{}, 'relation':{},'race':{},'sex':{},'hours':{}}
LessThan50KDataBase = {'age':{}, 'workClass':{}, 'education':{}, 'edu_num':{}, 'martial':{}, 'Occupation':{}, 'relation':{},'race':{},'sex':{},'hours':{}}

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

    if Items[14] == " <=50K":

        if age in LessThan50KDataBase['age']:
            LessThan50KDataBase['age'][age] += 1
        else:
            LessThan50KDataBase['age'][age] = 1

        if workClass in LessThan50KDataBase['workClass']:
            LessThan50KDataBase['workClass'][workClass] += 1
        else:
            LessThan50KDataBase['workClass'][workClass] = 1  

        if education in LessThan50KDataBase['education']:
            LessThan50KDataBase['education'][education] += 1
        else:
            LessThan50KDataBase['education'][education] = 1  

        if edu_Num in LessThan50KDataBase['edu_num']:
            LessThan50KDataBase['edu_num'][edu_Num] += 1
        else:
            LessThan50KDataBase['edu_num'][edu_Num] = 1       

        if marital in LessThan50KDataBase['martial']:
            LessThan50KDataBase['martial'][marital] += 1
        else:
            LessThan50KDataBase['martial'][marital] = 1    

        if Occupation in LessThan50KDataBase['Occupation']:
            LessThan50KDataBase['Occupation'][Occupation] += 1
        else:
            LessThan50KDataBase['Occupation'][Occupation] = 1    

        if relation in LessThan50KDataBase['relation']:
            LessThan50KDataBase['relation'][relation] += 1
        else:
            LessThan50KDataBase['relation'][relation] = 1    

        if race in LessThan50KDataBase['race']:
            LessThan50KDataBase['race'][race] += 1
        else:
            LessThan50KDataBase['race'][race] = 1    

        if sex in LessThan50KDataBase['sex']:
            LessThan50KDataBase['sex'][sex] += 1
        else:
            LessThan50KDataBase['sex'][sex] = 1    

        if HoursWork in LessThan50KDataBase['hours']:
            LessThan50KDataBase['hours'][HoursWork] += 1
        else:
            LessThan50KDataBase['hours'][HoursWork] = 1
    else:
        if age in LargerThan50KDataBase['age']:
            LargerThan50KDataBase['age'][age] += 1
        else:
            LargerThan50KDataBase['age'][age] = 1

        if workClass in LargerThan50KDataBase['workClass']:
            LargerThan50KDataBase['workClass'][workClass] += 1
        else:
            LargerThan50KDataBase['workClass'][workClass] = 1  

        if education in LargerThan50KDataBase['education']:
            LargerThan50KDataBase['education'][education] += 1
        else:
            LargerThan50KDataBase['education'][education] = 1  

        if edu_Num in LargerThan50KDataBase['edu_num']:
            LargerThan50KDataBase['edu_num'][edu_Num] += 1
        else:
            LargerThan50KDataBase['edu_num'][edu_Num] = 1       

        if marital in LargerThan50KDataBase['martial']:
            LargerThan50KDataBase['martial'][marital] += 1
        else:
            LargerThan50KDataBase['martial'][marital] = 1    

        if Occupation in LargerThan50KDataBase['Occupation']:
            LargerThan50KDataBase['Occupation'][Occupation] += 1
        else:
            LargerThan50KDataBase['Occupation'][Occupation] = 1    

        if relation in LargerThan50KDataBase['relation']:
            LargerThan50KDataBase['relation'][relation] += 1
        else:
            LargerThan50KDataBase['relation'][relation] = 1    

        if race in LargerThan50KDataBase['race']:
            LargerThan50KDataBase['race'][race] += 1
        else:
            LargerThan50KDataBase['race'][race] = 1    

        if sex in LargerThan50KDataBase['sex']:
            LargerThan50KDataBase['sex'][sex] += 1
        else:
            LargerThan50KDataBase['sex'][sex] = 1    

        if HoursWork in LargerThan50KDataBase['hours']:
            LargerThan50KDataBase['hours'][HoursWork] += 1
        else:
            LargerThan50KDataBase['hours'][HoursWork] = 1                                                                            

fileObj.close()