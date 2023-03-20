import numpy as np
import matplotlib.pyplot as plt
x=np.random.normal(0,1,200)
y=[]
for i in x:
    noise = np.random.randn()
    yhat=5*i+3 +noise
    y.append(yhat)
fig=plt.figure(figsize=(10,10))
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(x,y)
plt.show()
