import os
import requests
import time
import trustman
import maths_scorer as ms
from plot import plot
from plot import remove_file
from dotenv import load_dotenv
import vizu as vz

#remove_file("plot")

load_dotenv()

simulator_url = 'http://simulator:' + os.environ['SIMULATOR_PORT']


moy_cpu  = [] 
moy_ram  = []
med_cpu  = []
med_ram  = []
iqv_cpu  = []
iqv_ram  = []
trust_cpu= []
trust_ram= []


while True:
    time.sleep(int(os.environ['SCORER_INTERVAL']))

    payload = {}

    nodes = requests.get(simulator_url).json()
    
    #Initialisation de liste vide de score pour chacune des méthodes
    if (moy_cpu==[] and nodes!={}):
        #Compte le nombre de nodes
        n = vz.nb_nodes(nodes)
        for i in range(n):
            moy_cpu.append([])
            moy_ram.append([])
            med_cpu.append([])
            med_ram.append([])
            iqv_cpu.append([])
            iqv_ram.append([])
            trust_cpu.append([])
            trust_ram.append([])

    #Moyenne de l'historique des Cpus et Ram
    payload = ms.maths(nodes)[0]
    vz.append_m(nodes, moy_cpu, payload, "cpu_score_moy")
    vz.append_m(nodes, moy_ram, payload, "ram_score_moy")
    # plot(payload, "moyenne/cpu", nodes, "cpu_score_moy")
    # plot(payload, "moyenne/ram", nodes, "ram_score_moy")

    #Cpu/Ram median sur l'historique des Cpus et Ram
    payload = ms.maths(nodes)[1]
    vz.append_m(nodes, med_cpu, payload, "cpu_score_med")
    vz.append_m(nodes, med_ram, payload, "ram_score_med")
    # plot(payload, "mediane/cpu", nodes, "cpu_score_med")
    # plot(payload, "mediane/ram", nodes, "ram_score_med")

    #Ecart interquartile sur l'historique des cpus et ram
    payload = ms.maths(nodes)[2]
    vz.append_m(nodes, iqv_cpu, payload, "cpu_score_iqv")
    vz.append_m(nodes, iqv_ram, payload, "ram_score_iqv")
    # plot(payload, "iqv/cpu", nodes, "cpu_score_iqv")
    # plot(payload, "iqv/ram", nodes, "ram_score_iqv")

    #Fonction Trustman
    payload = trustman.Trustman_Scorer(nodes)
    vz.append_m(nodes, trust_cpu, payload, "cpu_score")
    vz.append_m(nodes, trust_ram, payload, "ram_score")
    # plot(payload, "trustman/cpu", nodes, "cpu_score")
    # plot(payload, "trustman/ram", nodes, "ram_score")

    
    #Plot des différentes méthodes en fonction des noeuds si on a au moins un score 
    cpu_l = [moy_cpu, med_cpu, iqv_cpu, trust_cpu]
    ram_l = [moy_ram, med_ram, iqv_ram, trust_ram]
    vz.plot(nodes, cpu_l, ram_l)

    requests.post(simulator_url + '/update_scores', json=payload)
