import os
import requests
import time
import trustman
import peerTrust
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
peer_cpu = []
peer_ram = []
geom_cpu = []
geom_ram = []
range_cpu = []
range_ram = []
harmonic_cpu = []
harmonic_ram = []
lehmer_cpu = []
lehmer_ram = []
value_cpu= []
value_ram= []
score_glob=[]


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
            geom_cpu.append([])
            geom_ram.append([])
            peer_cpu.append([])
            peer_ram.append([])
            range_cpu.append([])
            range_ram.append([])
            harmonic_cpu.append([])
            harmonic_ram.append([])
            lehmer_cpu.append([])
            lehmer_ram.append([])
            value_cpu.append([])
            value_ram.append([])
            score_glob.append([])

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

    #Moyenne geometrique sur l'historique des Cpus et Ram
    vz.append_m(nodes, geom_cpu, payload, "cpu_score_geom")
    vz.append_m(nodes, geom_ram, payload, "ram_score_geom")

    #Mid Range sur l'historique des Cpus et Ram
    vz.append_m(nodes, range_cpu, payload, "cpu_score_range")
    vz.append_m(nodes, range_ram, payload, "ram_score_range")

    #Moyenne harmonique sur l'historique des Cpus et Ram
    vz.append_m(nodes, harmonic_cpu, payload, "cpu_score_harmonic")
    vz.append_m(nodes, harmonic_ram, payload, "ram_score_harmonic")

    #Moyenne de Lehmer sur l'historique des Cpus et Ram
    vz.append_m(nodes, lehmer_cpu, payload, "cpu_score_lehmer")
    vz.append_m(nodes, lehmer_ram, payload, "ram_score_lehmer")


    #Fonction Trustman
    trustman.Trustman_Scorer(nodes, payload)
    vz.append_m(nodes, trust_cpu, payload, "cpu_score_trust")
    vz.append_m(nodes, trust_ram, payload, "ram_score_trust")
    # plot(payload, "trustman/cpu", nodes, "cpu_score")
    # plot(payload, "trustman/ram", nodes, "ram_score")


    # Fonction PeerTrust
    peerTrust.peerTrust(nodes,payload)
    vz.append_m(nodes, peer_cpu, payload, "cpu_score_peer")
    vz.append_m(nodes, peer_ram, payload, "ram_score_peer")


    ms.list_value(nodes, value_cpu, "cpu")
    ms.list_value(nodes, value_ram, "ram")

    #Score globale en fonction de la méthode choisi : Moyenne, Mediane, Ecart interquartil( écrire IQV) ou Trustman
    #Choisir importance du taux cpu et ram (0.7 : cpu et 0.3 : ram par exemple), la somme doit valoir 1
    rate_cpu = 0.7
    rate_ram = 0.3
    name = "Moyenne"
    ms.score_glob(nodes, name, rate_cpu, rate_ram, payload)
    vz.append_m(nodes, score_glob, payload, "score_glob")

    #Plot des différentes méthodes en fonction des noeuds si on a au moins un score
    cpu_l = [moy_cpu, med_cpu, iqv_cpu, geom_cpu, range_cpu, harmonic_cpu, lehmer_cpu, peer_cpu,trust_cpu, value_cpu]
    ram_l = [moy_ram, med_ram, iqv_ram, geom_ram, range_ram, harmonic_ram, lehmer_ram, peer_ram,trust_ram, value_ram]
    vz.plot(nodes, cpu_l, ram_l)

    #plot global score
    vz.plot_score_glob(nodes, score_glob, name)

    requests.post(simulator_url + '/update_scores', json=payload)
