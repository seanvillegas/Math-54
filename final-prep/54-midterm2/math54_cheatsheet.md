# MATH 54 — Midterm 2 Cheat Sheet
**Sections 4.1–4.6, 5.1–5.5, 6.1–6.5 | Lay, McDonald & Lay**

---

## Topics Confirmed On Midterm *(Lecture, lines 5–18)*

Change of coordinates · Matrix of linear transformation · Dimension / Rank / Nullity · Rank-Nullity theorem · Diagonalization · Dot product · Orthogonal sets/bases · Gram-Schmidt · Least-squares · QR decomposition · Proof problems ("promised easy")

**Not on midterm:** General inner product spaces, models → final only.

---

## CH 4: Vector Spaces

### 4.1 Vector Space / Subspace

**Definition.** A *vector space* $V$ satisfies 10 axioms (closure under $+$ and scalar mult, associativity, commutativity, identity $\mathbf{0}$, additive inverse, distributivity ×2, scalar-mult associativity, scalar identity 1).

**Subspace test (all 3 required):**
1. $\mathbf{0} \in H$
2. $\mathbf{u}, \mathbf{v} \in H \implies \mathbf{u} + \mathbf{v} \in H$
3. $\mathbf{u} \in H,\ c \in \mathbb{R} \implies c\mathbf{u} \in H$

**Shortcut (iff):** $H = \text{Span}\{\mathbf{v}_1,\ldots,\mathbf{v}_k\} \iff H$ is a subspace. Skip all 10 axioms **only if** $H$ is already expressed as an explicit span.

---

### 4.2 Null Space, Column Space, Row Space

| Space | Definition | Basis |
|---|---|---|
| $\text{Null}(A)$ | $\{\mathbf{x} : A\mathbf{x} = \mathbf{0}\}$ | Parametric vectors from $A\mathbf{x}=\mathbf{0}$ |
| $\text{Col}(A)$ | Span of columns of $A$ | Pivot columns of **original** $A$ (not RREF) |
| $\text{Row}(A)$ | Span of rows of $A$ | Nonzero rows of RREF of $A$ |

**Warning:** Row operations preserve row space, not column space. Never take $\text{Col}(A)$ basis from RREF.

---

### 4.3 Linear Independence

**Definition.** $\{\mathbf{v}_1,\ldots,\mathbf{v}_k\}$ is linearly independent (LI) iff
$$c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k = \mathbf{0} \implies c_1 = \cdots = c_k = 0.$$

**In $P_n$:** Set $\sum c_i p_i(t) = 0$ (zero polynomial). Match coefficients of $1, t, t^2, \ldots$ independently. Solve resulting homogeneous system. LI iff all $c_i = 0$.

---

### 4.4–4.5 Basis, Dimension, Rank-Nullity

**Definition.** $S$ is a basis for $V$ iff (1) $S$ is LI and (2) $S$ spans $V$. Both required.

**Rank-Nullity Theorem:**
$$\text{rank}(A) + \text{nullity}(A) = n \qquad (n = \text{number of columns of } A)$$

where $\text{rank}(A) = \dim \text{Col}(A) = \dim \text{Row}(A) = \#\text{pivot columns}$, and $\text{nullity}(A) = \dim \text{Null}(A) = \#\text{free variables}$.

---

### 4.6 Change of Basis / Matrix of Linear Transformation

**Coordinate vector:** If $\mathcal{B} = \{\mathbf{b}_1,\ldots,\mathbf{b}_n\}$ is a basis,
$$[\mathbf{x}]_\mathcal{B} = (c_1,\ldots,c_n)^T \quad \text{where} \quad \mathbf{x} = c_1\mathbf{b}_1 + \cdots + c_n\mathbf{b}_n.$$
Find by row-reducing $[\mathbf{b}_1 \mid \cdots \mid \mathbf{b}_n \mid \mathbf{x}]$.

**Matrix of $T$ relative to $\mathcal{B}$:**
$$M_\mathcal{B} = \bigl[[T(\mathbf{b}_1)]_\mathcal{B} \;\big|\; [T(\mathbf{b}_2)]_\mathcal{B} \;\big|\; \cdots \;\big|\; [T(\mathbf{b}_n)]_\mathcal{B}\bigr]$$
Columns = $\mathcal{B}$-coordinate vectors of the images of each basis vector.

---

## CH 5: Eigenvalues & Diagonalization

