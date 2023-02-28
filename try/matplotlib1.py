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