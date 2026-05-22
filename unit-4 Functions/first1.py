#### 
from statistics import mean 
import math 
def getMean(set):
    return mean(set)
def getDeviation(num,set):
    list = []
    for n in set:
        list.append(n-num)
    return list
def getSquaredList(devset):
    list = []
    for i in devset:
        list.append(math.pow(i,2))
    return list 

def getSumList(set):
    sum = 0 
    for s in set:
        sum = sum+s 
    return sum 
dataset = [46,69,32,60,52,41] 
print(f"The mean of the number is {getMean(dataset)}")
print(f"The standard Deviation of the list is {getDeviation(len(dataset),dataset)}")
print(f"The sum of the dataset is {getSumList(dataset)}")
print(f"The get squared of the dataset list {getSumList(dataset)} ")