### 5.1–5.2 Eigenvalues, Eigenvectors, Characteristic Polynomial

**Definition.** $\lambda$ is an *eigenvalue* of $A$ iff $\exists$ nonzero $\mathbf{v}$ with $A\mathbf{v} = \lambda\mathbf{v}$.

**Characteristic polynomial:**
$$p(\lambda) = \det(A - \lambda I)$$
Eigenvalues are roots of $p(\lambda) = 0$.

**Eigenspace:** $E_\lambda = \text{Null}(A - \lambda I)$. Basis: row-reduce $(A - \lambda I)$, extract free-variable vectors.

**Shortcut (iff):** $A$ upper or lower triangular $\iff$ eigenvalues are the diagonal entries. Valid **only** for triangular $A$.

**Multiplicities:**
- Algebraic multiplicity: power of $(\lambda - \lambda_0)$ in $p(\lambda)$
- Geometric multiplicity: $\dim \text{Null}(A - \lambda_0 I)$
- Always: $1 \leq \text{geo. mult} \leq \text{alg. mult}$

---

### 5.3 Diagonalization

**Definition.** $A$ is *diagonalizable* iff $A = PDP^{-1}$ for invertible $P$ and diagonal $D$.

**Necessary and sufficient:**
$$A \text{ diagonalizable} \iff \text{geo. mult}(\lambda) = \text{alg. mult}(\lambda) \text{ for ALL eigenvalues } \lambda$$

**Sufficient only:** $n$ distinct eigenvalues $\implies$ diagonalizable. Converse **fails**.

**To check without fully diagonalizing:** For each repeated $\lambda$, compute $\text{nullity}(A - \lambda I)$. If nullity $<$ alg. mult for any $\lambda$: not diagonalizable.

**Computing $A^k$** — PRECONDITION (iff): $A$ must be diagonalizable:
$$A^k = P D^k P^{-1}, \qquad D^k = \text{diag}(\lambda_1^k, \ldots, \lambda_n^k)$$
If $A$ is not diagonalizable, this formula does not apply.

---

### 5.5 Complex Eigenvalues

If $A$ is real and $\lambda = a + bi$ is an eigenvalue $\implies \bar{\lambda} = a - bi$ is also an eigenvalue. Eigenvectors come in conjugate pairs. Applies only when $A$ has real entries.

**Eigenspace for $\lambda = a+bi$:** Solve $(A - \lambda I)\mathbf{v} = \mathbf{0}$ over $\mathbb{C}$; same row-reduction procedure as real case.

---

## CH 6: Orthogonality & Least Squares

### 6.1 Inner Product, Length, Angle

$$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i, \qquad \|\mathbf{u}\| = \sqrt{\mathbf{u} \cdot \mathbf{u}}, \qquad \cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\,\|\mathbf{v}\|}$$

**Orthogonality:** $\mathbf{u} \perp \mathbf{v} \iff \mathbf{u} \cdot \mathbf{v} = 0$

**Pythagorean identity (iff):**
$$\|\mathbf{u}+\mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 \iff \mathbf{u} \perp \mathbf{v}$$

---

### 6.2 Orthogonal Sets

**Definition.** $\{\mathbf{u}_1,\ldots,\mathbf{u}_k\}$ is *orthogonal* if $\mathbf{u}_i \cdot \mathbf{u}_j = 0$ for all $i \neq j$ and no $\mathbf{u}_i = \mathbf{0}$.

**Theorem.** An orthogonal set is automatically LI.

**Shortcut (iff):** $n$ orthogonal nonzero vectors in $\mathbb{R}^n \iff$ basis for $\mathbb{R}^n$.

**Orthonormal columns (iff):** $U$ has orthonormal columns $\iff U^T U = I$. Does **not** imply $UU^T = I$ unless $U$ is square.

---

### 6.3 Orthogonal Projection

**Onto vector $\mathbf{u}$** — PRECONDITION: $\mathbf{u} \neq \mathbf{0}$:
$$\text{proj}_{\mathbf{u}}\,\mathbf{y} = \frac{\mathbf{y} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}\,\mathbf{u}$$

**Onto subspace $W$** — PRECONDITION: $\{\mathbf{u}_1,\ldots,\mathbf{u}_k\}$ must be an **orthogonal** basis for $W$. If not, run Gram-Schmidt first:
$$\hat{\mathbf{y}} = \sum_{i=1}^k \frac{\mathbf{y} \cdot \mathbf{u}_i}{\mathbf{u}_i \cdot \mathbf{u}_i}\,\mathbf{u}_i$$

