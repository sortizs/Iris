import numpy as np
import matplotlib.pyplot as plt
import os

class graph:
    def graphData(times, emotions, values):

        x = np.arange(len(times))
        y = values

        plt.plot(x, y, 'c--')
        plt.title('Emociones predominantes')
        plt.ylabel('Intensidad')
        plt.xlabel('Tiempo (ms)')
        
        for idx, emotion in enumerate(emotions):
            plt.text(x[idx], y[idx], emotion.capitalize())

        osPath = r'%s' % os.getcwd().replace('\\','/')
        path = osPath + '/media/result/'

        # plt.show()
        plt.savefig(path + 'result.png')
