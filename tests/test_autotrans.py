from os import path

from benchmarks.models.autotrans import _dosim
from numpy import array, float64
from numpy.testing import assert_allclose, assert_equal
from pandas import read_csv
from pytest import fixture

TEST_DIR = path.dirname(__file__)


@fixture
def inputs():
    inputs_path = path.join(TEST_DIR,  "data", "autotrans_inputs.csv")
    return read_csv(inputs_path).to_numpy()


@fixture
def outputs():
    outputs_path = path.join(TEST_DIR, "data", "autotrans_outputs.csv")
    return read_csv(outputs_path).to_numpy()


def test_autotrans(inputs, outputs):
    _, states, trajectories = _dosim(inputs[:, 0], inputs[:, 1:3].T)
    real_trajectories = outputs[:, 0:2].astype(float64)
    real_states = outputs[:, 2]

    assert_allclose(trajectories, real_trajectories, rtol=2e-4)
    assert_equal(states, real_states)

