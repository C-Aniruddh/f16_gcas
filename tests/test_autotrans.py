from os import path
from unittest import TestCase

from benchmarks.models.autotrans import _dosim
from numpy import array
from numpy.testing import assert_equal
from pandas import read_csv

TEST_DIR = path.dirname(__file__)


class AutotransTestCase(TestCase):
    def test_correct_output(self):
        inputs = read_csv(path.join(TEST_DIR,  "data", "autotrans_inputs.csv"))
        outputs = read_csv(path.join(TEST_DIR, "data", "autotrans_outputs.csv"))

        T = inputs["t"].to_numpy()
        U_cols = inputs.columns[1:3]
        U = inputs[U_cols].to_numpy()

        _, _, trajectories = _dosim(T, U.T)

        assert_equal(outputs.to_numpy(), trajectories)
