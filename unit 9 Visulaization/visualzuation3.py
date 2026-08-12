import numpy as np 
import matplotlib.pyplot as plt 
 
xover = np.array([1,2,3,4,5])
yrr =  np.array([10,20,30,40,50])
plt.plot(xover,yrr,marker = "H",color = "r",linewidth = "10",mec = "g",mfc = "b",ms = 10)
ycsk = np.array([20,25,30,35,40])
plt.plot(xover,ycsk,marker = "o",color = "b",linewidth = "10",mec = "r",mfc = "g",ms = 10)
plt.title("The Match between csk and RR ")
plt.xlabel("overs")
plt.ylabel("Runs- Red = RR,Blue = CSK ")
plt.show()