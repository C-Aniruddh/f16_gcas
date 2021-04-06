from numpy import array, float64
from pystaliro import staliro
from pystaliro.options import Options, SignalOptions
from pystaliro.optimizers import partitioning
from pystaliro.optimizers.partitioning import PartitioningOptions, SamplingMethod
from pystaliro.signals import ConstantInterpolatorFactory
from tltk_mtl import Predicate

from .benchmark import Benchmark
from .models.cars import cars_blackbox


class BenchmarkCC4(Benchmark):
    def __init__(self):
        pred1_Amat = array([[0, 0, 0, -1, 1]], dtype=float64)
        pred1_bvec = array([-8], dtype=float64)

        self.phi = "[]_(0, 65) <>_(0, 30) []_(0, 5) pred1"
        self.preds = {"pred1": Predicate("pred1", pred1_Amat, pred1_bvec)}
        self.options = Options(
            runs=1,
            iterations=200,
            seed=131013014,
            interval=(0, 1),
            static_parameters=[],
            signals=[
                SignalOptions((0, 1), factory=ConstantInterpolatorFactory),
                SignalOptions((0, 1), factory=ConstantInterpolatorFactory)
            ],
        )

        dims = len(self.options.bounds)
        self.optimizer_options = PartitioningOptions(
            subregion_file="/tmp/subregions_benchmarkcc4.csv",
            region_dimension=dims,
            num_partition=2,
            miscoverage_level=0.05,
            num_sampling=20,
            level=[0.5, 0.75, 0.9, 0.95],
            min_volume=0.001,
            max_budget=15_000,
            fal_num=50_000,
            n_model=20,
            n_bo=10,
            n_b=100,
            sample_method=SamplingMethod.BAYESIAN,
            part_num=1,
        )

    def run(self):
        return staliro(
            self.phi,
            self.preds,
            cars_blackbox,
            self.options,
            partitioning,
            self.optimizer_options,
        )
