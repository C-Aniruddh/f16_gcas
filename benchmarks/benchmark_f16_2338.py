from math import pi

from numpy import array, float64, deg2rad
from staliro import staliro
from staliro.models import blackbox
from staliro.options import Options
from staliro.optimizers.uniform_random import UniformRandom
from partx.partitioning import PartX
from partx.models import SamplingMethod, PartitioningOptions

from staliro.specification import PredicateProps, TLTK

from .models.f16_alt_2338 import f16_blackbox, get_static_params, F16_PARAM_MAP
from .benchmark import Benchmark

import pathlib

from collections import OrderedDict

BENCHMARK_NAME = "f16_alt2338_continued_sampling_10000"  # format is "f16_alt<alt>_method_budget"

home_directory = pathlib.Path().home()
result_directory = home_directory.joinpath('arch_results')
result_directory.mkdir(exist_ok=True)

benchmark_result_directory = result_directory.joinpath(BENCHMARK_NAME)
benchmark_result_directory.mkdir(exist_ok=True)

subregion_file = benchmark_result_directory.joinpath("subregions_f16.csv")

class BenchmarkF16_2338(Benchmark):
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

        self.optimizer = PartX(
            subregion_file=str(subregion_file.resolve()),
            region_dimension=len(static_params),
            num_partition=2,
            miscoverage_level=0.05,
            num_sampling=30,
            level=[0.5, 0.75, 0.9, 0.95],
            min_volume=0.001,
            max_budget=10000,
            fal_num=50_000,
            n_model=1000,
            n_bo=10,
            n_b=100,
            sample_method=SamplingMethod.BAYESIAN,
            part_num=1,
            continue_sampling_budget=100
        )

    def run(self):
        return staliro(
            f16_blackbox,
            self.specification,
            self.optimizer,
            self.options
        )
