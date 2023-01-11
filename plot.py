import matplotlib.pyplot as plt

def plot(payload, name_method, nodes):
    for node in nodes:
        score = str(payload[node]["cpu_score"]) + "\n"
        file = open("plot/"+name_method+"/"+ node +".txt", "a")
        file.write(score)
        file.close()

        file = open("plot/"+name_method+"/"+ node +".txt", "r")
        x = []
        y = []
        i = 0
        for line in file:
            y.append(float(line))
            x.append(i)
            i+=1
        
        fig, ax = plt.subplots( nrows=1, ncols=1 )
        ax.plot(x,y)
        fig.savefig("plot/"+ name_method+"/curve"+node+".png")
        plt.close(fig)
        file.close()
