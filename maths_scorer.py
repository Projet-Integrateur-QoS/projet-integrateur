#import statistics
import numpy as np
import statistics as st

def list_value(nodes, list, ressource):
    for node in nodes:
        list[int(node)].append(nodes[node][ressource][0])

def maths(nodes):

    payload_moy = dict()
    payload_med = dict()
    payload_iqv = dict()

    for node in nodes:
        payload_moy[node] = {}
        payload_med[node] = {}
        payload_iqv[node] = {}

        cpu_history = [float(cpu) for cpu in nodes[node]["cpu"]]
        ram_history = [float(ram) for ram in nodes[node]["ram"]]

        #moyenne
        cpu_score = round(sum(cpu_history) / len(cpu_history), 2)
        ram_score = round(sum(ram_history) / len(ram_history), 2)
        payload_moy[node]["cpu_score_moy"] = cpu_score
        payload_moy[node]["ram_score_moy"] = ram_score

        #mediane
        cpu_history.sort()
        ram_history.sort()
        cpu_score = np.median(cpu_history)
        ram_score = np.median(ram_history)
        payload_med[node]["cpu_score_med"] = cpu_score
        payload_med[node]["ram_score_med"] = ram_score

        #écart interquartile
        Q1_cpu = np.percentile(cpu_history,25)
        Q3_cpu = np.percentile(cpu_history,75)
        cpu_score = Q3_cpu - Q1_cpu
        Q1_ram = np.percentile(ram_history,25)
        Q3_ram = np.percentile(ram_history,75)  
        ram_score = Q3_ram - Q1_ram
        payload_iqv[node]["cpu_score_iqv"] = cpu_score
        payload_iqv[node]["ram_score_iqv"] = ram_score       
    
    return [payload_moy, payload_med, payload_iqv]

