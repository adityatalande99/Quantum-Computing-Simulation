import math
from absl import app

import bell
import ops
import state


def alice_manipulates(psi: state.State, bit0: int, bit1: int) -> state.State:
    """Alice encodes 2 classical bits in her 1 qubit."""
    print(f'Initial psi (Alice): {psi}')
    
    ret = ops.Identity(2)(psi)
    print(f'After Identity operation: {ret}')
    
    if bit0:
        ret = ops.PauliX()(ret)
        print(f'After PauliX operation for bit0={bit0}: {ret}')
    if bit1:
        ret = ops.PauliZ()(ret)
        print(f'After PauliZ operation for bit1={bit1}: {ret}')
    
    return ret


def bob_measures(psi: state.State, expect0: int, expect1: int):
    """Bob measures both bits (in computational basis)."""
    print(f'Initial psi (Bob): {psi}')
    
    # Change Hadamard basis back to computational basis.
    psi = ops.Cnot(0, 1)(psi)
    print(f'After CNOT operation: {psi}')
    
    psi = ops.Hadamard()(psi)
    print(f'After Hadamard operation: {psi}')
    
    p0, _ = ops.Measure(psi, 0, tostate=expect1)
    p1, _ = ops.Measure(psi, 1, tostate=expect0)
    
    if (not math.isclose(p0, 1.0, abs_tol=1e-6) or
        not math.isclose(p1, 1.0, abs_tol=1e-6)):
        raise AssertionError(f'Invalid Result p0 {p0} p1 {p1}')
    
    print(f'Measurement results: p0={p0}, p1={p1}')
    print(f'Expected/matched: |{expect0}{expect1}>.')


def main(argv):
    if len(argv) > 1:
        raise app.UsageError('Too many command-line arguments.')

    # Step 1: Alice and Bob share an entangled pair, and separate.
    psi = bell.bell_state(0, 0)
    print(f'Initial Bell state: {psi}')

    # Alice manipulates her qubit and sends her 1 qubit back to Bob,
    # who measures. In the Hadamard basis he would get b00, b01, etc.
    # but we're measuring in the computational basis by reverse
    # applying Hadamard and Cnot.
    for bit0 in range(2):
        for bit1 in range(2):
            print(f'\nEncoding bits: bit0={bit0}, bit1={bit1}')
            psi_alice = alice_manipulates(psi, bit0, bit1)
            bob_measures(psi_alice, bit0, bit1)


if __name__ == '__main__':
    app.run(main)
