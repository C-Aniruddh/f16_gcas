from os import path
from unittest import TestCase

from benchmarks.models.autotrans import _dosim
from numpy import array, float64
from numpy.testing import assert_allclose, assert_equal
from pandas import read_csv

TEST_DIR = path.dirname(__file__)


class AutotransTestCase(TestCase):
    def setUp(self):
        inputs_path = path.join(TEST_DIR,  "data", "autotrans_inputs.csv")
        inputs = read_csv(inputs_path).to_numpy()
        _, states, trajectories = _dosim(inputs[:, 0], inputs[:, 1:3].T)

        outputs_path = path.join(TEST_DIR, "data", "autotrans_outputs.csv")
        self.outputs = read_csv(outputs_path).to_numpy()
        self.states = states
        self.trajectories = trajectories

    def test_trajectories(self):
        real_trajectories = self.outputs[:, 0:2].astype(float64)
        assert_allclose(self.trajectories, real_trajectories)

    def test_states(self):
        real_states = self.outputs[:, 2]
        assert_equal(self.states, real_states)

