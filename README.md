# matplotlib_2nd
#Linestyle, linewidth
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,3,6,8])
plt.plot(x, linestyle ="dotted", linewidth = '20.5') #use "dashed" either
#ls instead linestyle, : to dotted, -- to dashed can e written too
plt.show()

#Multiple lines
x1 = np.array([1,4,12,9])
x2 = np.array([4,14,5,12])

plt.plot(x1)
plt.plot(x2)

plt.show()

#Labels & Titles
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.title("Premier League")
plt.xlabel("Clubs")
plt.ylabel("Countries")
plt.show()


#Font Size & Title Position
import matplotlib.pyplot as plt
import numpy as np

x = np.array([6, 7, 5, 4])
y = np.array([50,47,57,67])

font1 = {'family':'serif', 'color': 'green', 'size': 10}
font2 = {'family':'serif', 'color': 'red', 'size': 20}

plt.title("Players", fontdict= font2, loc = "right")
plt.xlabel("Heights", fontdict= font1)
plt.ylabel("Weights", fontdict= font1)

plt.plot(x)
plt.plot(y)
plt.grid() #adding grid lines
#plt.grid(axis='x') represents showing only y parallel grids
#plt.grid(color='red', linestyle='--', linewidth=0.5)
plt.show()

#multiple plots
import matplotlib.pyplot as plt
import numpy as np

#plot 1
x = np.array([1,3,5,7])
y = np.array([30,20,40,60])

plt.subplot(1,2,1)
plt.plot(x,y)
#plot 2
x = np.array([5,6,9,11])
y = np.array([20,40,48,68])

plt.subplot(1,2,2)
plt.plot(x,y)

plt.show() #for vertically show, subplot(2,1,1) and (2,1,2) is doable

#six plots
import matplotlib.pyplot as plt
import numpy as np
#1st plot
x = np.array([1,2,3,5])
y = np.array([10,20,30,35])
plt.subplot(2,3,1)
plt.plot(x,y)
#2nd plot
x = np.array([3,6,8,9])
y = np.array([1,10,31,30])
plt.subplot(2,3,2)
plt.plot(x,y)
#3rd plot
x = np.array([1,2,3,5])
y = np.array([5,6,7,9])
plt.subplot(2,3,3)
plt.plot(x,y)
#4th plot
x = np.array([2,6,7,3])
y = np.array([5,10,12,23])
plt.subplot(2,3,4)
plt.plot(x,y)
#5th plot
x = np.array([12,14,16,23])
y = np.array([1,4,7,8])
plt.subplot(2,3,5)
plt.plot(x,y)
#6th plot
x = np.array([10,8,5,19])
y = np.array([20,30,40,55])
plt.subplot(2,3,6)
plt.plot(x,y)

plt.suptitle("SIX CLUBS")
plt.show()
