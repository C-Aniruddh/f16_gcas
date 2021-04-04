from numpy import array, float64
from pystaliro import staliro
from pystaliro.models import Blackbox
from pystaliro.options import Options, SignalOptions
from pystaliro.optimizers import partitioning
from pystaliro.optimizers.partitioning import PartitioningOptions, SamplingMethod
from tltk_mtl import Predicate

from ._autotrans import sim_autotrans
from ._benchmark import Benchmark


@Blackbox
def autotrans_blackbox(_, T, u):
    return sim_autotrans(max(T), T, u, "6a")


class Benchmark6A(Benchmark):
    def __init__(self):
        self.phi = "([]_[0, 30] (rpm3000) ->[]_[0, 4] (speed35))"
        self.preds = {
            "rpm3000": Predicate(
                "rpm3000", array([[0, 1]], dtype=float64), array([3000], dtype=float64)
            ),
            "speed35": Predicate(
                "speed35", array([[1, 0]], dtype=float64), array([35], dtype=float64)
            ),
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
        self.optimizer_options = PartitioningOptions(
            subregion_file="/tmp/subregions_benchmark6a.csv",
            region_dimension=10,
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
            autotrans_blackbox,
            self.options,
            partitioning,
            self.optimizer_options,
        )
