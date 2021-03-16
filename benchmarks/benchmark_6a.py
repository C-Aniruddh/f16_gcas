from numpy import array
from pystaliro import staliro
from pystaliro.options import Options, SignalOptions
from pystaliro.optimizers import partitioning
from tltk_mtl import Predicate

from ._autotrans import simulate_autotrans
from ._benchmark import Benchmark


def _6a_blackbox(_, T, u):
    return simulate_autotrans(_, T, u)


class Benchmark6a(Benchmark):
    def __init__(self):
        self.phi = "([]_[0, 30] (rpm3000) ->[]_[0, 4] (speed35))"
        self.preds = {
            "rpm3000": Predicate("rpm3000", array([0, 1]), array([3000])),
            "speed35": Predicate("speed35", array([1, 0]), array([35])),
        }
        self.options = Options(
            runs=50,
            iterations=100,
            seed=131013014,
            static_parameters=[],
            signals=[
                SignalOptions((0, 100), control_points=7),
                SignalOptions((0, 350), control_points=3),
            ],
        )
        self.model = Blackbox(_6a_blackbox)

    def run(self):
        return staliro(self.phi, self.preds, self.model, self.options, partitioning)
