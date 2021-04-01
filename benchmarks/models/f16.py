from aerobench.run_f16_sim import run_f16_sim
from aerobench.examples.gcas.gcas_autopilot import GcasAutopilot
from pystaliro.models import Blackbox


@Blackbox
def f16_blackbox(X, T, _):
    power, alpha, beta, alt, vel, phi, theta, psi = X
    init_cond = [vel, alpha, beta, phi, theta, psi, 0, 0, 0, 0, 0, alt, power]
    step = 1/30
    autopilot = GcasAutopilot(init_mode="roll", stdout=False, gain_str="old")
    result = run_f16_sim(init_cond, max(T), autopilot, step, extended_states=True)

    return result["states"][:, "alt"], result["times"]

