import state
import helper

bits = [1,0]
#1  creating a qubit state
psi=state.qubit(1/2**0.5)
print('\n New qubit state psi',psi)

#2  creating a state and then normalize it
psi=state.State([1,2])
print('\n New state psi', psi)

psi=state.State.normalize(psi)
print('\nNormalized psi', psi)

#3  Adjoint of state
print('\nAdjoint of psi',state.State.adjoint(psi))

#3  Density of state
print('\nrho=',state.State.density(psi))

#produce the iterable cartesian of nbits {0, 1}


for bits in helper.bitprod(1):
#4  Amplitude of state
    print(f"\nAmplitude for {bits}:")
    print(psi.ampl(*bits))
#5  Probability of state
    print(f"\nProbability for {bits}:")
    print(psi.prob(*bits))
#6  Phase of state
    print(f"\nPhase for {bits}:")
    print(psi.phase(*bits))

#7  Find state with highest probability
print('\nState with highest probability',psi.maxprob())

#8  Produce the all-0/1 basis vector for `d` qubits.0
print('\nphi=',state.zeros_or_ones(1,0)
)

#9  Produce state with 'd' |0>, eg., |0000>.
print("\nProduce state with '2' |0>, i.e |00>\n",state.zeros(2))

#10 Produce state with 'd' |1>, eg., |1111>.
print("\nProduce state with '2' |1>, i.e |11>\n",state.ones(2))

#11 Product state |+>
print("\nProduct state |+>\n",state.plus(1))

#12 Product state |->
print("\nProduct state |->\n",state.minus(1))

#13 Product state |i>
print("\nProduct state |i>\n",state.plusi(1))

#13 Product state |-i>
print("\nProduct state |-i>\n",state.minusi(1))

#14 Produce a state from a given bit sequence, eg., |0101>
print("\nProduce a state from a given bit sequence, eg., |01>\n", state.bitstring(0,1))

#15 Produce random combination of |0> and |1>
print("\nProduce random combination of |0> and |1>\n",state.rand_bits(2))

