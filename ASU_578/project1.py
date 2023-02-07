import pandas as pd
import numpy as np

'''
#data = pd.read_csv('D:\myCode\ASU_578\\adult.data')

columns = ['Age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capitol-gain', 'capitol-loss', 'hour-per-week', 'native-country', 'salary']

data = pd.read_csv('D:\myCode\ASU_578\\adult.data', header = None, names = columns)

print(data)

gender_salary = {'> 50k':{}, '<= 50k': {}}

gender_salary['> 50k']['Male'] = 0
gender_salary['> 50k']['Female'] = 0
gender_salary['<= 50k']['Male'] = 0
gender_salary['<= 50k']['Female'] = 0

for row in data.iterTuples():
    if row['salary'] == '>50k' :
        if row['sex'] == 'Male':
            gender_salary['> 50k']['Male'] += 1
        else:
            gender_salary['> 50k']['Female'] += 1
    elif row['salary'] == '<=50k' :
        if row['sex'] == 'Male':
            gender_salary['<= 50k']['Male'] += 1
        else:
            gender_salary['<= 50k']['Female'] += 1

print(gender_salary)

'''




columns = ['Age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capitol-gain', 'capitol-loss', 'hour-per-week', 'native-country', 'salary']

data = pd.read_csv('D:\myCode\ASU_578\\adult.data', header = None, names = columns)

print(data)


result_by_salary = data.groupby(['salary', 'sex'])
finalcount = result_by_salary.value_counts()
print(finalcount)

pass


#clean_data[column] = clean_data[column].apply(lambda x : x.strip() if x. ,→strip() != '?' else None)

