import numpy as np
import matplotlib.pyplot as plt

marks = np.array([80, 89, 93, 81, 85, 90, 92, 87])
subjects = ['english', 'social', 'science', 'c-maths',
            'opt-maths', 'population', 'economics', 'history']
colors = ['red', 'orange', 'yellow', 'blue', 'cyan', 'green', '#e809c3', '#a3a0a3']
explode = [0] * 8
explode[0] = 0.2
wedges, texts, autotexts = plt.pie(marks, labels=subjects, colors=colors
                                   , autopct='%1.0f%%', shadow=True, startangle=45,
                                   explode=explode)
plt.legend(wedges, subjects, loc='right', bbox_to_anchor=(1.5, 0, 0.5, 1))
