from math import pi

from numpy import array, float64, deg2rad
from staliro import staliro
from staliro.models import blackbox
from staliro.options import Options
from staliro.optimizers.uniform_random import UniformRandom
from partx.partitioning import PartX
from partx.models import SamplingMethod, PartitioningOptions
from tltk_mtl import Predicate

from staliro.specification import PredicateProps, TLTK

from .models.f16 import f16_blackbox, get_static_params, F16_PARAM_MAP
from .benchmark import Benchmark

import pathlib

from collections import OrderedDict

BENCHMARK_NAME = "f16_alt2400_continued_sampling_10000"  # format is "f16_alt<alt>_method_budget"

home_directory = pathlib.Path().home()
result_directory = home_directory.joinpath('arch_results')
result_directory.mkdir(exist_ok=True)

benchmark_result_directory = result_directory.joinpath(BENCHMARK_NAME)
benchmark_result_directory.mkdir(exist_ok=True)

subregion_file = benchmark_result_directory.joinpath("subregions_f16.csv")

class BenchmarkF16UR(Benchmark):
    def __init__(self):
        # a_matrix = array([[-1]], dtype=float64)
        # b_vector = array([0], dtype=float64)

        phi = "[](0, 15) altitude >= 0"
        preds = {"altitude": PredicateProps(0, 'float64')}

        self.specification = TLTK(phi, preds)

        static_params = get_static_params(F16_PARAM_MAP)

        self.options = Options(
            runs=1,
            iterations=1,
            seed=131013014,
            interval=(0, 15),
            static_parameters=static_params,
            signals=[],
        )

        self.optimizer = UniformRandom()

    def run(self):
        return staliro(
            f16_blackbox,
            self.specification,
            self.optimizer,
            self.options
        )
