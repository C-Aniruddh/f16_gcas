from math import pi

from aerobench.run_f16_sim import run_f16_sim
from aerobench.examples.gcas.gcas_autopilot import GcasAutopilot
from benchmarks.models.f16 import f16_blackbox
from numpy import array, deg2rad, float32, float64
from pytest import fail


def test_f16_blackbox():
    X = [
            9,  # power
            deg2rad(2.1215),  # alpha
            0,  # beta
            1000,  # alt
            540,  # vel
            -pi / 8,  # phi
            (-pi / 2) * 0.3,  # theta
            0  # psi
    ]
    T = [3.51]

    try:
        f16_blackbox._func(X, T, [])
    except AssertionError:
        fail("f16 did not successfully integrate")

