import numpy as np
import matplotlib.pyplot as plt

# Student name is taken as input
stud_name = input('Enter Your Name: ')

# Semester is taken as input and Semester list is created
num_sem = int(input('Enter Number Of Semesters: '))
sem = list(range(1, num_sem + 1))

# SGPA is taken as input and SGPA list is created
sgpa = []
for i in range(num_sem):
    sgpa.append(float(input('Enter ' + str(i + 1) + ' Semester SGPA: ')))

# sem and sgpa list are converted into numpy arrays: np_sem and np_sgpa
np_sem = np.array(sem)
np_sgpa = np.array(sgpa)

# plot is generated with Semesters on x-axis and sgpa on y-axis
plt.plot(np_sem, np_sgpa)

# plot customizations are added
plt.title('Performance Report Of ' + stud_name)
plt.xlabel('Semesters')
plt.ylabel('SGPA')
plt.xticks(np_sem)

# plot is displayed
plt.show()
