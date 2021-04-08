import matlab
import matlab.engine
import numpy as np
from staliro.models import Blackbox

MODEL_NAME = "Autotrans_shift"
eng = None


def _dosim(T, U):
    global eng

    if eng is None:
        eng = matlab.engine.start_matlab()

    sim_t = matlab.double([0, max(T)])
    sim_inp = matlab.double([np.row_stack(T, U).T.tolist()])
    sim_opt = eng.simget(MODEL_NAME)
    sim_opt = eng.simset(sim_opt, "SaveFormat", "Array")

    timestamps, states, data = eng.sim(MODEL_NAME, sim_t, sim_opt, sim_inp, nargout=3)
    np_timestamps = np.array(timestamps, dtype=np.float32).flatten()
    np_states = np.array(states, dtype=int)
    np_data = np.array(data, dtype=np.float64).T

    return np_timestamps, np_states, np_data


@Blackbox
def autotrans_blackbox(_, T, U):
    timestamps, _, trajectories = _dosim(T, U)
    return trajectories, timestamps


@Blackbox
def autotrans_gears_blackbox(_, T, U):
    timestamps, states, _ = _dosim(T, U)
    return states, timestamps
