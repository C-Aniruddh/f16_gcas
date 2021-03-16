#!/usr/bin/env python3

from argparse import ArgumentParser
from importlib import import_module
from os import path, mkdir
from sys import exit

from scipy.io import savemat

ALL_BENCHMARKS = {"6a", "6b", "6c"}


def _load_module(name):
    mod_name = f"benchmark_{name}"
    return import_module(f"benchmarks.{mod_name}")


def _get_benchmark(name):
    mod = _load_module(name)
    cls_name = f"Benchmark{name.upper()}"
    ctor = getattr(mod, cls_name)

    return ctor()


def _mk_results_dict(results):
    return {f"run_{i}": result.history for i, result in enumerate(results)}


if __name__ == "__main__":
    parser = ArgumentParser(description="Run arch benchmarks")
    parser.add_argument("benchmark_names", nargs="*", help="Name of benchmarks to run")
    parser.add_argument("-a", "--all", help="Run all benchmarks", action="store_true")
    parser.add_argument("-l", "--list", help="List all benchmarks", action="store_true")
    args = parser.parse_args()

    if args.list:
        print(ALL_BENCHMARKS)
        exit(0)

    if args.all:
        benchmark_names = ALL_BENCHMARKS
    else:
        benchmark_names = set(args.benchmark_names)
        for name in benchmark_names:
            if name not in ALL_BENCHMARKS:
                raise ValueError(f"Unknown benchmark {name}")

    benchmarks = [_get_benchmark(name) for name in benchmark_names]

    if not benchmarks:
        raise ValueError("Must specify at least one benchmark to run")

    for benchmark in benchmarks:
        results = benchmark.run()

        if not path.isdir("results"):
            mkdir("results")

        filename = f"partX_trans_{name}.Arch21Bench"
        result_dict = _mk_results_dict(results)
        savemat(path.join("results", filename), result_dict, appendmat=False)
