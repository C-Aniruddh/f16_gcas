from matlab import double as mdouble
from matlab.engine import start_matlab
from numpy import array, row_stack
from staliro.models import Blackbox

MODEL_NAME = "Autotrans_shift"
eng = None


def _dosim(T, U):
    global eng

    if eng is None:
        eng = start_matlab()

    sim_t = mdouble([0, max(T)])
    sim_inp = mdouble([row_stack((T, U)).T.tolist()])
    sim_opt = eng.simget(MODEL_NAME)
    sim_opt = eng.simset(sim_opt, "SaveFormat", "Array")

    timestamps, states, data = eng.sim(MODEL_NAME, sim_t, sim_opt, sim_inp, nargout=3)
    np_timestamps = array(timestamps, dtype=np.float32).flatten()
    np_states = array(states, dtype=int)
    np_data = array(data, dtype=np.float64).T

    return np_timestamps, np_states, np_data


@Blackbox
def autotrans_blackbox(_, T, U):
    timestamps, _, trajectories = _dosim(T, U)
    return trajectories, timestamps


@Blackbox
def autotrans_gears_blackbox(_, T, U):
    timestamps, states, _ = _dosim(T, U)
    return states, timestamps

