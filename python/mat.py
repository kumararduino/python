import matplotlib.pyplot as plt
import numpy as np
plt.ion() ## Note this correction
plt.axis([0,1000,0,1])

i=0
x=list()
y=list()

while i <1000:
    temp_y=np.random.random();
    x.append(i);
    y.append(temp_y);
    plt.scatter(i,temp_y);
    i+=1;
    plt.pause(0.0001)
