import matplotlib.pyplot as pt 
import numpy as np 
# subject = np.array(["Science","Math","Computer","Data Science"])
# marks = np.array([30,40,50,60])
# pt.xlabel("Subjects")
# pt.ylabel("Marks")
# pt.bar(subject,marks,color = ["g","b","y","r"])
# pt.show()
### for the piechart 


y = np.array([35,25,30,35])
pt.pie(y,labels = ["python","algebra","math","dbms"],startangle=90,explode= (0.1,0,0,0),shadow = True,autopct = "%1.1f%%")
pt.legend(title = "S")
pt.show()