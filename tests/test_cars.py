from os import path

from benchmarks.models.cars import cars_blackbox
from numpy import array
from numpy.testing import assert_array_equal
from pandas import read_csv

TEST_DIR = path.dirname(__file__)


def test_cars():
    outputs_path = path.join(TEST_DIR, "data", "cars_outputs.csv")
    outputs = read_csv(outputs_path)

    X = []
    T = array([0, 20, 40, 60, 80, 100])
    U = array([[0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [0, 1]])

    trajectories, timestamps = cars_blackbox._func(X, T, U)
    real_timestamps = outputs["t"].to_numpy()
    real_trajectory_cols = ["x1", "x2", "x3", "x4", "x5"]
    real_trajectories = outputs[real_trajectory_cols].to_numpy()

    assert_array_equal(real_timestamps, timestamps)
    assert_array_equal(real_trajectories, trajectories)
