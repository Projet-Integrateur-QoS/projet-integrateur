import matplotlib.pyplot as plt
import os

def remove_file(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)


def plot(payload, folder, nodes, name_method):
    for node in nodes:
        score = str(payload[node][name_method]) + "\n"
        file = open("plot/"+folder+"/"+ node +".txt", "a")
        file.write(score)
        file.close()

        file = open("plot/"+folder+"/"+ node +".txt", "r")
        x = []
        y = []
        i = 0
        for line in file:
            y.append(float(line))
            x.append(i)
            i+=1

        fig, ax = plt.subplots( nrows=1, ncols=1 )
        ax.plot(x,y)
        fig.savefig("plot/"+ folder+"/curve"+node+".png")
        plt.close(fig)
        file.close()
