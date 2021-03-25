import matlab.engine
import numpy as np


def sim_autotrans(simT, T, u):
    eng = matlab.engine.connect_matlab()

    eng.workspace["u"] = u.tolist()
    eng.workspace["T"] = T.tolist()

    print("u", u)
    print("T", T)

    simopt = eng.simget("Autotrans_shift")
    simopt = eng.simset(simopt, "SaveFormat", "Array")
    timestamps, _, data = eng.sim(
        "Autotrans_shift", [0, float(simT)], simopt, np.row_stack((T, u)).astype(float).tolist(), nargout=3
    )
    np_data = np.array(data)

    return np_data[:, 0:1], np.array(timestamps)

