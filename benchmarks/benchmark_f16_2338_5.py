import logging
import math

import numpy as np
import plotly.graph_objects as go
from aerobench.run_f16_sim import run_f16_sim
from aerobench.examples.gcas.gcas_autopilot import GcasAutopilot
from numpy.typing import NDArray
from staliro.core.model import Failure
from staliro.models import StaticInput, SignalTimes, SignalValues, ModelData, blackbox
from staliro.optimizers import DualAnnealing
from staliro.options import Options
from staliro.specifications import TLTK
from staliro.staliro import staliro, simulate_model
from partx.interfaces.staliro import PartX
# from .models.f16_alt_2300 import f16_blackbox, get_static_params, F16_PARAM_MAP


MAX_BUDGET = 5000
NUMBER_OF_MACRO_REPLICATIONS = 50
ALTITUDE = 2338.5

F16DataT = ModelData[NDArray[np.float_], None]


@blackbox()
def f16_model(static: StaticInput, times: SignalTimes, signals: SignalValues) -> F16DataT:
    power = 9
    alpha = np.deg2rad(2.1215)
    beta = 0
    alt = ALTITUDE
    vel = 540
    phi = static[0]
    theta = static[1]
    psi = static[2]

    initial_state = [vel, alpha, beta, phi, theta, psi, 0, 0, 0, 0, 0, alt, power]
    step = 1 / 30
    autopilot = GcasAutopilot(init_mode="roll", stdout=False, gain_str = "old")

    result = run_f16_sim(initial_state, max(times), autopilot, step, extended_states=True)
    trajectories: NDArray[np.float_] = result["states"][:, 11:12]
    timestamps: NDArray[np.float_] = result["times"]
    # print(trajectories.T)
    return ModelData(trajectories.T, timestamps)


phi = "always[0, 15] (alt >= 0)"
specification = TLTK(phi, {"alt": 0})

# optimizer = DualAnnealing()

initial_conditions = [
    math.pi / 4 + np.array([-math.pi / 20, math.pi / 30]),  # PHI
    -math.pi / 2 * 0.8 + np.array([0, math.pi / 20]),  # THETA
    -math.pi / 4 + np.array([-math.pi / 8, math.pi / 8]),  # PSI
]


optimizer = PartX(
        benchmark_name="f16_alt{}_budget_{}".format(str(ALTITUDE).replace(".","_"), MAX_BUDGET),
        test_function_dimension = 3,
        initialization_budget = 30,
        continued_sampling_budget=100,
        number_of_BO_samples=[10],
        NGP=10000,
        M = 500,
        R = 20,
        branching_factor=2,
        nugget_mean=0,
        nugget_std_dev=0.001,
        alpha=[0.05],
        delta=0.001,
        macro_replication=NUMBER_OF_MACRO_REPLICATIONS,
        fv_quantiles_for_gp = [0.5,0.95,0.99],
        results_at_confidence = 0.95,
        results_folder_name = "F16_testing"
    )

#####################################################################################################################

# Pass to Psy-Taliro and Run

# options = Options(runs=1, iterations=MAX_BUDGET, interval=(0, 50), signals=signals)

options = Options(runs=1, iterations=MAX_BUDGET, interval=(0, 15), static_parameters=initial_conditions, signals = [])

result = staliro(
            f16_model,
            specification,
            optimizer,
            options
        )
