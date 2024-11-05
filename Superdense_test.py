# python3
"""Generators for various entangled states, eg., the Bell states."""

import numpy as np

import ops
import state


def bell_state(a: int, b: int) -> state.State:
  """Make one of the four bell states with a, b from {0,1}."""

  assert a in [0, 1] and b in [0, 1], 'Bits must be 0 or 1.'
  psi = state.bitstring(a, b)
  psi = ops.Hadamard()(psi)
  return ops.Cnot()(psi)

phi=bell_state(0,0)
print(phi)
