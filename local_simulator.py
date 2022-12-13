from collections import deque
import numpy as np

class Node:


    def __init__(self,id,maxLength=10,x=None,y=None):
        self.id = id
        self.HIST_MAXLEN = maxLength
        self.ram  = deque(maxlen=self.HIST_MAXLEN)
        self.cpu = deque(maxlen=self.HIST_MAXLEN)
        if x and y:
            self.x = x
            self.y = y
        else:
            self.x = 0
            self.y = 0
        self.cpu_score = 1
        self.ram_score = 1


    def get_ram_score(self):
        return self.ram_score

    def get_cpu_score(self):
        return self.cpu_score()


    def add_new_input(self,cpu,ram):
        self.cpu.appendleft(cpu)
        self.ram.appendleft(ram)

    def calculate_score(self,scorer):
        cpu_score,ram_score = scorer(self.cpu,self.ram)
        self.cpu_score = cpu_score
        self.ram_score = ram_score
        return cpu_score,ram_score




def generate_nodes(number):
    nodes = []
    for i in range(number):
        nodes.append((i,Node(i)))
    return nodes

def generate_data(numberNodes,quantity):
    ram = []
    cpu = []
    for i in range(numberNodes):
        dataRam = np.random.random_sample(size = quantity)
        dataCpu = np.random.random_sample(size = quantity)
        cpu.append(list(dataCpu))
        ram.append(list(dataRam))
    return cpu,ram

def init_simulation(nodesNumber):
    nodes = generate_nodes(nodesNumber)
    data = generate_data(nodesNumber,20)
