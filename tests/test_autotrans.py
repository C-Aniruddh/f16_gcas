from os import path
from unittest import TestCase

from benchmarks.models.autotrans import sim_autotrans
from numpy import array
from numpy.testing import assert_equal
from pandas import read_csv


class AutotransTestCase(TestCase):
    def test_correct_output(self):
        test_dir = path.dirname(__file__)
        inputs = read_csv(path.join(test_dir, "test_autotrans_inputs.csv"))
        outputs = read_csv(path.join(test_dir, "test_autotrans_outputs.csv"))

        simT = 30
        T = inputs["t"].tonumpy()
        U = inputs[["u1", "u2"]].tonumpy()
        trajectories, _ = simulate_autotrans(simT, T, U)

        assert_equal(outputs.tonumpy(), trajectories)
