#import statistics
import numpy as np
import statistics as st
import math

def list_value(nodes, list, ressource):
    for node in nodes:
        list[int(node)].append(nodes[node][ressource][0])

def geometric_mean(data):
    x = np.prod(data)
    res = math.exp(math.log(x)/len(data))
    return res

def mid_range(data):
    return 0.5*(max(data)+min(data))

def harmonic_mean(data):
    divide = np.sum(1/data)
    return len(data)/divide

def lehmer_mean(data,power):
    f = lambda x : np.sum(np.power(data,x))
    return f(power-1)/f(power)



def maths(nodes, payload):

    for node in nodes:

        cpu_history = [float(cpu) for cpu in nodes[node]["cpu"]]
        ram_history = [float(ram) for ram in nodes[node]["ram"]]

        #moyenne
        cpu_score = round(sum(cpu_history) / len(cpu_history), 2)
        ram_score = round(sum(ram_history) / len(ram_history), 2)
        payload[node]["cpu_score_moy"] = cpu_score
        payload[node]["ram_score_moy"] = ram_score

        #mediane
        cpu_history.sort()
        ram_history.sort()
        cpu_score = np.median(cpu_history)
        ram_score = np.median(ram_history)
        payload[node]["cpu_score_med"] = cpu_score
        payload[node]["ram_score_med"] = ram_score

        #écart interquartile
        Q1_cpu = np.percentile(cpu_history,25)
        Q3_cpu = np.percentile(cpu_history,75)
        cpu_score = Q3_cpu - Q1_cpu
        Q1_ram = np.percentile(ram_history,25)
        Q3_ram = np.percentile(ram_history,75)
        ram_score = Q3_ram - Q1_ram
        payload[node]["cpu_score_iqv"] = cpu_score
        payload[node]["ram_score_iqv"] = ram_score

        # Geometric mean
        payload[node]["cpu_score_geom"] = geometric_mean(cpu_history)
        payload[node]["ram_score_geom"] = geometric_mean(ram_history)

        # mid range
        payload[node]["cpu_score_range"] = mid_range(cpu_history)
        payload[node]["ram_score_range"] = mid_range(ram_history)

        # Geometric mean
        payload[node]["cpu_score_harmonic"] = harmonic_mean(cpu_history)
        payload[node]["ram_score_harmonic"] = harmonic_mean(ram_history)

        # Geometric mean
        payload[node]["cpu_score_lehmer"] = lehmer_mean(cpu_history,2)
        payload[node]["ram_score_lehmer"] = lehmer_mean(ram_history,2)
