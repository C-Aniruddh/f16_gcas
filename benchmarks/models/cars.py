from numpy import array, float32, float64, row_stack
from staliro.models import blackbox

eng = None
MODEL_NAME = "cars"


@blackbox
def cars_blackbox(X, T, U):
    try:
        from matlab import double as mdouble
        from matlab.engine import start_matlab
    except ImportError:
        raise NotImplementedError("You need MATLAB python engine installed to use this model")

    global eng

    if eng is None:
        eng = start_matlab()

    sim_opts = eng.simget(MODEL_NAME)
    sim_opts = eng.simset(sim_opts, "SaveFormat", "Array")
    sim_u = mdouble(row_stack((T, U)).T.tolist())
    sim_t = mdouble([0, max(T)])

    timestamps, _, data = eng.sim(MODEL_NAME, sim_t, sim_opts, sim_u, nargout=3)
    np_timestamps = array(timestamps, dtype=float32).flatten()
    np_data = array(data, dtype=float64)

    return np_data, np_timestamps

