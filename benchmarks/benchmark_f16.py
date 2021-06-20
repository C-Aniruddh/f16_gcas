from math import pi

from numpy import array, float64, deg2rad
from staliro import staliro
from staliro.models import blackbox
from staliro.options import StaliroOptions
from staliro.optimizers.uniform_random import UniformRandom
from partx.partitioning import PartX
from partx.models import SamplingMethod, PartitioningOptions
from tltk_mtl import Predicate

from staliro.specification import PredicateProps, TLTK

from .models.f16 import f16_blackbox, get_static_params, F16_PARAM_MAP
from .benchmark import Benchmark

import pathlib

from collections import OrderedDict

USE_PARTX = True

home_directory = pathlib.Path().home()
result_directory = home_directory.joinpath('arch_results')
result_directory.mkdir(exist_ok=True)

subregion_file = result_directory.joinpath("subregions_f16.csv")

class BenchmarkF16(Benchmark):
    def __init__(self):
        # a_matrix = array([[-1]], dtype=float64)
        # b_vector = array([0], dtype=float64)

        phi = "[](0, 15) altitude >= 0"
        preds = {"altitude": PredicateProps(0, 'float64')}

        self.specification = TLTK(phi, preds)

        static_params = get_static_params(F16_PARAM_MAP)

        self.options = StaliroOptions(
            runs=50,
            iterations=100,
            seed=131013014,
            interval=(0, 15),
            static_parameters=static_params,
            signals=[],
        )

        if USE_PARTX:
            self.optimizer = PartX(
                subregion_file=str(subregion_file.resolve()),
                region_dimension=len(static_params),
                num_partition=2,
                miscoverage_level=0.05,
                num_sampling=30,
                level=[0.5, 0.75, 0.9, 0.95],
                min_volume=0.001,
                max_budget=3000,
                fal_num=50_000,
                n_model=1000,
                n_bo=10,
                n_b=100,
                sample_method=SamplingMethod.BAYESIAN,
                part_num=1,
                continue_sampling_budget=100
            )
        else:
            self.optimizer = UniformRandom()

    def run(self):
        return staliro(
            self.specification,
            f16_blackbox,
            self.options,
            self.optimizer
        )
