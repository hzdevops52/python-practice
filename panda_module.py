import pandas

data = pandas.read_csv('emp_data.csv')
print(data)

print(data.salary.min())
print(data.salary.max())
print(data.salary.sum())
print(data.salary.mean())
print(data.salary.median())

max_salary = data[data.salary == data.salary.max()]
print(max_salary)

print(data.emp_name)

#print(data.to_dict())
print(data.salary.to_list())

#change data
data.loc[data.emp_id == 102, 'salary'] = 9000
print(data)

#delete data
find_index = data.index[data.emp_id == 109].to_list()[0]
data = data.drop(find_index)
print(data)

#sorting
data = data.sort_values(by='salary', ascending=False)
print(data)


#add new column
data['bonus'] = data.salary * 0.1
print(data)

#remove column
data = data.drop('bonus', axis=1)
print(data)

#change original file data
data.to_csv('emp_data_modified.csv')