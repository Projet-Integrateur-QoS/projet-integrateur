# Import statistics Library
import statistics
import csv
import numpy as np

CPUNode1 = []
CPUNode2 = []
CPUNode3 = []

RAMNode1 = []
RAMNode2 = []
RAMNode3 = []

lenDataSet = 20000
listNodes = dict()
listTest =[]


def uploadData(path):
    lenDataSet = 0
    with open(path, 'r') as file:
        csvreade = csv.reader(file, delimiter=';')
        for row in csvreade:
            lenDataSet += 1
            CPUNode1.append(float(row[3]))
            CPUNode2.append(float(row[5]))
            CPUNode3.append(float(row[7]))
            RAMNode1.append(float(row[4]))
            RAMNode2.append(float(row[6]))
            RAMNode3.append(float(row[8]))
    print(lenDataSet)


def createNodes(numberOfNodes):
    for i in range(numberOfNodes):
        listNodes[f'Nodes_{i}'] = (1,1)

uploadData("./dataset/value.csv")
print(lenDataSet)

listResource=[(CPUNode1,RAMNode1),(CPUNode2,RAMNode2),(CPUNode3,RAMNode3)]
def dataAnalyze(numberOfNodes):
    median = int(lenDataSet/2)
    print(median)
    for (cpu,ram) in listResource:
        #print(cpu)
        cpu.sort()
        #print(ram)
        ram.sort()
        Q1_Cpu = np.median(cpu[:median])
        Q3_Cpu = np.median(cpu[median:])
        Q1_Ram = np.median(ram[:median])
        Q3_Ram = np.median(ram[median:])

        print("Min CPU :"+ str(cpu[0]))
        print("Min RAM :"+str(ram[0]))
        #print("Max CPU :"+str(cpu[-1]))
        #print("Max RAM :"+str(ram[-1]))

        print("écart min max cpu : "+str(cpu[-1]-cpu[0]))
        print("écart min max ram : "+str(ram[-1]-ram[0]))
        print("median du CPU : "+str(np.median(cpu)))
        print("median de la RAM : "+str(np.median(ram)))
        print("variance du CPU : "+str(np.median(statistics.variance(cpu))))
        print("variance de la RAM : "+str(np.median(statistics.variance(ram))))
        Scor_Cpu = (Q3_Cpu - Q1_Cpu)
        Scor_Ram = (Q3_Ram - Q1_Ram)
        listTest.append((Scor_Cpu,Scor_Ram))


createNodes(3)
dataAnalyze(3)
#print(listResource)
print(listTest)
listTest=[]