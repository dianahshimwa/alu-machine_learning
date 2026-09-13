#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

people = ['Farrah', 'Fred', 'Felicia']
x = np.arange(3)
width = 0.5

apples = fruit[0]
bananas = fruit[1]
oranges = fruit[2]
peaches = fruit[3]

plt.bar(x, apples, width, color='red', label='apples')
plt.bar(x, bananas, width, bottom=apples, color='yellow', label='bananas')
plt.bar(x, oranges, width, bottom=apples + bananas,
        color='#ff8000', label='oranges')
plt.bar(x, peaches, width, bottom=apples + bananas + oranges,
        color='#ffe5b4', label='peaches')

plt.xticks(x, people)
plt.ylabel('Quantity of Fruit')
plt.yticks(np.arange(0, 81, 10))
plt.ylim(0, 80)
plt.title('Number of Fruit per Person')
plt.legend()
plt.show()
