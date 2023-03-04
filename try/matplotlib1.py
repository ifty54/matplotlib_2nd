#to install, write on terminal- pip install matplotlib
#Checking mpl version
import matplotlib
print(matplotlib.__version__) #3.6.2

#pyplot
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,2])
y = np.array([67,100])

plt.plot(x,y)
plt.show()

#plotting without line
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,2])
y = np.array([67,100])

plt.plot(x,y,'o')
plt.show()

#Multiple points
#pyplot
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,2,6,9])
y = np.array([6,3,12,2])

plt.plot(x,y)
plt.show()

#Default x axis (x will start like 0,1,2,3...)
import matplotlib.pyplot as plt
import numpy as np

y = np.array([6,3,12,2])

plt.plot(y)
plt.show()

#marker
import matplotlib.pyplot as plt
import numpy as np

y = np.array([6,3,12,2])

plt.plot(y, marker = 'o')
plt.show()

#fmt or format strings
import matplotlib.pyplot as plt
import numpy as np

y = np.array([3, 8, 1, 10])

plt.plot(y, 'o:r', ms = 20, mfc='b') #where : shows dot, r is red
#Alternatively, you can write
#plt.plot(y, marker = 'o', ms = 20, mec = 'r', mfc = 'b')
#mfc = marked face color; mec = marked edge color (HexaDec color, {specific name-color like hotpink} input is doable too)
plt.show()


#Scatter Plots
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,4,6,7,8,9,12,13,15,16])
y = np.array([23,24,26,46,36,68,69,80,99,108])
plt.scatter(x,y, color="yellow")

x = np.array([2,3,5,6,7,8,9,14,15,47])
y = np.array([21,25,26,35,46,49,76,77,88,98])
plt.scatter(x,y, color= "red")

plt.show()

#separately color choice
x = np.array([1,4,6,7,8,9,12,13,15,16])
y = np.array([23,24,26,46,36,68,69,80,99,108])

colors = np.array(["yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
sizes = np.array([120,300,600,700,81,41,100,390,800,90])
plt.scatter(x,y, c=colors, cmap='nipy_spectral', s=sizes, alpha=0.5) #alpha measures opacity
plt.title("Heat Map")
plt.colorbar()
plt.show()

#bars
x = ["Manchester United", "Manchester City", 'Chelsea']
y = [400, 350, 500]
plt.bar(x,y, color = 'red', width=0.1) #height is expected too
#plt.barh(x,y) barh is horizontal
plt.show()


#histogram
import numpy as np
x = np.random.normal(180,20,70)

plt.hist(x)
plt.show()

#pie chart

y = np.array([20,25,30,40])
mylabels = ["England", "France", "Portugal", "Uruguay"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]
myexplode = [0.2,0.1,0,0] #explode makes distance
plt.pie(y, labels = mylabels, startangle=290, explode = myexplode, shadow = True, colors=mycolors)
plt.legend(title = "Countries")
plt.show()
