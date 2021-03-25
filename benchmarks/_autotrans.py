import matlab
import matlab.engine
import numpy as np


def sim_autotrans(simT, T, u):
    simT = matlab.double([0, float(simT)])
    simInp = matlab.double(np.row_stack((T, u)).T.astype(float).tolist())

    eng = matlab.engine.connect_matlab()
    simOpt = eng.simget("Autotrans_shift")
    simOpt = eng.simset(simOpt, "SaveFormat", "Array")
    timestamps, _, data = eng.sim("Autotrans_shift", simT, simOpt, simInp, nargout=3)

    np_timestamps = np.array(timestamps).flatten()
    np_data = np.array(data).T

    print(np_timestamps)
    print(np_data[0:2])

    return np_data[0:2, :], np_timestamps

