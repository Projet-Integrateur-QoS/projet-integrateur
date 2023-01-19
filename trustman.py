


#Fonction qui augment le score actuel en fonction de la resource cpu/ram
def Augmentation_score(current_score,resource): 
    new_score = 0.4*(1-current_score)*resource + current_score
    return new_score

#Fonction qui augment le score actuel en fonction de la resource cpu/ram
def Dimunition_score(current_score,resource,best_resource): 
    new_score = current_score - 0.4*((best_resource - resource)*current_score)
    return new_score


def Trustman_Scorer(dataHist):
    list_cpu = []
    list_ram = []    
    
    for node in dataHist : 
        if (dataHist[node]["cpu_score"] == None and dataHist[node]["ram_score"]== None):
            new_score_cpu = 0.5
            new_score_ram = 0.5 
        #Check si une valeur de cpu ou de ram d'une Node est à None
        if (dataHist[node]["cpu"][0] == None):
            list_cpu.append(0)
        else: 
            list_cpu.append(float(dataHist[node]["cpu"][0]))

        if dataHist[node]["ram"][0] == None : 
            #Mettre le score à 0
            list_ram.append(0)

        else:
            list_ram.append(float(dataHist[node]["ram"][0]))
    

    if(list_ram != [] and list_cpu != []):
        best_resource_cpu = max(list_cpu)
        best_resource_ram = max(list_ram)

        indice_best_cpu = list_cpu.index(max(list_cpu))
        indice_best_ram = list_ram.index(max(list_ram))
    
    #if None score à score à 0

    node_crt = dict()
    #Faire une boucle sur les nodes restant et dimunition score
    for node in dataHist :
        node_crt[node]={}
        if(dataHist[node]["cpu_score"] != None and dataHist[node]["ram_score"] != None):

            if(int(node) == indice_best_cpu) :
                new_score_cpu = Augmentation_score(float(dataHist[str(indice_best_cpu)]["cpu_score"]),best_resource_cpu)
            else : 
                #diminution
                new_score_cpu = Dimunition_score(float(dataHist[node]["cpu_score"]),float(dataHist[node]["cpu"][0]),best_resource_cpu)

            if(int(node) == indice_best_ram) :
                #Mettre à jour le score des nodes 
                new_score_ram = Augmentation_score(float(dataHist[str(indice_best_ram)]["ram_score"]),best_resource_ram)
            else : 
                new_score_ram = Dimunition_score(float(dataHist[node]["ram_score"]),float(dataHist[node]["ram"][0]),best_resource_ram)
        else:
            new_score_cpu = 0.5
            new_score_ram = 0.5 

        node_crt[node]["cpu_score"] = new_score_cpu
        node_crt[node]["ram_score"] = new_score_ram

    return node_crt
        