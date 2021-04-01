import matlab
import matlab.engine
import numpy as np

engs = {}


def sim_autotrans(simT, T, u, tag = "default"):
    global engs

    if tag not in engs:
        engs[tag] = matlab.engine.start_matlab()

    eng = engs[tag]
    TU = matlab.double(T[:, np.newaxis].tolist())
    U = matlab.double(u.T.tolist())
    timestamps, _, data, _, _, _ = eng.blackbox_autotrans(0, float(simT), TU, U, nargout=6)

    np_timestamps = np.array(timestamps, dtype=np.float32).flatten()
    np_data = np.array(data, dtype=np.float64).T

    return np_data, np_timestamps

