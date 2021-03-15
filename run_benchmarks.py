#!/usr/bin/env python3

from argparse import ArgumentParser
from importlib import import_module
from os import path, mkdir

from scipy.io import savemat


def _load_module(name):
    mod_name = f"benchmark_{name}"
    return import_module(f"benchmarks.{mod_name}")


def _get_benchmark(name, mod):
    cls_name = f"Benchmark{name.upper()}"
    ctor = getattr(mod, cls_name)

    return ctor()


def _mk_results_dict(results):
    return {f"run_{i}": result.history for i, result in enumerate(results)}


parser = ArgumentParser(description="Run arch benchmarks")
parser.add_argument("name", help="Name of benchmark to run", choices=["s3"])

if __name__ == "__main__":
    args = parser.parse_args()
    mod = _load_module(args.name)
    benchmark = _get_benchmark(args.name, mod)
    results = benchmark.run()

    if not path.isdir("results"):
        mkdir("results")

    filename = f"partX_trans_{args.name}.Arch21Bench"
    result_dict = _mk_results_dict(results)
    savemat(path.join("results", filename), result_dict, appendmat=False)
