from numpy import array
from staliro import staliro
from staliro.options import Options, SignalOptions
from staliro.optimizers import partitioning
from staliro.optimizers.partitioning import PartitioningOptions, SamplingMethod
from tltk_mtl import Predicate

from .benchmark import Benchmark
from .models import autotrans_gears_blackbox


class Benchmark5(Benchmark):
    def __init__(self):
        self.phi = "[]_[0, 30] ((!gear3 /\ X gear3) -> X []_[0, 2.5] (gear3))"
        self.preds = {
            "gear3": Predicate("gear3", array([[1], [-1]]), array([2.5, -3.5]))
        }
        self.options = Options(
            runs=50,
            iterations=100,
            seed=131013014,
            interval=(0, 30),
            static_parameters=[],
            signals=[
                SignalOptions((0, 100), control_points=7),
                SignalOptions((0, 350), control_points=3),
            ],
        )
        dimensions = len(self.options.bounds)
        self.optimizer_options = PartitioningOptions(
            subregion_file="/tmp/subregions_benchmark5.csv",
            region_dimension=dimensions,
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
            autotrans_gears_blackbox,
            self.options,
            partitioning,
            self.optimizer_options,
        )
