#import statistics
import numpy as np
import statistics as st

def list_value(nodes, list, ressource):
    for node in nodes:
        list[int(node)].append(nodes[node][ressource][0])

def maths(nodes, payload):

    for node in nodes:
        node_id = int(node)
        cpu_history = [float(cpu) for cpu in nodes[node]["cpu"]]
        ram_history = [float(ram) for ram in nodes[node]["ram"]]

        #moyenne
        cpu_score = round(sum(cpu_history) / len(cpu_history), 2)
        ram_score = round(sum(ram_history) / len(ram_history), 2)
        payload[node_id]["cpu_score_moy"] = cpu_score
        payload[node_id]["ram_score_moy"] = ram_score

        #mediane
        cpu_history.sort()
        ram_history.sort()
        cpu_score = np.median(cpu_history)
        ram_score = np.median(ram_history)
        payload[node_id]["cpu_score_med"] = cpu_score
        payload[node_id]["ram_score_med"] = ram_score

        #écart interquartile
        Q1_cpu = np.percentile(cpu_history,25)
        Q3_cpu = np.percentile(cpu_history,75)
        cpu_score = Q3_cpu - Q1_cpu
        Q1_ram = np.percentile(ram_history,25)
        Q3_ram = np.percentile(ram_history,75)  
        ram_score = Q3_ram - Q1_ram
        payload[node_id]["cpu_score_iqv"] = cpu_score
        payload[node_id]["ram_score_iqv"] = ram_score       
    
