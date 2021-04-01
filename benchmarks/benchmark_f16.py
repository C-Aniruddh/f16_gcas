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

        self.phi = "[]_ts:(0, inf) altitude"
        self.preds = {"altitude": Predicate("altitude", a_matrix, b_vector)}
        self.options = Options(
            runs=1,
            iterations=100,
            seed=131013014,
            interval=(0, 3.51),
            static_parameters=[
                (0, 10),  # power (int: 0-10)
                (0, 2 * pi),  # alpha (rad: 0-2pi)
                (0, 2 * pi),  # beta  (rad: 0-2pi)
                (1000, 1100),  # altitude (int: 1000-1100)
                (500, 600),  # velocity (int: 500-600)
                (0, 2 * pi),  # phi (rad: 0-2pi)
                (0, 2 * pi),  # theta (rad: 0-2pi)
                (0, 2 * pi),  # psi (rad: 0-2pi)
            ],
            signals=[],
        )
        self.optimizer_options = PartitioningOptions(
            subregion_file = "/tmp/subregions_benchmark6a.csv",
            region_dimension = 8,
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

