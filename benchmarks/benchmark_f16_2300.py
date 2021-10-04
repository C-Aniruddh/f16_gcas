from math import pi

from numpy import array, float64, deg2rad
from staliro import staliro
from staliro.models import blackbox
from staliro.options import Options
from staliro.optimizers.uniform_random import UniformRandom

from partx.interfaces.run_psytaliro import PartX 

from staliro.specification import PredicateProps, TLTK

from .models.f16_alt_2300 import f16_blackbox, get_static_params, F16_PARAM_MAP
from .benchmark import Benchmark

import pathlib

from collections import OrderedDict

MAX_BUDGET = 5000
NUMBER_OF_MACRO_REPLICATIONS = 50
ALTITUDE = 2300

class BenchmarkF16_2300(Benchmark):
    def __init__(self):
        # a_matrix = array([[-1]], dtype=float64)
        # b_vector = array([0], dtype=float64)

        phi = "[](0, 15) altitude >= 0"
        preds = {"altitude": PredicateProps(0, 'float64')}

        self.specification = TLTK(phi, preds)

        static_params = get_static_params(F16_PARAM_MAP)

        self.options = Options(
            runs=1,
            iterations=MAX_BUDGET,
            seed=131013014,
            interval=(0, 15),
            static_parameters=static_params,
            signals=[],
        )

        self.optimizer = PartX(
            benchmark_name="f16_alt{}_budget_{}".format(ALTITUDE, MAX_BUDGET),
            test_function_dimension=len(static_params),
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
            number_of_macro_replications=NUMBER_OF_MACRO_REPLICATIONS,
            initial_seed=1000,
            fv_quantiles_for_gp = [0.5,0.95,0.99],
            fv_confidence_at = 0.95,
            points_for_unif_sampling = 1,
            results_folder = "f16_final_results"
        )

    def run(self):
        return staliro(
            f16_blackbox,
            self.specification,
            self.optimizer,
            self.options
        )
