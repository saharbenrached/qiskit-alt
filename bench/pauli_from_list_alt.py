# Benchmark creating a SparsePauliOp from a list of strings using qiskit_alt

import random
from timeit import timeit

from qiskit_alt import QuantumOps, PauliSum_to_SparsePauliOp

random.seed(123)

def rand_label(k, n):
    return ["".join(random.choices("IXYZ", k=k)) for _ in range(n)]

qkalt_times = []

for k in (10, 100):
    for n in (10, 100, 1000, 5000, 10_000, 100_000):
        label = rand_label(k, n)
        number = 20
        t = timeit(lambda: PauliSum_to_SparsePauliOp(QuantumOps.PauliSum(label)), number=number)
        t /= number
        qkalt_times.append(t)
        print(f'k={k}, n={n}, {t} sec')

qkalt_times
