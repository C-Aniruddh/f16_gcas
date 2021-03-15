from pystaliro import staliro
from pystaliro.models import Blackbox
from pystaliro.options import Options, SignalOptions
from pystaliro.optimizers import dual_annealing
from tltk_mtl import Predicate

from ._benchmark import Benchmark
from ._autotrans import simulate_autotrans


def _s3_blackbox(X, U):
    results = simulate_autotrans(X, U)
    return results[1]


class BenchmarkS3(Benchmark):
    def run(self):
        phi = "[]_[0, 30] ((!(gear1) /\ X (gear1))-> X []_[0, 2.5] (gear1))"
        preds = {"gear1": Predicate("gear1", [], [])}
        options = Options(
            runs=50,
            iterations=100,
            seed=131013014,
            static_parameters=[],
            signals=[
                SignalOptions((0, 100), control_points=7),
                SignalOptions((0, 350), control_points=3),
            ],
        )
        model = Blackbox(_s3_blackbox)

        staliro(phi, preds, autotrans, options)
