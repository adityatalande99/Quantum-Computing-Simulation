import tensor

import numpy as np
#1 Number of bits

A = tensor.Tensor([[1.0, 1.0], [1.0, -1.0]])
print('\nTensor A \n',A)

print('\n Number of bits',A.nbits)


#2 is_close to check the tensors are equal with tolerance 10^-6
H=tensor.Tensor([[1.0, 0.0], [0.0, 1.0]])

print('\nTensor H \n',H)


if (A.is_close(H)):
    print('\nTensor A equal to H')
else:
    print('\nTensor A not equal to H')

#3  Check if the tensor is Hermitian
if (A.is_hermitian):
    print('\nTensor A is Hermitian')
else:
    print('\nTensor A is not Hermitian')

#4  Check if the tensor is unitary
if (tensor.Tensor.is_unitary(A)):
    print('\nTensor A is unitary')
else:
    print('\nTensor A is not unitary')

#5  Check if this tensor is a density operator
if (tensor.Tensor.is_density(A)):
    print('\nTensor A is a density operator')
else:
    print('\nTensor A is not a density operator')

#6  Check if this tensor describes a pure state (else it is mixed).
if (tensor.Tensor.is_pure(A)):
    print('\nTensor A is a pure state') 
else:   
    print('\nTensor A is a mixed state')

#7 Check whether a tensor is a true permutation matrix.
if (tensor.Tensor.is_permutation(A)):
    print('\nTensor A is a true permutation matrix')
else:
    print('\nTensor A is not a true permutation matrix')

#7  Return the kronecker product of the object with arg.
print('\nTensor A kron A \n',tensor.Tensor.kron(A,A))

#8  Return the tensor product of this object with itself `n` times.
print('\nTensor A pow 3 \n', tensor.Tensor.kpow(A,2))