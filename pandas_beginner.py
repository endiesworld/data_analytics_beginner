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
