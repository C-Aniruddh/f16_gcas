from numpy import array, float32, float64, row_stack
from staliro.models import Blackbox

MODEL_NAME = "Autotrans_shift"
eng = None


def _dosim(T, U):
    try:
        from matlab import double as mdouble
        from matlab.engine import start_matlab
    except ImportError:
        raise NotImplementedError("You need MATLAB python engine installed to use this model")
    else:
        global eng

        if eng is None:
            eng = start_matlab()

        sim_t = mdouble([0, max(T)])
        sim_inp = mdouble(row_stack((T, U)).T.tolist())
        sim_opt = eng.simget(MODEL_NAME)
        sim_opt = eng.simset(sim_opt, "SaveFormat", "Array")

        timestamps, _, data = eng.sim(MODEL_NAME, sim_t, sim_opt, sim_inp, nargout=3)
        np_timestamps = array(timestamps, dtype=float32).flatten()
        np_data = array(data, dtype=float64)

        return np_timestamps, np_data[:, 2], np_data[:, 0:2]


@Blackbox
def autotrans_blackbox(_, T, U):
    timestamps, _, trajectories = _dosim(T, U)
    return trajectories.T, timestamps


@Blackbox
def autotrans_gears_blackbox(_, T, U):
    timestamps, states, _ = _dosim(T, U)
    return array([states]), timestamps

