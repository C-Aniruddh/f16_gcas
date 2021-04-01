import matlab
import matlab.engine
import numpy as np

engs = {}
MODEL_NAME = "Autotrans_shift"


def sim_autotrans(simT, T, u, tag = "default"):
    global engs

    if tag not in engs:
        engs[tag] = matlab.engine.start_matlab()

    eng = engs[tag]
    simT = matlab.double([0, float(simT)])
    simInp = matlab.double(np.row_stack((T, u)).T.tolist())
    simOpt = eng.simget(MODEL_NAME)
    simOpt = eng.simset(simOpt, "SaveFormat", "Array")
    timestamps, _, data = eng.sim(MODEL_NAME, simT, simOpt, simInp, nargout=3)

    np_timestamps = np.array(timestamps, dtype=np.float32).flatten()
    np_data = np.array(data, dtype=np.float64).T

    return np_data[0:2], np_timestamps

