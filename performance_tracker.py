import numpy as np
import matplotlib.pyplot as plt

def grade(s):
    if s > 9:
        return "Excellent"
    elif s > 8:
        return "Very Good"
    elif s > 7:
        return "Good"
    elif s > 6:
        return "Average"
    elif s > 5:
        return "Need Improvement"
    else:
        return "Poor"

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

for i in list(range(num_sem)):
    sem_i = np_sem[i]
    sgpa_i = np_sgpa[i]
    plt.text(sem_i, sgpa_i, grade(sgpa_i))

# plot is displayed
plt.show()
