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
value_cpu= []
value_ram= []


while True:
    time.sleep(int(os.environ['SCORER_INTERVAL']))


    nodes = requests.get(simulator_url).json()

    payload = {}
    for node in nodes:
        payload[node] = dict()

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
            value_cpu.append([])
            value_ram.append([])

    #Calcul des nouveaux scores de chaque fonction
    ms.maths(nodes, payload)

    #Moyenne de l'historique des Cpus et Ram
    vz.append_m(nodes, moy_cpu, payload, "cpu_score_moy")
    vz.append_m(nodes, moy_ram, payload, "ram_score_moy")
    # plot(payload, "moyenne/cpu", nodes, "cpu_score_moy")
    # plot(payload, "moyenne/ram", nodes, "ram_score_moy")

    #Cpu/Ram median sur l'historique des Cpus et Ram
    vz.append_m(nodes, med_cpu, payload, "cpu_score_med")
    vz.append_m(nodes, med_ram, payload, "ram_score_med")
    # plot(payload, "mediane/cpu", nodes, "cpu_score_med")
    # plot(payload, "mediane/ram", nodes, "ram_score_med")

    #Ecart interquartile sur l'historique des cpus et ram
    vz.append_m(nodes, iqv_cpu, payload, "cpu_score_iqv")
    vz.append_m(nodes, iqv_ram, payload, "ram_score_iqv")
    # plot(payload, "iqv/cpu", nodes, "cpu_score_iqv")
    # plot(payload, "iqv/ram", nodes, "ram_score_iqv")

    #Fonction Trustman
    trustman.Trustman_Scorer(nodes, payload)
    vz.append_m(nodes, trust_cpu, payload, "cpu_score_trust")
    vz.append_m(nodes, trust_ram, payload, "ram_score_trust")
    # plot(payload, "trustman/cpu", nodes, "cpu_score")
    # plot(payload, "trustman/ram", nodes, "ram_score")

    ms.list_value(nodes, value_cpu, "cpu")
    ms.list_value(nodes, value_ram, "ram")

    #Plot des différentes méthodes en fonction des noeuds si on a au moins un score
    cpu_l = [moy_cpu, med_cpu, iqv_cpu, trust_cpu, value_cpu]
    ram_l = [moy_ram, med_ram, iqv_ram, trust_ram, value_ram]
    vz.plot(nodes, cpu_l, ram_l)

    requests.post(simulator_url + '/update_scores', json=payload)
