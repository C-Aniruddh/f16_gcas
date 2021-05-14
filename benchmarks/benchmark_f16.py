from math import pi

from numpy import array, float64, deg2rad
from staliro import staliro
from staliro.models import Blackbox
from staliro.options import Options
from staliro.optimizers import partitioning
from staliro.optimizers.partitioning import PartitioningOptions, SamplingMethod
from tltk_mtl import Predicate

from .models.f16 import f16_blackbox, get_static_params, F16_PARAM_MAP
from .benchmark import Benchmark

from collections import OrderedDict

class BenchmarkF16(Benchmark):
    def __init__(self):
        a_matrix = array([[-1]], dtype=float64)
        b_vector = array([0], dtype=float64)

        self.phi = "[]_ts:(0, 15) altitude"
        self.preds = {"altitude": Predicate("altitude", a_matrix, b_vector)}
        self.options = Options(
            runs=50,
            iterations=100,
            seed=131013014,
            interval=(0, 15),
            static_parameters=get_static_params(F16_PARAM_MAP),
            signals=[],
        )
        self.optimizer_options = PartitioningOptions(
            subregion_file="/tmp/subregions_benchmark_f16.csv",
            region_dimension=len(static_params),
            num_partition=2,
            miscoverage_level=0.05,
            num_sampling=30,
            level=[0.5, 0.75, 0.9, 0.95],
            min_volume=0.001,
            max_budget=15_000,
            fal_num=50_000,
            n_model=1000,
            n_bo=10,
            n_b=100,
            sample_method=SamplingMethod.BAYESIAN,
            part_num=1,
        )

    def run(self):
        return staliro(
            self.phi,
            self.preds,
            f16_blackbox,
            self.options,
            partitioning,
            self.optimizer_options,
        )
