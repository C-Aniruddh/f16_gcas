from os import path
from unittest import TestCase

from benchmarks.models.autotrans import _dosim
from numpy import array
from numpy.testing import assert_equal
from pandas import read_csv

TEST_DIR = path.dirname(__file__)


class AutotransTestCase(TestCase):
    def test_correct_output(self):
        inputs = read_csv(path.join(TEST_DIR, "test_autotrans_inputs.csv"))
        outputs = read_csv(path.join(TEST_DIR, "test_autotrans_outputs.csv"))

        T = inputs["t"].tonumpy()
        U = inputs[["u1", "u2"]].tonumpy()
        _, _, trajectories = _dosim(T, U)

        assert_equal(outputs.tonumpy(), trajectories)
