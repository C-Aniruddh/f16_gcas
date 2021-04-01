from aerobench.run_f16_sim import run_f16_sim
from aerobench.examples.gcas.gcas_autopilot import GcasAutopilot
from numpy import array, float32, float64
from pystaliro.models import Blackbox


@Blackbox
def f16_blackbox(X, T, _):
    power, alpha, beta, alt, vel, phi, theta, psi = X
    init_cond = [vel, alpha, beta, phi, theta, psi, 0, 0, 0, 0, 0, alt, power]
    step = 1/30
    autopilot = GcasAutopilot(init_mode="roll", stdout=False, gain_str="old")

    print(f"Simulating F16 with initial conditions: {init_cond}")

    result = run_f16_sim(init_cond, max(T), autopilot, step, extended_states=True)
    trajectories = result["states"][:, 11:12].T.astype(float64)
    timestamps = array(result["times"], dtype=(float32))

    return trajectories, timestamps

