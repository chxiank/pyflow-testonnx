print(888)
import numpy as np

def uo(data, n1=7, n2=14, n3=28, n4=56):
    data = np.array(data)
    data = data.reshape(-1, 1)
    data = data.astype(np.float64)
    data = data.tolist()
    uo = []
    for i in range(len(data)):
        if i < n1 + n2 + n3 + n4:
            uo.append(0)
        else:
            uo.append(())

            uo[i] = (data[i] - min(data[i - n1:i])) / (max(data[i - n1:i]) - min(data[i - n1:i])) * 100
            uo[i] = (uo[i] - min(uo[i - n2:i])) / (max(uo[i - n2:i]) - min(uo[i - n2:i])) * 100
            uo[i] = (uo[i] - min(uo[i - n3:i])) / (max(uo[i - n3:i]) - min(uo[i - n3:i])) * 100
            