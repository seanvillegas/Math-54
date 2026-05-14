## 2.0

\textbf{Intro:} adding leading entries example, implies multiply entries. But it doesnt. Why is this a false notion?

Range and co-domain need to be the same? I.e. same number of columns and rows (perfect squares)
    - i.e. codomain in first trans., and range in second trans

Proof by contradiction, both equations are R to R so–– why we cant do ST (assume ST are linear trans)??

S(x) = 2x, T(x) = 3x

(ST)(x) = 6x^2


S \compose T is linear, proof in 1.8 lecture


Direct Proof:

AB = A[b_1 b_2 b_p], columns of B are b_p

= [Ab_1 Ab_2 Ab_p] is m*n . Where Ab_p is columns

Why rows of A time columns of B? Does rows times rows (answer is no)? 


Understanding Does rows times rows = A time columns of B

Make B into one x vector, and then apply A to it. 
e.g.:

A= 
1 2
3 4 
B=
[
5 6 
7 8  (x_1, x_2)
]

multiply to get

19 22 x_1
43 50 x_2


matrix multiplication \implies associative \land \lnot commulative. In other words use parenthesis to dictate order of operations

A = 3*2 matrix
B = 2*2 matrix

When defined
can we say AB: 3*3?, BA: 2*2? 

defined \land same size \iff both square and same size

BUT, they still arent the same. Take A = 1, 0; 0, 0, and B = 0, 1; 0, 0. THUS AB and BA are not the same

Cant assume AB, where one is 0, thus it becomes 0. Not the same rule with \real numbers??


f(x) = 2x, g(x) = 3x

(f \compose g)(x) = 6x

[2][3] = [6]

## Transpose A^T

A^T = rows of A into columns, vice versa

First row of A becomes first column of A^T (same order of entries)

So if A is m*n, A^T is n*m !!!!!


IFF A, B same size and defined

A+B^T = A^T + B^T

AB^T = B^TA^T where m*n n*p, p*n n*m 

##

How do we create an inverse of the matrix

