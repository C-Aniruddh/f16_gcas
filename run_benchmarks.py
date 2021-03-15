#!/usr/bin/env python3

from argparse import ArgumentParser
from importlib import import_module


def _load_module(name):
    mod_name = f"benchmark_{name}"
    return import_module(f"benchmarks.{mod_name}")


def _get_benchmark(name, mod):
    cls_name = f"Benchmark{name.upper()}"
    ctor = getattr(mod, cls_name)

    return ctor()


parser = ArgumentParser(description="Run arch benchmarks")
parser.add_argument("name", help="Name of benchmark to run", choices=["s3"])

if __name__ == "__main__":
    args = parser.parse_args()
    mod = _load_module(args.name)
    benchmark = _get_benchmark(args.name, mod)

    benchmark.run()
