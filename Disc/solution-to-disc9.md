We are representing x under different basises. 


By definition, to create x we scale by some a \in R^n by the Basis, which in this case is P_B. It becomes apparent as you write it out, that we have expressed x. I.e.:


Given a vector v whose coordinates are given in the standard basis,
how does one use PB to find its corrdinates in the B basis?

P_B v = B_1 v_1 + ... + B_n v_n = x

Where v \in the standard basis e_1, e_n

This implies that P_B v = B_1 v_1 + ... + B_n v_n = P_B v = x.

b. What if instead we were given x with its
coordinates in the B basis?

The representation of x in B is expressed as P^{-1}_B. Implying that we use part a, P_B v = x and solve for e_1 (which I argue is v since a basis has the condition that it must be independent implying we have full rank).

P_B v = x
v = P^{-1}_B x (multiply both sides by the inverse)

We have shown that v is equal to the inverse of P^{-1}_B x.
