from matlab.engine import connect_matlab
from numpy import array, hstack


def sim_autotrans(simT, T, u):
    matlab = connect_matlab()

    matlab.workspace["u"] = u
    matlab.workspace["T"] = T

    simopt = matlab.simget("Autotrans_shift")
    simopt = matlab.simset(simopt, "SaveFormat", "Array")
    timestamps, _, data = matlab.sim(
        "Autotrans_shift", [0, simT], simopt, hstack((T, u)), nargout=3
    )
    np_data = array(data)

    return np_data[:, 0:1], array(timestamps)
