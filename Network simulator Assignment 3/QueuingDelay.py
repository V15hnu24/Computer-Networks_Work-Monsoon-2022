import matplotlib.pyplot as plt
import numpy as np

file = open("C:\\Users\\799vi\\Desktop\\Courses\\Computer networks\\Network simulator Assignment 3\\Q1\\tcp-example.tr", "r")

data = file.readlines()

x = []
y = []

Q = {}

delay_t = 0
packets_t = 0
temp = 0

for i in data:
    j = i.split()

    sequence = int(j[36][4:])
    time = float(j[1])
    enq = j[0]=="+"
    deq = j[0]=="-"

    if enq:
        Q[sequence] = time
    elif deq:
        if sequence in Q:
            u = time - Q[sequence]
            delay_t += time - Q[sequence]
            packets_t += 1

            if len(x) > 0 and x[-1] == time:
                y[-1] = (y[-1] * (temp + u)) / (temp + 1)
                temp += 1
            else:
                temp = 1
                x.append(time)
                y.append(u)

X = np.array(x)
Y = np.array(y)

plt.plot(X, Y,"g")
plt.xlabel("Time")
plt.ylabel("Queuing Delay")
plt.title("Queuing Delay vs Time")
plt.show()