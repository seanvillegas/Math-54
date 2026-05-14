(1, 2) (2, 1) (2,2)

(3, 4) = (2,2) + (1, 2) because

(2, 2) = 2/3 ((1, 2) + (2, 1))

or you can 

state that v_1 to v_n is dependent, s.t. 
one:
c_1v_1 + ... + c_{n-1}v_{n-1} = v_n

two:
take any vector, say w

w = a_1v_1 + a_nv_n

then since we know v_n is dependent, we can plug in a_n into the expression and write in dependence

**remember you cant multiply vectors, a_n represents the coefficent matrix or scalar.**

w =  a_1v_1 + a_n(c_1 v_1 + ... + c_n v_{n-1})

w = (a_1 + c_1)v_1 + ... + (a_{n-1} + a_nc_{n-1})v_{n-1}


