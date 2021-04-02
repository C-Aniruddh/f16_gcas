from math import pi

from numpy import array, float64
from pystaliro import staliro
from pystaliro.models import Blackbox
from pystaliro.options import Options
from pystaliro.optimizers import partitioning
from pystaliro.optimizers.partitioning import PartitioningOptions, SamplingMethod
from tltk_mtl import Predicate

from .models.f16 import f16_blackbox
from ._benchmark import Benchmark


class BenchmarkF16(Benchmark):
    def __init__(self):
        a_matrix = array([[-1]], dtype=float64)
        b_vector = array([0], dtype=float64)

        self.phi = "[]_ts:(0, 15) altitude"
        self.preds = {"altitude": Predicate("altitude", a_matrix, b_vector)}

        static_params = [
            (pi/4) +  array((-pi/20, pi/30)),  # phi
            (-pi/2)*0.8 + array((0, pi/20)),  # theta
            (-pi/4) + array((-pi/8, pi/8)),  # psi
        ]

        self.options = Options(
            runs=1,
            iterations=100,
            seed=131013014,
            interval=(0, 15),
            static_parameters=static_params,
            signals=[],
        )
        self.optimizer_options = PartitioningOptions(
            subregion_file = "/tmp/subregions_benchmark6a.csv",
            region_dimension = len(static_params),
            num_partition = 2,
            miscoverage_level = 0.05,
            num_sampling = 20,
            level = [0.5, 0.75, 0.9, 0.95],
            min_volume = 0.001,
            max_budget = 15_000,
            fal_num = 50_000,
            n_model = 20,
            n_bo = 10,
            n_b = 100,
            sample_method = SamplingMethod.BAYESIAN,
            part_num = 1
        )

    def run(self):
        return staliro(
                self.phi,
                self.preds,
                f16_blackbox,
                self.options,
                partitioning,
                self.optimizer_options
        )

