import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('emp_data.csv')
plt.plot(data.emp_id, data.salary)
plt.show()