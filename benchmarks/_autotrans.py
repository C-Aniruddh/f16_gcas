import matlab
import matlab.engine
import numpy as np


def sim_autotrans(simT, T, u, tag = "default"):
    matlab_sessions = matlab.engine.find_matlab()
    eng_name = f"benchmark_{tag}"

    if eng_name not in matlab_sessions:
        eng = matlab.engine.start_matlab()
        eng.shareEngine(eng_name)
    else:
        eng = matlab.engine.connect_matlab(eng_name)

    simT = matlab.double([0, float(simT)])
    simInp = matlab.double(np.row_stack((T, u)).T.tolist())
    simOpt = eng.simget("Autotrans_shift")
    simOpt = eng.simset(simOpt, "SaveFormat", "Array")
    timestamps, _, data = eng.sim("Autotrans_shift", simT, simOpt, simInp, nargout=3)

    np_timestamps = np.array(timestamps, dtype=np.float32).flatten()
    np_data = np.array(data, dtype=np.float64).T

    return np_data[0:2], np_timestamps

