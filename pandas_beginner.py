import pandas as pd

name = ['Emmanuel', 'Adaobi', 'Dubem', 'Kamuma']
age = [35, 29, 9, 2]
sex = ['M', 'F', 'M', 'F']

my_dict = {'Name': name, 'Age': age, 'Sex': sex}

my_family = pd.DataFrame(my_dict)

print(my_family)
print(my_family['Age'])

new_age = pd.Series([35, 30, 10, 2], name='Age')

# Set row label

my_family.index = ['Father', 'Mother', 'Son', 'Daughter']
print(my_family)

# Row base index using loc

row_0_element = my_family.loc['Father']
row_0_ele_list = my_family.loc[['Father']]
print(row_0_element)
print(row_0_ele_list)

row_0_and_2 = my_family.loc[['Father', 'Son']]
print(row_0_and_2)
print(my_family['Father': 'Mother'])

print(my_family.loc[['Father', 'Daughter'], ['Name', 'Age']])

print(my_family.loc[:, ['Name', 'Age']])

# Row base index using iloc. This is same as loc, the only difference is how data s referenced

print(my_family.iloc[[0, 2, 3], [0, 2]])
print("************ Using pandas series method ********************")
print(my_family[my_family['Name'].str.len() > 5])

print("**************************************************")
print(type(my_family))
