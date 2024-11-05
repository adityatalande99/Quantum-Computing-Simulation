import state
import tensor
import ops

#1  creating a qubit state psi
psi=state.qubit(1/2**0.5)

#2 Identity operator
print("\nIdentity operator\n", ops.Identity())

#3 PauliX operator
print("\nPauliX operator\n", ops.PauliX())

#4 PauliY operator
print("\nPauliY operator\n", ops.PauliY())

#5 PauiliZ operator
print("\nPauliZ operator\n", ops.PauliZ())

#5 Pauli matrices
print("\nPauli matrices\n", ops.Pauli(1))

#6 Hadamard operator
print("\nHadamard operator\n", ops.Hadamard())

#7 Phase gate, also called S or Z90. Rotate by 90 deg around z-axis.
print("\nPhase gate\n", ops.Phase())

#8 Phase gate is also called S-gate
print("\nS gate\n", ops.Sgate())

#9 T-gate, which is sqrt(S)
print("\nT gate\n", ops.Tgate())

#10 V-gate, which is sqrt(X)
print("\nV gate\n", ops.Vgate())

#11 Yroot is sqrt(Y)
print("\nYroot gate\n", ops.Yroot())

#12 RotationX operator
print("\nRotationX operator\n", ops.RotationX(0))

#13 RotationY operator
print("\nRotationY operator\n", ops.RotationY(90))

#14 RotationZ operator
print("\nRotationZ operator\n", ops.RotationZ(90))

#15 ZeroProjector operator
print("\nZeroProjector operator\n", ops.ZeroProjector(1))

#16 OneProjector operator
print("\nOneProjector operator\n", ops.OneProjector(1))

#17 Cnot gate
print("\nCnot gate\n", ops.Cnot())

#18 Cnot0 gate
print("\nCnot0 gate\n", ops.Cnot0())
ops.Operator.dump(ops.Cnot)