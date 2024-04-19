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