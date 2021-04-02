from math import pi

from aerobench.run_f16_sim import run_f16_sim
from aerobench.examples.gcas.gcas_autopilot import GcasAutopilot
from benchmarks.models.f16 import f16_blackbox
from numpy import array, deg2rad, float32, float64
from pytest import fail


def test_f16_blackbox():
    X = [-pi / 8, (-pi / 2) * 0.3, 0]
    T = [3.51]
    U = []

    try:
        f16_blackbox._func(X, T, U)
    except AssertionError:
        fail("f16 did not successfully integrate")

