from math import pi

from numpy import array, float64, deg2rad
from staliro import staliro
from staliro.models import blackbox
from staliro.options import Options
from staliro.optimizers.uniform_random import UniformRandom

from partx.interfaces.run_psystaliro_UR import PartX_UR 

from staliro.specification import PredicateProps, TLTK

from .models.f16_alt_2338_5 import f16_blackbox, get_static_params, F16_PARAM_MAP
from .benchmark import Benchmark

import pathlib

from collections import OrderedDict

MAX_BUDGET = 5000
NUMBER_OF_MACRO_REPLICATIONS = 50
ALTITUDE = 2338.5

class BenchmarkF16UR_2338_5(Benchmark):
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
    
        self.optimizer = PartX_UR(
                number_of_macro_replications=NUMBER_OF_MACRO_REPLICATIONS,
                benchmark_name="f16_alt{}_budget_{}".format(str(ALTITUDE).replace(".","_"), MAX_BUDGET),
                initial_seed=1000,
                test_function_dimension=len(static_params),
                number_of_samples = MAX_BUDGET,
                results_folder = "f16_final_results_UR_replications",
            )

    def run(self):
        return staliro(
            f16_blackbox,
            self.specification,
            self.optimizer,
            self.options
        )
