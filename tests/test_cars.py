from os import path

from benchmarks.models.cars import cars_blackbox
from numpy import array, linspace, row_stack
from numpy.testing import assert_array_almost_equal
from pandas import read_csv
from pytest import fixture
from scipy.interpolate import interp1d

TEST_DIR = path.dirname(__file__)


@fixture
def inputs():
    inputs_path = path.join(TEST_DIR, "data", "cars_inputs.csv")
    return read_csv(inputs_path)


@fixture
def times(inputs):
    return inputs["t"].to_numpy().flatten()


@fixture
def signals(inputs):
    signal_cols = inputs.columns[1:3]
    return inputs[signal_cols].to_numpy().T


@fixture
def outputs():
    outputs_path = path.join(TEST_DIR, "data", "cars_outputs.csv")
    return read_csv(outputs_path)


def test_cars(times, signals, outputs):
    trajectories, timestamps = cars_blackbox._func([], times, signals)
    real_timestamps = outputs["t"].to_numpy()
    real_trajectory_cols = outputs.columns[1:6]
    real_trajectories = outputs[real_trajectory_cols].to_numpy()

    assert_array_almost_equal(real_timestamps, timestamps, decimal=5)
    assert_array_almost_equal(real_trajectories, trajectories, decimal=5)

