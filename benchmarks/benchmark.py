from abc import abstractmethod


class Benchmark:
    @abstractmethod
    def run(self):
        raise NotImplementedError()
