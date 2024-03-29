import plotly.graph_objects as pgo

#compte du nombre de nodes
def nb_nodes(nodes):
    i=0
    for node in nodes:
        i+=1
    return i

#ajout du nouveau score
def append_m(nodes, list, payload, name_method):

    for node in nodes:
        node1 = int(node)
        score = payload[node][name_method]
        list[node1].append(score)

#maj des plots
def maj_figure(list, xn, n, path):
    fig = pgo.Figure(layout=pgo.Layout(title="Méthods for "+path+" on the node n°"+str(n)))
    fig.update_layout(xaxis_title="Time",yaxis_title="Score")
    for method in list:
        y = method[1][n]
        fig.add_trace(pgo.Scatter(x=xn, y=y, mode='lines+markers', name=method[0]))

    fig.write_html("plot/"+path+"/node_" + str(n) +".html", auto_open=True)

def plot(nodes, cpu_l, ram_l):
    if (nodes !={}):
        if (cpu_l[0][0]!=[]):
            #Récupération nombre d'élement pour l'abscisse
            n = len(cpu_l[0][0])

            cpu= [["Moyenne", cpu_l[0]],
            ["Mediane", cpu_l[1]],
            ["Equart interquartile", cpu_l[2]],
            ["Trustman", cpu_l[8]],
            ["Moyenne Geometrique",cpu_l[3]],
            ["Mid range",cpu_l[4]],
            ["Moyenne harmonique",cpu_l[5]],
            #["Moyenne de Lehmer",cpu_l[6]],
            ["PeerTrust",cpu_l[7]],
            ["CPU_Value", cpu_l[9]]]

            ram= [["Moyenne", ram_l[0]],
            ["Mediane", ram_l[1]],
            ["Equart interquartile", ram_l[2]],
            ["Trustman", ram_l[8]],
            ["Moyenne Geometrique",ram_l[3]],
            ["Mid range",ram_l[4]],
            ["Moyenne harmonique",ram_l[5]],
            #["Moyenne de Lehmer",ram_l[6]],
            ["PeerTrust",ram_l[7]],
            ["RAM_Value", ram_l[9]]]

            if (n==1):
                for node in nodes:
                    #Initialisation du graphe si première valeur de score
                    maj_figure(cpu, [0], int(node), "cpu")
                    maj_figure(ram, [0], int(node), "ram")
            else:
                x = []
                for i in range(n):
                    x.append(i)

                for node in nodes:
                    #Maj du graphe avec les nouvelles valeurs de score
                    maj_figure(cpu, x,  int(node), "cpu")
                    maj_figure(ram, x,  int(node), "ram")

def plot_score_glob(nodes, l, name):
    if (nodes !={}):
        if (l[0]!=[]):
            n = len(l[0])

            xn = []
            for i in range(n):
                xn.append(i)

            score = pgo.Figure(layout=pgo.Layout(title="Global Score for the function "+name))
            score.update_layout(xaxis_title="Time",yaxis_title="Score")
            for node in nodes:
                yn = l[int(node)]
                score.add_trace(pgo.Scatter(x=xn, y=yn, mode='lines+markers', name="Node_"+node))

            score.write_html("plot/global/evol_score_node.html", auto_open=True)