**Decomposition:** $\mathbf{y} = \hat{\mathbf{y}} + \mathbf{z}$ where $\hat{\mathbf{y}} \in W$ and $\mathbf{z} = \mathbf{y} - \hat{\mathbf{y}} \perp W$.

**Distance from $\mathbf{y}$ to $W$:** $\|\mathbf{y} - \hat{\mathbf{y}}\|$

---

### 6.4 Gram-Schmidt

**Input:** LI set $\{\mathbf{x}_1,\ldots,\mathbf{x}_p\}$. **Output:** orthogonal $\{\mathbf{u}_1,\ldots,\mathbf{u}_p\}$ with $\text{Span}\{\mathbf{u}_1,\ldots,\mathbf{u}_k\} = \text{Span}\{\mathbf{x}_1,\ldots,\mathbf{x}_k\}$ at each step.

$$\mathbf{u}_1 = \mathbf{x}_1$$
$$\mathbf{u}_k = \mathbf{x}_k - \sum_{j=1}^{k-1} \frac{\mathbf{x}_k \cdot \mathbf{u}_j}{\mathbf{u}_j \cdot \mathbf{u}_j}\,\mathbf{u}_j$$

**Normalize for orthonormal basis / QR:** $\mathbf{e}_i = \mathbf{u}_i / \|\mathbf{u}_i\|$

**Shortcut (conditional):** If $\text{Col}(A)$ has rank $r < n$, apply Gram-Schmidt to only $r$ LI columns. Detect dependence first.

---

### 6.5 Least Squares

**Problem:** $A\mathbf{x} = \mathbf{b}$ inconsistent. Find $\hat{\mathbf{x}}$ minimizing $\|\mathbf{b} - A\mathbf{x}\|$.

**Normal equations** (always valid — no invertibility precondition on this step):
$$A^T A\,\hat{\mathbf{x}} = A^T \mathbf{b}$$

**Closed-form** — PRECONDITION (iff): $A^T A$ invertible $\iff$ columns of $A$ are LI $\iff$ $A$ has full column rank:
$$\hat{\mathbf{x}} = (A^T A)^{-1} A^T \mathbf{b}$$
If $A$ is rank-deficient: $A^T A$ is singular, $(A^T A)^{-1}$ undefined. Use QR decomposition or pseudoinverse $A^+$.

**$2 \times 2$ inverse** — PRECONDITION (iff): $ad - bc \neq 0$:
$$\begin{bmatrix} a & b \\ c & d \end{bmatrix}^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$
If $ad - bc = 0$: singular matrix, division by zero — undefined.

**Least-squares error:** $\|\mathbf{b} - A\hat{\mathbf{x}}\|$. Geometrically: distance from $\mathbf{b}$ to $\text{Col}(A)$. Zero iff $\mathbf{b} \in \text{Col}(A)$.

**Least-squares line** $y = c + dx$:

$$A = \begin{bmatrix} 1 & x_1 \\ \vdots & \vdots \\ 1 & x_m \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} y_1 \\ \vdots \\ y_m \end{bmatrix}, \quad \text{solve normal equations for } (c,\, d)^T$$

---

## Proof Strategies *(Lecture-highlighted)*

| Claim | Proof structure |
|---|---|
| $\text{Col}(A^{k+1}) \subseteq \text{Col}(A^k)$ | $A^{k+1}\mathbf{v} = A^k(A\mathbf{v})$; $A\mathbf{v} \in \mathbb{R}^n$ since $A$ square |
| $A^m = 0 \implies A^n = 0$ | $\dim$ drops $\geq 1$ each step by strict containment; after $n$ steps $\dim = 0$ |
| $A^2 = I \implies \lambda \in \{\pm 1\}$ | $A\mathbf{u}=\lambda\mathbf{u} \implies \lambda^2\mathbf{u} = A^2\mathbf{u} = \mathbf{u} \implies \lambda^2=1$ |
| $A^2 = I \implies A$ diagonalizable | Rank-nullity on $(A+I)$: $\text{range}(A+I) = E_1$, $\text{null}(A+I) = E_{-1}$; $\dim E_1 + \dim E_{-1} = n$ |
| LI in $P_n$ | Set $\sum c_i p_i(t) = 0$; match coefficients of each power; solve $\implies$ all $c_i = 0$ |
