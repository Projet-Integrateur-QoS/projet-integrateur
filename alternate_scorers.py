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





# FIXME - Update max possible value based on prio lists
# FIXME - Only 3 history data -> adapt algorithm  or adapt data sending

# scoreTimePriority -> dict with range as string as key and factor as value
# Key -> '5-8' '9- '
# nodePriorities -> dict with node as key and factor as value
# data represents the whole database in a json format
# the json uses a node id per key
def peerTrust(data,alpha=1,beta=1,nodePriorities=None,scoreTimePriority=None,epsilon=0.2,delta=5):

    print(data)
    if data:
        histSize = len(data["0"]["ram"])
        nodePrioList = []
        scorePrioList = []

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
            nodePrioList = np.ones(histSize)
            scorePrioList = np.ones(histSize)
        elif mode == 1:
            nodePrioList = nodePriorities
            scorePrioList = np.ones(histSize)
        elif mode == 2:
            nodePrioList = np.ones(histSize)
            scorePrioList = scoreTimeFactorList
        else:
            nodePrioList = nodePriorities
            scorePrioList = scoreTimeFactorList


    nodeScore = dict()
    for node in data:
        nodeScore[node] = dict()

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
            sumRam += float(data[node]["ram"][i]) * scorePrioList[i] + (beta*nodePrioList[int(node)])
            sumCpu += float(data[node]["cpu"][i]) * scorePrioList[i] + (beta*nodePrioList[int(node)])
            if ( abs(histSize - i ) < delta):
                sumRamSmall += float(data[node]["ram"][i])*scorePrioList[i] + (beta*nodePrioList[int(node)])
                sumCpuSmall += float(data[node]["cpu"][i])*scorePrioList[i] + (beta*nodePrioList[int(node)])

        if abs(sumCpu-sumCpuSmall) > epsilon:
            resCpu = sumCpuSmall
        else:
            resCpu = sumCpu
        if abs(sumRam-sumRamSmall) > epsilon:
            resRam = sumRamSmall
        else:
            resRam = sumRam

        print("index = ",node)
        print("hist size",histSize)
        print("cpu score",resCpu)
        print("ram score",resRam)
        # max : 1 + 1 for n times
        nodeScore[node]["cpu_score"] = (alpha * resCpu)/(2*histSize)
        nodeScore[node]["ram_score"] = (alpha * resRam)/(2*histSize)

    return nodeScore
