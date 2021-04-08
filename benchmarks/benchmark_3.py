from numpy import array
from staliro import staliro
from staliro.options import Options
from staliro.optimizers import partitioning
from staliro.optimizers.partitioning import PartitioningOptions, SamplingMethod
from tltk_mtl import Predicate

from .benchmark import Benchmark
from .models import autotrans_gears_blackbox


class Benchmark3(Benchmark):
    def __init__(self):
        self.phi = "[]_[0, 30] ((!(gear1) /\ X (gear1))-> X []_[0, 2.5] (gear1))"
        self.preds = {
            "gear1": Predicate(array([[1, 0, 0], [-1, 0, 0]]), array([0.5, -1.5]))
        }
        self.options = Options()
        self.optimizer_options = PartitioningOptions()

    def run(self):
        return staliro(
            self.phi,
            self.preds,
            autotrans_gears_blackbox,
            self.options,
            partitioning,
            self.optimizer_options,
        )
