import math
from abc import abstractmethod


class IDecayFunction:
    @abstractmethod
    def __call__(self, decay: float, step: int, total_steps: int):
        pass


class ConstantDecay(IDecayFunction):
    def __call__(self, decay: float, step: int, total_steps: int):
        return decay


class ThresholdDecay(IDecayFunction):
    def __call__(self, decay: float, step, total_steps: int):
        return min(decay, (1 + step) / (10 + step))


class ExpDecay(IDecayFunction):
    def __init__(self, beta: float):
        self.beta = beta

    def __call__(self, decay: float, step, total_steps: int):
        x = step / total_steps
        return decay * (1 - math.exp(-x * self.beta))


EMA_DECAY_FUNCTIONS = {"constant": ConstantDecay, "threshold": ThresholdDecay, "exp": ExpDecay}