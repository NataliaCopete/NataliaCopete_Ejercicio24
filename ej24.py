import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,20,100)

lambd=np.linspace(1,100,100)


def p(x,l):
  return (1/l)*np.exp(-x/l)

def N(x,l): 
  return np.trapz(p(x,l))

datos=np.array([1.2,2.5,2.8,5.0])

proba=np.copy(lambd)

for i in range(len(lambd)):
  proba[i]=(p(datos[0],lambd[i])*p(datos[1],lambd[i])*p(datos[2],lambd[i])*p(datos[3],lambd[i]))/N(x,lambd[i])


plt.plot(lambd,proba)
plt.xlabel("lambda")
plt.ylabel("probabilidad")
plt.savefig("grafica.png")
   


  
 
