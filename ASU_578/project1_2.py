fileName = 'D:\myCode\ASU_578\\adult.data'
fileObj = open(fileName)

gender_salary = {'> 50k':{}, '<= 50k': {}}

gender_salary['> 50k']['Male'] = 0
gender_salary['> 50k']['Female'] = 0
gender_salary['<= 50k']['Male'] = 0
gender_salary['<= 50k']['Female'] = 0

for oneLine in fileObj:
    Items = oneLine[0: len(oneLine) - 1].split(sep = ',')
    
    for index in Items:
        if Items[14] == ' >50k' and Items[9] == ' Male':
            gender_salary['> 50k']['Male'] += 1
        elif Items[14] == ' >50k' and Items[9] == ' Female':
            gender_salary['> 50k']['Female'] += 1
        elif Items[14] == ' <=50k' and Items[9] == ' Male':
            gender_salary['<= 50k']['Male'] += 1
        elif Items[14] == ' <=50k' and Items[9] == ' Female':
            gender_salary['<= 50k']['Female'] += 1

print(gender_salary)


fileObj.close()