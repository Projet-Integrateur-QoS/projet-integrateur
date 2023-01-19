import math
import numpy as np

def geometric_mean(data):
    x = np.prod(data)
    res = math.exp(math.log(x)/len(data))
    return res

def mid_range(data):
    return 0.5*(max(data)+min(data))

def harmonic_mean(data):
    divide = np.sum(1/data)
    return len(data)/divide

def lehmer_mean(data,powerRange:tuple):
    f = lambda x : np.sum(data**x)
    return [f(i-1)/f(i) for i in range(powerRange[0],powerRange[1])]




# scoreTimePriority -> dict with range as string as key and factor as value
# Key -> '5-8' '9- '
# nodePriorities -> dict with node as key and factor as value
# data represents the whole database in a json format
# the json uses a node id per key
def peerTrust(data,alpha=1,beta=1,nodePriorities=None,scoreTimePriority=None,epsilon=0.2,delta=5):

    nodePrioList = []
    scorePrioList = []
    print(data)
    if data:
        histSize = len(data["0"]["ram"])
        nodeNumber = len(data)

        mode = 0
        # Check if no priorities
        if scoreTimePriority:
            mode = 2
            scoreTimeFactorList = []
            for key in scoreTimePriority:
                start = key[0]
                end = key[-1]
                startIndex = 0
                endIndex = histSize
                if start != " ":
                    startIndex = int(start)
                if end != " ":
                    endIndex = int(end)
                for _ in range(startIndex,endIndex):
                    scoreTimeFactorList.append(scoreTimePriority[key])

        if nodePriorities:
            # if time priorities exists the mode will be update too
            mode += 1

        if mode == 0:
            nodePrioList = np.ones(nodeNumber)
            scorePrioList = np.ones(histSize)
        elif mode == 1:
            nodePrioList = nodePriorities
            scorePrioList = np.ones(histSize)
        elif mode == 2:
            nodePrioList = np.ones(nodeNumber)
            scorePrioList = scoreTimeFactorList
        else:
            nodePrioList = nodePriorities
            scorePrioList = scoreTimeFactorList


    scorePrioSum = np.sum(scorePrioList)
    nodeScore = dict()

    for node in data:
        nodeScore[node] = dict()
        print("node: ",node)
        print(nodePrioList)
        maxValue = scorePrioSum + beta*nodePrioList[int(node)]

        sumRam = 0
        sumRamSmall = 0
        sumCpu = 0
        sumCpuSmall = 0

        for i in range(histSize):
            if not data[node]["ram"][i]:
                data[node]["ram"][i] = '0'
            if not data[node]["cpu"][i]:
                data[node]["cpu"][i] = '0'

            print("i",i)

            # Compute scores on the whole window and a reduced window
            sumRam += float(data[node]["ram"][i]) * scorePrioList[i]
            sumCpu += float(data[node]["cpu"][i]) * scorePrioList[i]
            if ( abs(histSize - i ) < delta):
                sumRamSmall += float(data[node]["ram"][i])*scorePrioList[i]
                sumCpuSmall += float(data[node]["cpu"][i])*scorePrioList[i]

        if abs(sumCpu-sumCpuSmall) > epsilon:
            resCpu = sumCpuSmall
        else:
            resCpu = sumCpu
        if abs(sumRam-sumRamSmall) > epsilon:
            resRam = sumRamSmall
        else:
            resRam = sumRam

        resCpu += beta*nodePrioList[int(node)]
        resRam += beta*nodePrioList[int(node)]

        print("index = ",node)
        print("hist size",histSize)
        print("cpu score",float("{:.2f}".format((alpha * resCpu)/maxValue)))
        print("ram score",float("{:.2f}".format((alpha * resRam)/maxValue)))



        nodeScore[node]["cpu_score"] = float("{:.2f}".format((alpha * resCpu)/maxValue))
        nodeScore[node]["ram_score"] = float("{:.2f}".format((alpha * resRam)/maxValue))

    return nodeScore
